# Import python libraries
import os
import asyncio
import discord
from discord.ext import commands

import utils.config
import utils.log

config = utils.config.load()  # Load the configuration
logger = utils.log.setup()  # Configure the logger

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
# Initialize Discord.Bot
bot = commands.Bot(command_prefix="!", intents=intents)


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event  # Create bot event for logon
async def on_ready():
    logger.info(f"Bot logged in as {bot.user}")

# Run the bot
# bot.run(config["discord"]["token"])


async def main():
    async with bot:
        await load_extensions()
        await bot.start(config["discord"]["token"])

asyncio.run(main())
