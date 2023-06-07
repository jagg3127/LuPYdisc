from LuPYdisc.Class.COMP import format_command

AC={}

def add_command(Name:str, Group:str, Code:str):
    from LuPYdisc.Class.LuPYClient import client, commands, asyncio
    class main_bod:
        def __init__(self, bot):
            self.bot = bot

        @commands.command(name=Name)
        async def load(self, ctx, *args, Code=Code):
            await format_command(Code, ctx)

    if Group in AC:
        asyncio.run(client.remove_cog(Group))
        AC[Group][f"load{len(AC[Group])}"] = main_bod.load
    else:
        AC[Group] = {'__init__': main_bod.__init__, 'load': main_bod.load}
    try:
        COGS = type(Group, (commands.Cog,), {'__init__': main_bod.__init__, 'load': main_bod.load})
    except:
        COGS = type(Group, (commands.Cog,), AC[Name])
    client.add_cog(COGS(client))