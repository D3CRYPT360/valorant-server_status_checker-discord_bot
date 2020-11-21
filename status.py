import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix = "YOUR PREFIX")
TOKEN = "YOUR TOKEN"

@bot.event
async def on_ready():
    print("bot is now online")


thumbnail = "https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256"


@bot.command()
async def status(ctx, region):
    region = region.lower()
    r = requests.get(f"https://valorant.secure.dyn.riotcdn.net/channels/public/x/status/{region}.json")
    if r.status_code == 200:
        json_data = r.json()
                
        if (json_data['incidents']) and (json_data['maintenances']) == []:# If there is no incidents/maintenance
            await ctx.send ("No recent issues or events reported")
                  
        
        elif (json_data['maintenances'])!= []:# If the issue is related to a maintenance
            embed = discord.Embed(
                colour = discord.Colour.dark_gold(),
                title=(json_data["maintenances"][0]['titles'][0]['content'])
            )
            embed.add_field(name = (json_data['maintenances'][0]['updates'][0]['created_at'][:10]), value=(json_data['maintenances'][0]['updates'][0]['translations'][0]['content']))
            embed.set_thumbnail(url=thumbnail)
            await ctx.send(embed=embed)
            
        elif (json_data['incidents']) != []:# If the issue is related to an incident
            embed = discord.Embed(
                colour = discord.Colour.dark_gold(),
                title=(json_data["incidents"][0]['titles'][0]['content'])
            )
            embed.add_field(name = (json_data['incidents'][0]['updates'][0]['created_at'][:10]), value=(json_data['incidents'][0]['updates'][0]['translations'][0]['content']))
            embed.set_thumbnail(url=thumbnail)
            await ctx.send(embed=embed)
                
        if (json_data['maintenances']) and (json_data['incidents']) != []: # If there is both a maintenance and an incident  
            embed1 = discord.Embed(
                colour = discord.Colour.dark_gold(),
                title=(json_data["maintenances"][0]['titles'][0]['content'])
            )
            embed1.add_field(name = (json_data['maintenances'][0]['updates'][0]['created_at'][:10]), value=(json_data['maintenances'][0]['updates'][0]['translations'][0]['content']))
            embed1.set_thumbnail(url=thumbnail)
            
            embed2 = discord.Embed(
                colour = discord.Colour.dark_gold(),
                title=(json_data["incidents"][0]['titles'][0]['content'])
            )
            embed2.add_field(name = (json_data['incidents'][0]['updates'][0]['created_at'][:10]), value=(json_data['incidents'][0]['updates'][0]['translations'][0]['content']))
            embed2.set_thumbnail(url=thumbnail)
            await ctx.send(embed=embed1)
            await ctx.send(embed=embed2)
            
    
    elif r.status_code != 200:
        await ctx.send(f"{region} server status not found...")




bot.run(TOKEN)