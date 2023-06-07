from LuPYdisc.Functions import setup_functions
from discord.ext import commands
import discord
import asyncio
from LuPYdisc.tools import FunctionHandler

global client

class _LuPYClient():
    def __init__(self,  command_prefix:tuple, WhenMentioned:bool=False, intents:str="default", activity=None, case_sensitive:bool=True):
        global client
        setup_functions()



        if   WhenMentioned and command_prefix==():   command_prefix = commands.when_mentioned_or()
        elif WhenMentioned:                          command_prefix = commands.when_mentioned_or(*command_prefix)
        
        intents=intents.lower().strip()
        if intents == "all":
            intents=discord.Intents.all()
        else:
            intents=discord.Intents.default()

        client = commands.Bot(command_prefix=command_prefix, intents=intents, case_insensitive=False if case_sensitive else True)



def LuPYClient(*command_prefix:str|list, WhenMentioned:bool=False, intents:str="default", activity=None, case_sensitive:bool=True):
    global client

    Functions = FunctionHandler()

    _LuPYClient(command_prefix=command_prefix, WhenMentioned=WhenMentioned, intents=intents, activity=activity, case_sensitive=case_sensitive)
    client.LUPY_FUNCS=Functions
    Functions.register_functions()
    return client