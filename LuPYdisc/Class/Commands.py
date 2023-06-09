from LuPYdisc.Class.COMP import format_command


def add_command(Name:str, Group:str, Code:str):
    from LuPYdisc.Class.LuPYClient import _client, commands, asyncio

    AC=_client.AC

    class main_bod:
        def __init__(self, bot):
            self.bot = bot

        @commands.command(name=Name)
        async def load(self, ctx, *args, Code=Code):
            await format_command(Code, ctx)

    if Group in AC:
        AC[Group][f"load{len(AC[Group])}"] = main_bod.load
    else:
        AC[Group] = {'__init__': main_bod.__init__, 'load': main_bod.load}
    try:
        COGS = type(Group, (commands.Cog,), {'__init__': main_bod.__init__, 'load': main_bod.load})
        _client.add_cog(COGS(_client))
    except:
        _client.remove_cog(Group)
        COGS = type(Group, (commands.Cog,), AC[Group])
        _client.add_cog(COGS(_client))