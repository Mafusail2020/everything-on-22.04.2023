import disnake
from disnake.ext import commands

APP_ID = "1011622174131507311"
TOKEN = "MTAxMTYyMjE3NDEzMTUwNzMxMQ.GBaGbo.H30bxeJr51RUS_QjahzDcoi2AcS7J-LiY9VGa0"

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=">>$", intents=intents, activity=disnake.Game("очке своим пальчиком", status=disnake.Status.online))
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Bruh (disnake)")


# can add name="help" to make a name for cmd
@bot.slash_command()
async def help(inter):
    await inter.send("Help command")

bot.run(TOKEN)
