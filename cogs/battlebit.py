##############################
# Created by: Mark <Marx#8945>
##############################
import re
import utils.log
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context, Bot


class BattleBit(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.log = utils.log.get()

    # Create slash command for /bbinfo
    @commands.hybrid_command(name="bbinfo", description="View Battlebit Game Info!")
    async def bbinfo(self, ctx: Context):
        if len(ctx.message.mentions) > 0:
            player = ctx.guild.get_member(ctx.message.mentions[0].id)
            self.log.info(
                f"{ctx.author.display_name} ran bbinfo on {player.display_name}")

            if "BattleBit" in player.activity.name:
                embed = Embed(
                    title="Battle Bit Info - " + player.display_name)

                embed.add_field(
                    name="Server:", value=player.activity.details, inline=False)

                embed.add_field(name="Squad:", value=player.activity.state +
                                " " + player.activity.small_image_text, inline=False)

                embed.set_image(url=player.activity.large_image_url)

                embed.set_author(
                    name="Battlebit Info", icon_url=player.activity.small_image_url
                )

                await ctx.send(" ", embed=embed)


# Py-Cord calls setup on load
async def setup(bot):
    await bot.add_cog(BattleBit(bot))  # Add cog to the bot
