# Import python libraries
import discord
import yaml
import os
import aiohttp
import json

async def getCat():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://cataas.com/cat/cute?json=true') as resp:
            catJson = await resp.json()
            return f'https://cataas.com/{catJson["url"]}'


# Error Handling, what if config.yaml doesn't exist?
if(os.path.isfile("config.yaml") == False):
    print("[ERROR]: 'config.yaml' does not exist!")
    exit()

# Load yaml config
with open("config.yaml", "r") as yamlconfig:
    config = yaml.safe_load(yamlconfig)

# Error Handling when discord:token doesn't exist
if("token" in config['discord'].keys() == False):
    print("[ERROR]: Config missing token!")
    exit()

# Initialize Discord.Bot
bot = discord.Bot()

# Create bot event for logon
@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

# Create slash command for /hello
@bot.slash_command(guild_ids=[config['discord']['server_id']], name="hello", description="Say Hello!")
async def hello(ctx):
    # print(f"{ctx.author} said hello.") # TODO: Convert to python logging
    await ctx.respond(f'Hello {ctx.user.display_name}!')
    
@bot.slash_command(guild_ids=[config['discord']['server_id']], name="randomcat", description="Sends a random cute cat image to the discord server")
async def randCat(ctx):
    await ctx.respond(await getCat())

# Run the bot
bot.run(config['discord']['token'])