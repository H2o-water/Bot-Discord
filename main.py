import discord
from discord.ext import commands, tasks
import random
import asyncio

bot = commands.Bot(command_prefix = "$", description = "Bot made by H2o")


                    #RANDOM

Status = ["Use $help",
        "Made by H2o",
        "Exploration battalion"]

bot.remove_command("help")

@bot.event
async def on_ready():
    print("ready !")
    status.start()

@tasks.loop(seconds = 5)
async def status():
    game = discord.Game(random.choice(Status))
    await bot.change_presence(activity=discord.Streaming(name= f"{game}", url= "https://www.twitch.tv/relaxbeats"))
    #await bot.change_presence(status = discord.Status.dnd, activity = streaming)


                        #HELP

#help
@bot.command()
async def help(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    liens = "#"
    lien = "#"
    embed = discord.Embed(title = "**Menu of ALB**", description = "The menu can help you if you forgot your command(s) or discover other commands.", color = 0xFFD8BE)
    embed.add_field(name = "**Turn the page**", value = "Click on the reaction below the embed to look other pages in the Menu.", inline = False)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.set_image(url = "https://media.giphy.com/media/jAe22Ec5iICCk/giphy.gif")
    embed.set_footer(text = f"ALB | {serverName}")

    await ctx.send(embed = embed)


#snk
@bot.command()
async def snk(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    emoji = '<:780153015096705036:814554884061134859>s'
    liens = "https://www.youtube.com/watch?v=9jXSfJIrNB4"
    embed = discord.Embed(title = "Attaque Des Titans | Shingeki no Kyojin", description = "In French", color = 0xFFD8BE)
    embed.add_field(name = "**Shingeki no Kyojin | Episode 1 vf**", value = "Eren Jäger, Mikasa Ackerman et Armin Arlelt sont trois enfants vivants dans une ville fortifiée en paix jusqu'à l'arrivée du Titan Colossal qui va changer le cours de leur vie.", inline = False)
    embed.add_field(name = "*Clique en dessous là où il y a un le nom de l'épisode en bleu sa t'aménera sur le site où il y a l'épisode.*", value = f"[**Shingeki no Kyojin | Episode 1 vf**]({liens})", inline = False)
    embed.set_thumbnail(url = "https://fr.web.img5.acsta.net/c_210_280/pictures/18/10/31/18/23/3895256.jpg")
    embed.set_image(url = "https://media.giphy.com/media/c4sF8kUpkL1Cw/giphy.gif")


    await ctx.send(embed = embed)


































bot.run("ODE0MjMwNDcyMjg0NTY5NjAw.YDa1OA.p4sQI8LskbgYQWslZJkRk8MRO9w")