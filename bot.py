# Import python libraries
import os
import discord

import utils.config
import utils.log

config = utils.config.load()  # Load the configuration
logger = utils.log.setup()  # Configure the logger
bot = discord.Bot()  # Initialize Discord.Bot

# Load bot commands
for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        logger.debug(f"Loading command: {cog}")
        command = bot.load_extension(f"cogs.{cog[:-3]}")


@bot.event  # Create bot event for logon
async def on_ready():
    logger.info(f"Bot logged in as {bot.user}")

# Run the bot
bot.run(config["discord"]["token"])
