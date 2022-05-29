import sys, json, threading, asyncio, time, discord
sys.path.append("..")

from utils import *
from DiscordBot import DiscordBot
from TwitchBot import TwitchBot
from . import Scene

class MobileSprout:

    def __init__(self):
        print("Mobile Sprout Initialized...")

        self.settings = self.loadSettings("../userdata/auth.json")

        #Set up threads
        self.DiscordBot = DiscordBot(self.settings["DiscordData"])
        
        self.DiscordThread = threading.Thread(target=self.startDiscordBot)
        self.DiscordThread.setDaemon(True)

        self.DiscordThread.start()

        self.mainLoop()
        #self.DiscordThread.join()

        #Initialize Twitchbot
        #self.TwitchBot = TwitchBot(self.settings["TwitchData"])


    def startDiscordBot(self):
        log("Discord Bot Thread Activating...", "DEBUG")
        self.DiscordBot.runBot()

    def loadSettings(self, settings):
        with open(settings, 'r') as file:
            return json.load(file)


    def mainLoop(self):
        quit = False
        while quit == False:
            pass
