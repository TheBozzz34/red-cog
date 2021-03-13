from redbot.core import commands
import discord
from discord.ext.commands import (
    BadArgument,
    CommandError,
    CheckFailure,
    DisabledCommand,
    command as dpy_command_deco,
    Command as DPYCommand,
    Cog as DPYCog,
    CogMeta as DPYCogMeta,
    Group as DPYGroup,
    Greedy,
)


class Mycog(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
		
		
		
	@commands.command()
    async def pog(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send(":pog:")
 
	