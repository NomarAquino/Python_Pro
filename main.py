import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('Tu bot {bot.user} está en línea')

@bot.command()
async def saludar(ctx, *, mensaje: str):
    mensaje = mensaje.lower().strip()

    if mensaje == 'hola':
        await ctx.send('Hola, ¿cómo estás?')
    elif mensaje == 'klk':
        await ctx.send('klk, ¿todo bien?')
    elif mensaje == 'buenas':
        await ctx.send('Buenas, ¿qué tal?')
    else:
        await ctx.send('¡SALUDA BIEN!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

token = ''

bot.run(token)
