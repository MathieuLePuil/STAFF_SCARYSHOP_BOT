import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
from discord_slash import SlashCommand, ButtonStyle
import datetime
import json
import random
from discord import Permissions
from colorama import Fore, Style
from discord_slash.utils.manage_components import *
from discord_components import *
from discord_slash import cog_ext


class Money(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="money", description="Affiche la money disponible sur le compte ScaryShop.")
    @commands.has_permissions(manage_roles=True)
    async def money(self, ctx, quantite):
        guild = ctx.guild

        emserver = discord.Embed(description=f"Le compte Minecraft `ScaryShop` possède **{quantite}**.",
                                 timestamp=datetime.datetime.utcnow(), color=0xFFA500)
        emserver.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

        await ctx.send(embed=emserver)


def setup(bot):
    bot.add_cog(Money(bot))
