from discord.ext import commands
import discord
import asyncio
from LuPYdisc.tools import FunctionHandler
from LuPYdisc.Class.help import Help
from LuPYdisc.Class.LUPY_READER import run_file
from LuPYdisc.Funcs import newline_char

global _client

class _LuPYClient():
    def __init__(self,  command_prefix:tuple, WhenMentioned:bool=False, intents:str="default", activity=None, case_sensitive:bool=True):
        global _client



        if   WhenMentioned and command_prefix==():   command_prefix = commands.when_mentioned_or()
        elif WhenMentioned:                          command_prefix = commands.when_mentioned_or(*command_prefix)
        
        intents=intents.lower().strip()
        if intents == "all":
            intents=discord.Intents.all()
        else:
            intents=discord.Intents.default()

        _client = commands.Bot(command_prefix=command_prefix, intents=intents, case_insensitive=False if case_sensitive else True)


class help():
    def __init__(self):
        self.title       = "LUPYBOT"
        self.embed_color = 0x000000
        self.description = """
        Below is a list of commands you can use.

        Type .help followed by the command for more details
        """


class Client():
    def __init__(self) -> None:
        self.help = _client.help

    def run(self, token):
        _client.add_cog(Help(_client))
        _client.run(token)

    def set_file(self, path, dir=None):
        _client.PATH     =path
        _client.DIRECTORY=dir

        _client.FILE_LIST_OF_LINES=[]
        run_file()





def LuPYClient(*command_prefix:str|list, WhenMentioned:bool=False, intents:str="default", activity=None, case_sensitive:bool=True):
    global _client

    Functions = FunctionHandler()

    _LuPYClient(command_prefix=command_prefix, WhenMentioned=WhenMentioned, intents=intents, activity=activity, case_sensitive=case_sensitive)
    
    
    _client.newline_char = newline_char
    _client.LUPY_FUNCS   = Functions
    _client.help         = help()
    _client.AC           = {}

    Functions.register_functions()
    return Client()