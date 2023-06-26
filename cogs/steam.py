##############################
# Created by: Brian <Jeewa#6972>
##############################
import aiohttp
import discord
import utils.log
from discord.ext import commands


class Steam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log = utils.log.get()

    # creating a library thats async
    async def get_steam_featured(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://store.steampowered.com/api/featuredcategories/"
            ) as response:
                steam = await response.json()
                return steam["specials"]["items"]

    # Create slash command for /steamsales
    @commands.hybrid_command(
        name="steamsales", description="View current sales on steam!"
    )
    async def Steam(self, ctx):
        self.log.info(f"{ctx.author} said /steam.")
        specials = await self.get_steam_featured()

        sales_embed = discord.Embed(title="Today's Steam Sales:")

        for game in specials:
            original_price = int(game["original_price"]) / 100
            sale_price = int(game["final_price"]) / 100
            sales_embed.add_field(
                name=game["name"],
                value=f"~~${original_price}~~ **${sale_price}** *({game['discount_percent']}% off)* - [Store Page](https://steampowered.com/app/{game['id']})",
                inline=False,
            )
        sales_embed.set_footer(text="All prices are in USD.")

        await ctx.respond("", embed=sales_embed)


# Py-Cord calls setup on load
async def setup(bot):
    await bot.add_cog(Steam(bot))  # Add cog to the bot
