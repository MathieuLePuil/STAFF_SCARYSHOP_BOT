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
import requests
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

#py Desktop\Bots_Discord\Staff_ScaryShop_BOT\main.py

bot = commands.Bot(command_prefix = "s/", intents=intents)
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands = True)

extensions = ['absence', 'effectif_vendeur', 'on_member', 'rc_vendeur', 'rc_moderateur', 'role_vendeur', 'role_moderateur', 'iw_vendeur', 'iw_moderateur', 'help', 'money']

@bot.event
async def on_ready():
    print("Staff - ScaryShop | BOT est PRET!")
    DiscordComponents(bot)

@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        await ctx.send('Loaded **{}**'.format(extension))
    except Exception as error:
        await ctx.send('**{}** cannot be loaded. [{}]'.format(extension, error))

@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        await ctx.send('Unloaded **{}**'.format(extension))
    except Exception as error:
        await ctx.send('**{}** cannot be unloaded. [{}]'.format(extension, error))

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('**{}** cannot be loaded. [{}]'.format(extension, error))

@bot.command()
async def reload(ctx, extension):
    if extension:
        try:
            bot.reload_extension(extension)
            await ctx.send('Reloaded **{}**'.format(extension))
        except:
            bot.load_extension(extension)
            await ctx.send('Loaded **{}**'.format(extension))


bot.run("OTI4NzQ1NjE5MzU3NTk3NzM2.YddPwg.IEKeXMunE4VaDkzITo3s1sskuXg")