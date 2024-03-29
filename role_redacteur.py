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

class Role_redacteur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name = "role_redacteur", description = "Ajoute les rôles de rédaction à l'utilisateur.")
    @commands.has_permissions(manage_roles = True)
    async def role_redaction(self, ctx, user : discord.User):
        guild = ctx.guild

        if guild.id == 705089080693751850:

            role1 = guild.get_role(831618115137568875)
            role2 = guild.get_role(1002654508037447720)
            role3 = guild.get_role(838446325389066270)

            await user.add_roles(role1)
            await user.add_roles(role2)
            await user.add_roles(role3)


            emserver = discord.Embed(description = f"Les rôles de rédaction ont bien été ajoutés à {user.mention}.", timestamp=datetime.datetime.utcnow(), color = 0xFFA500)
            emserver.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            await ctx.send(embed = emserver)

        else:

            emserver = discord.Embed(description = f"Vous ne pouvez pas effectuer cette commande sur ce serveur.", timestamp=datetime.datetime.utcnow(), color = 0xFFA500)
            emserver.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            await ctx.send(embed = emserver)


def setup(bot):
    bot.add_cog(Role_redacteur(bot))