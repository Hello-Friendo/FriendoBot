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
intents.presences = True
intents.members = True

# Initialize Discord.Bot
bot = commands.Bot(command_prefix="!", intents=intents)


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            logger.debug(f"Loading extension: cogs/{filename}")
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def start_bot():
    await bot.start(config["token"])


@bot.event  # Create bot event for logon
async def on_ready():
    logger.info(f"Bot logged in as {bot.user}")

asyncio.run(load_cogs())
asyncio.run(start_bot())
# bot.start(config["discord"]["token"])
