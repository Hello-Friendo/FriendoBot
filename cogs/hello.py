##############################
# Created by: Mark <Marx#8945>
##############################
import utils.log
from discord.ext import commands
from discord.ext.commands import Context, Bot


class Hello(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.log = utils.log.get()

    # Create slash command for /hello
    @commands.hybrid_command(name="hello", description="Say Hello!")
    async def hello(self, ctx: Context):
        self.log.info(f"{ctx.author} said /hello!")
        await ctx.send(f"Hello {ctx.author.display_name}!")


# Py-Cord calls setup on load
async def setup(bot):
    await bot.add_cog(Hello(bot))  # Add cog to the bot
