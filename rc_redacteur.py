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


class Rc_redacteur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="rc_redacteur", description="Accepte ou refuse un utilisateur en entretien rédacteur.")
    @commands.has_permissions(manage_roles=True)
    async def rc_moderateur(self, ctx, status, user: discord.User, *, reason="Aucun raison n'a été renseignée !"):
        guild = ctx.guild
        if status == "accept":
            emuser = discord.Embed(title="Félicitations 🎉✨",
                                   description="Votre candidature pour devenir rédacteur sur le ScaryShop a été **retenue**. Celle-ci donne donc suite à un entretien vocal qui aura lieu sur le serveur discord réservé au Staff du ScaryShop. Si vous partagez le serveur à qui que ce soit, vous serez banni de nos services. \n \n > ***Lien du serveur :***  https://discord.gg/S5dwdD97Cr \n \n Lorsque vous arrivez dessus, veuillez indiquer dans #ma-demande la raison pour laquelle vous figurez sur le serveur. \n \n **Bon courage pour l'entretien !**",
                                   timestamp=datetime.datetime.utcnow(), color=0xFFA500)
            emuser.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            emserver = discord.Embed(
                description=f"Le message de validation de la candidature de {user.mention} a bien été envoyé 📧.",
                timestamp=datetime.datetime.utcnow(), color=0xFFA500)
            emserver.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            await user.send(embed=emuser)
            await ctx.send(embed=emserver)

        elif status == "decline":
            emuser = discord.Embed(title="Désolé 🥺",
                                   description=f"Malheureusement, votre candidature pour devenir rédacteur sur le ScaryShop **n'a pas été retenue**. Vous pourrez tout de même retenter votre chance dans 3 mois. \n \n > *Raison :* {reason} \n \n **Bon courage pour la suite !**",
                                   timestamp=datetime.datetime.utcnow(), color=0xFFA500)
            emuser.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            emserver = discord.Embed(
                description=f"Le message de refus de la candidature de {user.mention} a bien été envoyé 📧.",
                timestamp=datetime.datetime.utcnow(), color=0xFFA500)
            emserver.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

            await user.send(embed=emuser)
            await ctx.send(embed=emserver)

        else:
            return


def setup(bot):
    bot.add_cog(Rc_redacteur(bot))
