import discord
from discord.ext import commands

class On_member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        thewelChann = member.guild.get_channel(928742298748059679)
        em = discord.Embed(title = "NOUVEAU MEMBRE", description = f"> **Bienvenue à toi** {member.mention} sur le **Staff - ScaryShop**. Tu es le **{member.guild.member_count} ème**. Merci de nous informer dans le salon <#928748159927197766> la raison de votre venu sur ce serveur (entretien, vendeur, modérateur...).", color = 0xFFA500)
        em.set_thumbnail(url = member.avatar_url)
        await thewelChann.send(embed = em)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        thewelChann = member.guild.get_channel(928742473512124446)
        em = discord.Embed(title = "AU REVOIR !", description = f"> {member.mention} nous a quitté. Nous espérons te revoir bientôt !", color = 0xFFA500)
        em.set_thumbnail(url = member.avatar_url)
        await thewelChann.send(embed = em)

def setup(bot):
    bot.add_cog(On_member_join(bot))