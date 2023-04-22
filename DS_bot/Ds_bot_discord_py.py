import discord
from discord.ext import commands

APP_ID = "1011622174131507311"
TOKEN = "MTAxMTYyMjE3NDEzMTUwNzMxMQ.GBaGbo.H30bxeJr51RUS_QjahzDcoi2AcS7J-LiY9VGa0"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents,
                   activity=discord.Game("очке своим пальчиком",
                   status=discord.Status.online))

bot.remove_command('help')

# Переменные / Функции для работы

async def clear_cmd(ctx):
    await ctx.channel.purge(limit=1)


greetings = ["привет", "здарова", "ку", "прив", "дарова", "hi", 'sup', "howdy", "hello"]
# Переменные / Функции для работы

@bot.event
async def on_ready():
    print("Bruh (discord.py)")


@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    await clear_cmd(ctx)
    emb = discord.Embed(title="Member muted!", description=f"Muted member {member.mention}")

    # Получение спикска ролей сервера
    mute_role = discord.utils.get(ctx.message.guild.roles, name="muted")

    await member.add_roles(mute_role)
    await ctx.send(embed=emb)


@bot.command()
async def send_p(ctx, dest: discord.Member, *text):
    emb = discord.Embed(title="Info about sent message")
    emb.add_field(name="Message author:", value=ctx.author)
    emb.add_field(name="Message destination:", value=type(dest))
    emb.add_field(name="Text sended:", value=" ".join(list(text)))

    await ctx.send(embed=emb)
    # await ctx.send(f"Message author: {ctx.author}")
    # await ctx.send(f"Message destination: {dest}")
    # await ctx.send("Text sended: " + str(*list(text)))
    await dest.send(" ".join(list(text)))


@bot.command()
@commands.has_permissions(administrator=True)
async def add_role(ctx, member: discord.Member, *added_role):
    await clear_cmd(ctx)
    ac_role = ''
    for i in added_role:
        ac_role += i
    emb = discord.Embed(title=f"Congrats {member.name}!", description=f"{member.mention} was given role {ac_role}!")

    # Получение спикска ролей сервера
    role = discord.utils.get(ctx.message.guild.roles, name=f"{ac_role}")

    await member.add_roles(role)
    await ctx.send(embed=emb)


@bot.command()
async def testemb(ctx):
    emb = discord.Embed(title="Psst tou are susy", description="I hate niggers", colour=discord.Color.lighter_grey(), url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCneBC6fAuR_jJV7w_ULFLuCJRBZ9CP_gxbg&usqp=CAU')

    emb.set_author(name="Ur mom", icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCneBC6fAuR_jJV7w_ULFLuCJRBZ9CP_gxbg&usqp=CAU')
    # emb.set_footer(text=ctx.author.name, icon_url=bot.user.name)
    emb.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCneBC6fAuR_jJV7w_ULFLuCJRBZ9CP_gxbg&usqp=CAU')
    emb.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCneBC6fAuR_jJV7w_ULFLuCJRBZ9CP_gxbg&usqp=CAU")

    emb.add_field(name="Have you been on sawcon?", value="I mean SAWCON DEEZ NUTS")

    await ctx.send(embed=emb)


@bot.command()
async def help(inter):
    emb = discord.Embed(title="Susy")

    emb.add_field(name="Kinda sus", value="I FOUND AMONGUS!!!!11")
    await inter.send(embed=emb)


# ctx.message.author.mention - @randomperson
# ctx.message.author - randomperson#XXXX
@bot.command()
async def hello(ctx):
    await clear_cmd(ctx)
    await ctx.send(f"{ctx.message.author.mention}, hello!")


@bot.command()
async def echo(ctx, *mes):
    await ctx.send(f"{ctx.message.author.mention}, {' '.join(mes)}")


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, reason=None):
    await clear_cmd(ctx)
    await member.kick(reason=reason)
    await ctx.send(f"{member} kicked!")


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, reason=None, time=1):
    await clear_cmd(ctx)
    await member.ban(delete_message_days=time, reason=reason)
    await ctx.send(f"{member} banned!")


@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.message.delete()
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Разбанен {user}')
            return


@bot.event
async def on_message(message):
    # Применение комманд
    await bot.process_commands(message)
    text = message.content.lower()
    if text in greetings:
        await message.channel.send("Чё тебе надо, бомжара?")


bot.run(TOKEN)
