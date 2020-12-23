import discord
from discord.ext import commands
from valoStatus import Region

bot = commands.Bot(command_prefix=",")
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
            embed = discord.Embed(
                colour = discord.Colour.orange(),
                title = region.incidents_title()
            )
            embed.add_field(name=region.incidents_date(), value=region.incidents_reason())
            await ctx.send(embed=embed)

        elif region.maintenence_check() == True:
            embed = discord.Embed(
                colour = discord.Colour.orange(),
                title = region.maintenances_title()
            )
            embed.add_field(name=region.maintenances_date(), value=region.maintenances_reason())
            await ctx.send(embed=embed)
            

bot.run(TOKEN)
