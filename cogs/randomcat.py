####################################
# Created by: Grandon <Grandon#2681>
####################################
import aiohttp
import utils.log
from discord.ext import commands


class RandomCat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log = utils.log.get()
        self.prevUrl = ""

    # used to get a random Cat image
    # Returns a String
    async def getCat():
        # get a Client from AIOHttp
        async with aiohttp.ClientSession() as session:
            # Connects to 'https://cataas.com/cat/cute?json=true' and gets a responce
            async with session.get("https://cataas.com/cat/cute?json=true") as resp:
                # Parses the Responce from JSON to Python Dictanary
                catJson = await resp.json()
                # Returns a String that is made up of the responce URL and https://cataas.com/
                return f'https://cataas.com{catJson["url"]}'

    # Create slash command for /hello
    @commands.slash_command(
        name="randomcat",
        description="Sends a random cute cat image to the discord server",
    )
    async def randCat(self, ctx):
        self.log.info("A user requested a random cat")
        # get a cat URL
        catUrl = await self.getCat()
        # checks that PrevUrl isn't None and the CatUrl isn't the same as the previous Cat Url
        if self.prevUrl != None and catUrl != self.prevUrl:
            # the the previous cat Url to the new Cat url
            self.prevUrl = catUrl
            # Sends the Cat URl
            await ctx.respond(catUrl)
        else:
            # if the previous checks fail it just get a new cat URL and respond with that
            await ctx.respond(await self.getCat())


# Py-Cord calls setup on load
def setup(bot):
    bot.add_cog(RandomCat(bot))  # Add cog to the bot
