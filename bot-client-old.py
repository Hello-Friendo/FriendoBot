# Import python libraries
import discord
import yaml

# Load yaml config
with open("config.yaml", "r") as yamlconfig:
    config = yaml.safe_load(yamlconfig)

# Create Discord client "intents"
intents = discord.Intents.default()
intents.message_content = True

# Create Discord Client
client = discord.Client(intents=intents)

# Create Client event on_ready()
@client.event
async def on_ready():
    print(f'Client logged in as {client.user}')

# Create Client event on_message()
@client.event
async def on_message(message):
    # Make bot ignore messages sent from itself
    if message.author == client.user:
        return
    
    # Respond to $hello with Hello {author}!
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author}')

# Run the bot
client.run(config['discord']['token'])
