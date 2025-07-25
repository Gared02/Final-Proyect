import discord
from discord.ext import commands
from modelo import main

permisos= discord.Intents.default()
permisos.message_content = True

bot = commands.Bot(command_prefix='!', intents=permisos)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def check(ctx):
    await ctx.send("Por favor, ingresa una imagen para poder analizarla.")

    def verificar(m):
        return m.author == ctx.author and m.channel == ctx.channel and len(m.attachments) > 0
    
    try:
        mesaje= await bot.wait_for('message', check=verificar, timeout=60)
        archivo= mesaje.attachments[0]
        nombre_archivo= archivo.filename
        ruta_archivo= f"./img/{nombre_archivo}"
        await archivo.save(ruta_archivo)
        await ctx.send(main(mod="keras_model.h5", leb="labels.txt", img=f"./img/{nombre_archivo}"))

    except ValueError as e:
        await ctx.send(f"No se recibió ninguna imagen en el tiempo permitido {e}")
    
bot.run("MTMyODc0MTg0MzYwNDYwMjkwMQ.GGXkDC.6eKT_x6j9STYaXeBwBOuxJy8Lq3_uXoFEJppXg")