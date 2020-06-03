from tkinter import Label, Button

class Main_window:
    def __init__ (self, master_, robot_state_):
        self.master = master_
        self.master.title ("Controller")

        self.label = Label (self.master, text = "Controller")
        self.label.pack ()

        self.wiki_button = Button (self.master, text="Search wiki", command = self.set_wiki_search)
        self.wiki_button.pack ()

        self.football_button = Button (self.master, text="Play football", command = self.set_play_football)
        self.football_button.pack ()

        self.close_button = Button (self.master, text = "Close", command = self.master.quit)
        self.close_button.pack ()

        self.robot_state = robot_state_

    def set_wiki_search (self):
        print ("changing robot state to wiki_search")
        self.robot_state.change_state ("wiki_search")

    def set_play_football (self):
        print ("changing robot state to play_football")
        self.robot_state.change_state ("play_football")
