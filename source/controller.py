from tkinter import Tk
import os
import requests

from interface import Main_window
from speech_processing import Speech_processor#, Dialogue_system

# class Robot:
#     def __init__ (self, ip_num_, port_, autonomous_ = False):
#         self.ip_prefix = "http://"
#         self.ip_postfix = ":"
#
#         self.ip_num = ip_num_
#         self.ip     = self.ip_prefix + ip_num_ + self.ip_postfix
#         self.port   = port_
#
#         self.autonomous = autonomous_
#
#     def _send_command (self, command):
#         if (self.autonomous == True):
#             print ("Robot", self.ip, "in autonomous mode, skipping command", command)
#             return
#
#         try:
#             r = requests.get (command)
#
#         except:
#             print ("cannot send command", command, "to robot", self.ip, self.port)
#
#     def send_command (self, action, text):
#         command = self.ip + str (self.port) + "/?action=" + action + "&text=" + text
#         self._send_command (command)
#
#     def copy_file_to_robot (self, filename_local, path_remote):
#         #TODO: add checking for files that are already present
#         copy_str = "scp " + filename_local + " " + "nao@" + self.ip_num + self.ip_postfix + path_remote
#         print ("copy_str:", copy_str)
#
#         os.system ("scp " + filename_local + " " + "nao@" + self.ip_num + self.ip_postfix + path_remote)

class Robot_state:
    def __init__ (self, speech_processor_):#, robot_, dialogue_system_):
        #self.robot = robot_

        self.robot_state = "waiting"
        self.states_list = ["waiting", "wiki_search", "play_football"]

        self.speech_processor = speech_processor_
        #self.dialogue_system  = dialogue_system_

    def change_state (self, new_state):
        if (new_state in self.states_list):
            self.robot_state = new_state

        else:
            print ("cannot set state", new_state, "on robot")#, self.ip, ": no such state")
            return

        self.handle_state_change ()

    #def on_idle (self):

    # def handle_dialogue (self):
    #     #listen, recognize, ask dialogue system for response, generate
    #
    #     return succ, filename

    def handle_state_change (self):
        if (self.robot_state == "waiting"):
            return

        # succ     = False
        # filename = ""
        #
        if (self.robot_state == "wiki_search"):
            succ, filename = self.speech_processor.search_wiki ()

            print ("searched:", succ, filename)

            # if (succ == True):
            #     self.robot.copy_file_to_robot (filename, "/home/nao/sounds")
            #     self.robot.send_command ("/play_mp3", filename)

        #
        # elif (self.robot_state == "dialogue"):
        #     succ, filename = self.handle_dialogue ()
        #
        #
        # else:
        #     print ("response generation did not work out")
        #     return
        #

        print ("state", self.robot_state, "handled")

        self.change_state ("waiting")

# dialogue_system  = Dialogue_system  ()

#robot = Robot ("192.168.1.9", 9569)
#robot = Robot ("10.0.0.102", 9559)

speech_processor = Speech_processor ()
robot_state = Robot_state (speech_processor)

root = Tk ()
my_gui = Main_window (root, robot_state)
root.mainloop ()