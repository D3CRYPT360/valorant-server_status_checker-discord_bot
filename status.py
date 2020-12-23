"""
MIT License

Copyright (c) 2020 D3crypt360

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
