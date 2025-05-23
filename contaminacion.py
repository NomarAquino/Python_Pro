import discord
from discord.ext import commands
import random
import os
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('Tu bot {bot.user} está en línea')

@bot.command()
async def contaminacion(ctx,*,mensaje:str):

    if mensaje in ("significado"):
        await ctx.send("Contaminación es ensuciar el ambiente con cosas que no deberían estar allí, como basura, humo, químicos o ruido.")

    elif mensaje in ("cuales son las causas?"):
        await ctx.send ("Las causas de la contaminación son las acciones humanas que ensucian o dañan el medio ambiente.")

    elif mensaje in ("como podemos prevenirlo?"):
        await ctx.send("Prevenir la contaminación es posible si todos hacemos nuestra parte: el gobierno, las empresas y cada persona.")



token = ''