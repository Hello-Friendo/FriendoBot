##############################
# Created by: Mark <Marx#8945>
##############################
import utils.log
from discord.ext import commands


class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log = utils.log.get()

    def log_hello(self, ctx):
        self.log.info(f"{ctx.author} said /hello!")

    # Create slash command for /hello
    @commands.slash_command(name="hello", description="Say Hello!")
    async def hello(self, ctx):
        self.log_hello(ctx)
        await ctx.respond(f"Hello {ctx.user.display_name}!")


# Py-Cord calls setup on load
def setup(bot):
    bot.add_cog(Hello(bot))  # Add cog to the bot
