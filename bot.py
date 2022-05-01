# Import python libraries
import discord
import yaml
import os

# These Import are used for Random Cat Images
import aiohttp
import json

# used to get a random Cat image
# Returns a String
async def getCat():
    # get a Client from AIOHttp
    async with aiohttp.ClientSession() as session:
        # Connects to 'https://cataas.com/cat/cute?json=true' and gets a responce
        async with session.get('https://cataas.com/cat/cute?json=true') as resp:
            # Parses the Responce from JSON to Python Dictanary 
            catJson = await resp.json()
            # Returns a String that is made up of the responce URL and https://cataas.com/
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

# Create slash command for /randomcat   
# inits a varible for uses later
prevUrl = None
@bot.slash_command(guild_ids=[config['discord']['server_id']], name="randomcat", description="Sends a random cute cat image to the discord server")
async def randCat(ctx):
    # get a cat URL
    catUrl = await getCat()
    # checks that PrevUrl isn't None and the CatUrl isn't the same as the previous Cat Url
    if(prevUrl != None and catUrl != prevUrl):
        # the the previous cat Url to the new Cat url
        prevUrl = catUrl
        # Sends the Cat URl
        await ctx.respond(catUrl)
    else:
        # if the previous checks fail it just get a new cat URL and respond with that
        await ctx.respond(await getCat())


# Run the bot
bot.run(config['discord']['token'])