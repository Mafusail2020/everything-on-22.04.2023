import discord
from discord.ext import commands


Token = "MTAxMTYyMjE3NDEzMTUwNzMxMQ.GBaGbo.H30bxeJr51RUS_QjahzDcoi2AcS7J-LiY9VGa0"
bot = commands.Bot(command_prefix=">>",
                   intents=discord.Intents.all(),
                   activity=discord.Game("with his d"),
                   status=discord.Status.online)


@bot.event
async def on_ready():
    print("Ready")


@bot.command()
async def sus(ctx):
    await ctx.send("SUSSSS")

bot.run(Token)
