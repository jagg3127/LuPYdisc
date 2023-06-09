"""THIS HELP COMMAND WAS MADE BY A DEAR FRIEND OF MINE IVE EDITED IT ONLY SLIGHTLY I GIVE FULL CREDIT TO ACACIA"""

import discord
from   discord.ext import commands

global title
global embed_color
global description

class LUPYHelp(commands.HelpCommand):
    def get_command_signature(self, cmd):
        return f"{self.context.clean_prefix}{cmd.qualified_name} {cmd.signature}"
    
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title=title, colour=embed_color)
        embed.description = description
        for cog, commands in mapping.items():
            name = 'No Category' if cog is None else cog.qualified_name
            if name.lower().strip() == "help": continue
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                value = ', '.join(f"{c.name}" for c in commands if not c.hidden)
                if cog and cog.description:
                    value = '{}'.format(value)
            
                if name.lower() != "mod":
                    embed.add_field(name=f"__{name}__", value=f'{value}', inline=False)
                else:
                    embed.add_field(name=f"__{name}__", value='this command is for moderators only', inline=False)
        
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title='{0.qualified_name} Commands'.format(cog), colour=embed_color)
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=False)
        for command in filtered:
            embed.add_field(name=f"{self.get_command_signature(command)}",
                            value=command.short_doc or f'No help given.',
                            inline=False)
      
        await self.get_destination().send(embed=embed)
    
    async def send_group_help(self, group):
        embed = discord.Embed(title=self.get_command_signature(group), colour=embed_color)
        if group.help:
            embed.description = group.help

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                embed.add_field(name=self.get_command_signature(command),
                                value=command.short_doc or f'No help given.',
                                inline=False)

        await self.get_destination().send(embed=embed)
    
    send_command_help = send_group_help

class Help(commands.Cog):
    def __init__(self, bot):
        global title
        global embed_color
        global description
        
        title       = bot.help.title
        embed_color = bot.help.embed_color
        description = bot.help.description

        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = LUPYHelp()
        bot.help_command.cog = self
    
    def cog_unload(self):
        self.bot.help_command = self._original_help_command