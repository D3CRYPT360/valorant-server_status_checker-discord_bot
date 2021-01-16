import discord
from discord.ext import commands
import DiscordUtils # https://github.com/toxicrecker/DiscordUtils

bot = commands.Bot(command_prefix="PREFIX")
TOKEN = "TOKEN"


@bot.event
async def on_ready():
    print("bot is ready")

@bot.command()
async def status(ctx, region):
    region = Region(region)
    if region.get_status_issue() == False:
        await ctx.send("no errors")

    else:
        
        if region.incident_check() == True:
            global embed1
            embed1 = discord.Embed(
                colour = discord.Colour.orange(),
                title = region.incident_title()
            )
            embed1.add_field(name=region.incident_date(), value=region.incident_reason())

        if region.maintenence_check() == True:
            embed2 = discord.Embed(
                colour = discord.Colour.orange(),
                title = region.maintenance_title()
            )
            embed2.add_field(name=region.incident_reason(), value=region.maintenance_reason())


            # running in a paginator so it looks cleaner
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
            paginator.add_reaction('⬅️', "back")
            paginator.add_reaction('➡️', "next")
            embeds = [embed1, embed2]
            await paginator.run(embeds)


bot.run(TOKEN)
