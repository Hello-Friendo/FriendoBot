##############################
# Created by: Mark <Marx#8945>
##############################
import utils.log
from discord.ext import commands
from discord import Member, ActivityType


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log = utils.log.get()

    # @commands.Cog.listener()
    # async def on_member_update(self, before, after):
    #     print("Member Update: " + after)

    @commands.Cog.listener()
    async def on_presence_update(self, before, user: Member):
        if not user.bot:
            if hasattr(user.activity, "type") and user.activity.type == ActivityType.playing:
                self.log.info(
                    f"{user.display_name} playing {user.activity.name}")


async def setup(bot):  # Py-Cord calls setup on load
    # await bot.add_cog(Games(bot))  # Add cog to the bot
    pass
