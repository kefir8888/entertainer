import speech_recognition as sr
import wikipedia
from gtts import gTTS

class Speech_processor:
    def __init__ (self):
        self.init_recognition ()

    def init_recognition (self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone (device_index=0)
        wikipedia.set_lang ("ru")

    def get_audio (self):
        with self.microphone as source:
            print ("listening...")
            self.audio = self.recognizer.listen (source)

            return self.audio

    def recognize (self):
        success = True

        try:
            self.recognized = self.recognizer.recognize_google (self.audio, language = 'ru-RU')
            print (self.recognized)

        except:
            print ("cannot recognize")
            success = False

        return success, self.recognized

    def get_wiki_content (self):
        succ = True

        try:
            self.page = wikipedia.page (self.recognized)
            print (self.page.url)
            print (self.page.title)

            self.content = self.page.content # Content of page.
            self.to_generate = self.content [:100]
            print ("to generate:", self.to_generate)

        except:
            succ = False

        return succ, self.content

    def generate_mp3 (self, filename = "1.mp3"):
        print ("generating:", self.to_generate)
        
        succ = True

        try:
            tts = gTTS (self.to_generate, lang='ru')
            tts.save (filename)

        except:
            print ("cannot generate file")
            succ = False

        return succ, filename

    def search_wiki (self):
        self.get_audio ()

        succ, _ = self.recognize ()

        if (succ == True):
            print ("recognized")
            succ, _ = self.get_wiki_content ()

        else:
            print ("aborting")
            return "nothing.nothing", succ

        name = ""

        if (succ == True):
            print ("content extracted")
            succ, name = self.generate_mp3 ()

        else:
            print ("aborting")
            return "nothing.nothing", succ

        return succ, name

# class Dialogue_system:
#     def __init__ (self, speech_processor_, config_path_):
#         self.speech_processor = speech_processor
#         self.config_path      = config_path_
#
#         self.dialogues = []
#
#     def load_dialogues_content (self, path = ""):
#         if (path == ""):
#             path = self.config_path
#
#         #read, loop, add
#
#     def response_in_dialogue (self, phrase):
#         filename = ""
#
#
#
#         return filename
#
#     def search_wiki (self):
#