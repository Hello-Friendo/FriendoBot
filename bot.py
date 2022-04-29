# Import python libraries
import discord
import yaml
import os

# Error Handling, what if config.yaml doesn't exist?
if(os.path.isfile("config.yaml") == False):
    print("[ERROR]: 'config.yaml' does not exist!")
    exit()
    
# Load yaml config
with open("config.yaml", "r") as yamlconfig:
    config = yaml.safe_load(yamlconfig)

# Initialize Discord.Bot
bot = discord.Bot()

# Create bot event for logon
@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

# Create slash command for /hello
@bot.slash_command(guild_ids=[config['discord']['server_id']], 
                    name="hello", 
                    description="Say Hello!")
async def hello(ctx):
    await ctx.respond(f'Hello {ctx.author}!')

# Run the bot
bot.run(config['discord']['token'])