import discord
import time
import asyncio
from redbot.core import checks, commands
from random import choice, randint

class rainbow(commands.Cog):
    

    def __init__(self, bot):
        self.bot = bot
    
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(administrator=True)
    async def arainbow(self, ctx, interval:float, *, role):
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)
        if not roleObj:
            no = discord.Embed(title="{} is not a valid role".format(role))
            await self.bot.say(embed=no)
            return
        if interval < 120:
            interval = 120
        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.role.edit(ctx.message.server, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)

    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(administrator=True)
    async def rainbow(self, ctx, *, role: discord.Role):

        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.role.edit(ctx.message.server, role, colour=discord.Colour(value=colour))
            await asyncio.sleep(0.0)
