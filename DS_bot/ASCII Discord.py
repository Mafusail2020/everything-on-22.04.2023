import discord
from discord.ext import commands
import cv2 as cv

APP_ID = "1011622174131507311"
TOKEN = "MTAxMTYyMjE3NDEzMTUwNzMxMQ.GBaGbo.H30bxeJr51RUS_QjahzDcoi2AcS7J-LiY9VGa0"

intends = discord.Intents.all()
bot = commands.Bot(command_prefix='>>', intents=intends, status=discord.Status.online)

img = cv.imread("../op/Apple.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


@bot.event
async def on_ready():
    print("Ready")


@bot.command()
async def start(ctx):
    symbs = ' ⠠⠨⠰⠸⠶⠼⠾⣿'
    scale_multiplier = 6
    ret = ""
    for y in range(0, len(img_gray), scale_multiplier * 2):
        for x in range(0, len(img_gray[y]), scale_multiplier):
            ret += symbs[img_gray[y][x] % len(symbs) - 2]
        ret += '\n'

    await ctx.send(ret)


bot.run(TOKEN)
