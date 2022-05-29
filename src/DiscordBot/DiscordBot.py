import discord

class DiscordBot(discord.Client):
    """
    The discord bot is simply an interface for the main application to send 
    messages to and from users.
    """

    def __init__(self, settings):
        super().__init__()
        print("Discord Bot initializing...")
        self.settings = settings

        #This becomes active only when the bot is in-play so it wont reply to random commands.
        self.listening = False
        self.activeChannel = None  #Battles can only happen in one channel


    def runBot(self):
        self.run(self.settings["Token"])


    
    async def on_message(self, message):
        """
        """
        if message.author == self.user or self.listening == False:
            return


