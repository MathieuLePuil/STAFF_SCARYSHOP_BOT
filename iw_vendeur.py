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

class Iw_vendeur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name = "iw_vendeur", description = "Accepte ou refuse un utilisateur dans l'équipe des vendeurs.")
    @commands.has_permissions(manage_roles = True)
    async def iw_vendeur(self, ctx, status, user : discord.User):
        guild = ctx.guild
        if status == "accept":
            emuser = discord.Embed(title = "Félicitations 🎉✨", description = "Vous êtes **accepté dans l'équipe** des **Vendeurs du ScaryShop**. Vous pouvez commencer à découvrir vos accès sur le serveur Staff du ScaryShop. \n \n > ***Lien du serveur :***  https://discord.gg/S5dwdD97Cr \n \n Nous vous invitions à mentionner le responsable qui vous a fait passé votre entretien afin de prendre un rendez-vous pour les explications. \n \n **Bienvenue dans l'équipe !**", timestamp=datetime.datetime.utcnow(), color = 0xFFA500)
            emuser.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            emserver = discord.Embed(description = f"Le message de validation de l'entretien de {user.mention} a bien été envoyé 📧.", timestamp=datetime.datetime.utcnow(), color = 0xFFA500)
            emserver.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            await user.send(embed = emuser)
            await ctx.send(embed = emserver)

        elif status == "decline":
            emuser = discord.Embed(title = "Désolé 🎉✨", description = "Malheureusement, votre entretien vendeur **ne donnera pas de suite**. Vous pourrez tout de même retenter votre chance dans 2 mois. \n \n **Bon courage pour la suite !**", timestamp=datetime.datetime.utcnow(), color = 0xFFA500)
            emuser.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            emserver = discord.Embed(description = f"Le message de refus de l'entretien de {user.mention} a bien été envoyé 📧.", timestamp=datetime.datetime.utcnow(), color = 0xFFA500)
            emserver.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            await user.send(embed = emuser)
            await ctx.send(embed = emserver)

        else:
            return



def setup(bot):
    bot.add_cog(Iw_vendeur(bot))