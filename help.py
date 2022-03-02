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

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name = "help", description = "Affiche la liste des commandes disponibles.")
    async def help(self, ctx):
        guild = ctx.guild
        em1 = discord.Embed(title = "Help Staff - ScaryShop | BOT", description = "Voici la liste de toutes les commandes disponibles:", color = 0xFFA500)
        em1.add_field(name = "`s/absence`", value = "<:fad:929432506946695238> Affiche l'interface des absences. {Staff - ScaryShop}", inline = False)
        em1.add_field(name = "`/effectif_vendeur`", value = "<:fad:929432506946695238> Affiche l'effectif des vendeurs. {Staff - ScaryShop}", inline = False)
        em1.add_field(name = "`/money <money>`", value = "<:fad:929432506946695238> Affiche la quantité de money présente surle compte `ScaryShop`. {Staff - ScaryShop}", inline = False)
        em1.add_field(name = "`/rc_vendeur <accept | decline> <@pseudo>`", value = "<:fad:929432506946695238> Accepte ou refuse une demande de recrutement vendeur. {ScaryShop}", inline = False)
        em1.add_field(name = "`/iw_vendeur <accept | decline> <@pseudo>`", value = "<:fad:929432506946695238> Accepete ou refuse un entretien vendeur. {Staff - ScaryShop}", inline = False)
        em1.add_field(name = "`/role_vendeur <@pseudo>`", value = "<:fad:929432506946695238> Ajoute les rôles de vendeur à l'utilisateur. {ScaryShop}", inline = False)
        em1.add_field(name = "`/rc_moderateur <accept | decline> <@pseudo>`", value = "<:fad:929432506946695238> Accepte ou refuse une demande de recrutement modérateur. {ScaryShop}", inline = False)
        em1.add_field(name = "`/iw_moderateur <accept | decline> <@pseudo>`", value = "<:fad:929432506946695238> Accepete ou refuse un entretien modérateur. {Staff - ScaryShop}", inline = False)
        em1.add_field(name = "`/role_moderateur <@pseudo>`", value = "<:fad:929432506946695238> Ajoute les rôles de modérateur à l'utilisateur. {ScaryShop}", inline = False)
        em1.set_thumbnail(url = "https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
        em1.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")
        await ctx.send(embed = em1)



def setup(bot):
    bot.add_cog(Help(bot))