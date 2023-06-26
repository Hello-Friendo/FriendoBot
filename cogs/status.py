##############################
# Created by: Mark <Marx#8945>
# Set pre-defined statuses on a loop
##############################
import discord
import utils.log
import random
from discord.ext import tasks, commands


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log = utils.log.get()
        self.statuses = [
            "Hello Friendo 👋",
            "👋 Hello Friendo",
            "👋 Hello Friendo 👋",
            "Learn to code Python! 🐍",
            "Hello Friendo Bot",
            "The Friendo Machine",
            "FRIENDOS FOREVER"
        ]
        self.activities = [
            discord.ActivityType.playing,
            discord.ActivityType.listening,
            discord.ActivityType.watching
            # discord.ActivityType.streaming
        ]

    @commands.Cog.listener()
    async def on_ready(self):
        self.set_status.start()

    @tasks.loop(minutes=20)
    async def set_status(self):
        status = random.choice(self.statuses)
        activity = random.choice(self.activities)
        await self.bot.change_presence(activity=discord.Activity(type=activity, name=status))
        self.log.info(f"Set activity {activity} to status {status}")


def setup(bot):  # Py-Cord calls setup on load
    bot.add_cog(Status(bot))  # Add cog to the bot
