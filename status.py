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


#IMPORTS
import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix = "YOUR_PREFIX")
TOKEN = #TOKEN

@bot.event
async def on_ready():
    print("bot is now online")


# NA
@bot.command()
async def na(ctx):
    # GETS REQ FROM API
    r = requests.get("https://valorant.secure.dyn.riotcdn.net/channels/public/x/status/na.json")
    riot = r.json()
    
    # CHECKS FOR INCIDENTS
    if (riot['incidents']) == []:
        await ctx.send ("No recent issues or events reported")
        
    # TRIGERRS IF THERE IS AN INCIDENT
    elif (riot['incidents']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["incidents"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['incidents'][0]['updates'][0]['created_at'][:16].split("T")), value=(riot['incidents'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)
        
    # TRIGGERS IF THERE IS A MAINTENANCE
    elif (riot['maintenances']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["maintenances"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['maintenances'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['maintenances'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)

#AP
@bot.command()
async def ap(ctx):
    # GETS REQ FROM API
    r = requests.get("https://valorant.secure.dyn.riotcdn.net/channels/public/x/status/ap.json")
    riot = r.json()
    
    # CHECKS FOR INCIDENTS
    if (riot['incidents']) == []:
        await ctx.send ("No recent issues or events reported")

    # TRIGERRS IF THERE IS AN INCIDENT
    elif (riot['incidents']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["incidents"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['incidents'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['incidents'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)
    
    # TRIGGERS IF THERE IS A MAINTENANCE
    elif (riot['maintenances']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["maintenances"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['maintenances'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['maintenances'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)
 
#BR       
@bot.command()
async def br(ctx):
    # GETS REQ FROM API
    r = requests.get("https://valorant.secure.dyn.riotcdn.net/channels/public/x/status/br.json")
    riot = r.json()
    
    # CHECKS FOR INCIDENTS
    if (riot['incidents']) == []:
        await ctx.send ("No recent issues or events reported")
        
    # TRIGERRS IF THERE IS AN INCIDENT
    elif (riot['incidents']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["incidents"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['incidents'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['incidents'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)
    
    # TRIGGERS IF THERE IS A MAINTENANCE
    elif (riot['maintenances']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["maintenances"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['maintenances'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['maintenances'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)

#EU        
@bot.command()
async def eu(ctx):
    # SENDS REQ TO API
    r = requests.get("https://valorant.secure.dyn.riotcdn.net/channels/public/x/status/eu.json")
    riot = r.json()
    
    # CHECKS FOR INCIDENTS
    if (riot['incidents']) == []:
        await ctx.send ("No recent issues or events reported")
    
    # TRIGGERS IF THERE IS AN INCIDENT
    elif (riot['incidents']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["incidents"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['incidents'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['incidents'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)
    
    # TRIGGERS IF THERE IS A MAINTENANCE
    elif (riot['maintenances']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["maintenances"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['maintenances'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['maintenances'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)

#LATAM       
@bot.command()
async def latam(ctx):
    
    # SENDING REQ TO API
    r = requests.get("https://valorant.secure.dyn.riotcdn.net/channels/public/x/status/latam.json")
    riot = r.json()
    
    # CHECKS FOR INCIDENTS
    if (riot['incidents']) == []:
        await ctx.send ("No recent issues or events reported")
    
    # TRIGGERS IF THERE IS AN INCIDENT    
    elif (riot['incidents']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["incidents"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['incidents'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['incidents'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)
    
    # TRIGGERS IF THERE IS A MAINTENANCE    
    elif (riot['maintenances']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["maintenances"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['maintenances'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['maintenances'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)
    
#KR        
@bot.command()
async def kr(ctx):
    # SENDS REQ TO API
    r = requests.get("https://valorant.secure.dyn.riotcdn.net/channels/public/x/status/kr.json")
    riot = r.json()
    
    # CHECKS FOR INCIDENTS
    if (riot['incidents']) == []:
        await ctx.send ("No recent issues or events reported")
     
    # TRIGGERS IF THERE IS AN INCIDENT    
    elif (riot['incidents']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["incidents"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['incidents'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['incidents'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)
        
    # TRIGGERS IF THERE IS A MAINTENANCE  
    elif (riot['maintenances']) != []:
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title=(riot["maintenances"][0]['titles'][0]['content'])
        )
        embed.add_field(name = (riot['maintenances'][0]['updates'][0]['created_at'][:16].split("T")[0]), value=(riot['maintenances'][0]['updates'][0]['translations'][0]['content']))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256")
        await ctx.send(embed=embed)

bot.run(TOKEN)
