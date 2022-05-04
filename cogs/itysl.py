##############################
# Created by: Mark <Marx#8945>
##############################
import csv
import random

import discord
import utils.log
from discord.ext import commands


class ITYSL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log = utils.log.get()
        self.sketches = []

        with open(
            "./data/itysl-sketches.csv", "r", encoding="utf-8-sig"
        ) as csv_sketches:
            reader = csv.DictReader(csv_sketches)
            for row in reader:
                self.sketches.append(row)

    async def get_random_sketch(self):
        return random.choice(self.sketches)

    async def get_quotes(self, sketch):
        quotables = sketch["Transcript"].split(".")
        return [
            random.choice(quotables).strip()[:1024],
            random.choice(quotables).strip()[:1024],
        ]

    # Create slash command for /itysl
    @commands.slash_command(
        name="itysl", description="I THINK YOU SHOULD LEAVE: QUOTE AND MEMES"
    )
    async def itysl(self, ctx):
        # Get random sketch
        sketch = await self.get_random_sketch()
        embed = discord.Embed(title=sketch["Name"])

        # Create quotes
        quotes = await self.get_quotes(sketch)

        embed.add_field(name="Quote 1:", value=quotes[0], inline=False)
        embed.add_field(name="Quote 2:", value=quotes[1], inline=False)

        # Embed image
        if sketch["Image"] is not None:
            embed.set_image(url=sketch["Image"])

        embed.set_author(
            name="Tim Robinson", icon_url="https://i.imgur.com/QcVgX2N.png"
        )
        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/en/d/d4/I_Think_You_Should_Leave.png"
        )

        # Add timestamp
        embed.add_field(name="Timestamp:", value=sketch["Link"], inline=False)

        embed.set_footer(
            text="Season " + sketch["Season"] + " Episode " + sketch["Episode"]
        )

        await ctx.respond(" ", embed=embed)


# Py-Cord calls setup on load
def setup(bot):
    bot.add_cog(ITYSL(bot))  # Add cog to the bot
