##############################
# Created by: Mark <Marx#8945>
##############################
import utils.log
from discord.ext import commands


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log = utils.log.get()

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        print("Member Update: " + after)

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        print("Presence Update: " + after)


async def setup(bot):  # Py-Cord calls setup on load
    await bot.add_cog(Games(bot))  # Add cog to the bot
