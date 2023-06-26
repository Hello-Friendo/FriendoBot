##############################
# Created by: Mark <Marx#8945>
##############################
import utils.log
from discord.ext import commands


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log = utils.log.get()

    # Listen for a member updates
    @commands.Cog.listener()
    async def on_member_update(before, after):
        print("Member Update: " + after)

    # Listen for a member to updates their activity
    @commands.Cog.listener()
    async def on_presence_update(before, after):
        print("Presence Update: " + after)


# Py-Cord calls setup on load
def setup(bot):
    bot.add_cog(Games(bot))  # Add cog to the bot
