import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# -------------------------------------------------------
# EVENTO ON_READY
# -------------------------------------------------------
@bot.event
async def on_ready():
    print(f"Bot conectado como: {bot.user}")

# -------------------------------------------------------
# COMANDO MEM (imagen aleatoria)
# -------------------------------------------------------
@bot.command()
async def mem(ctx):
    imagen = random.choice(os.listdir('images'))
    with open(f'images/{imagen}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

# -------------------------------------------------------
# COMANDO RECYCLE (versión inteligente)
# -------------------------------------------------------
@bot.command()
async def recycle(ctx, *, objeto: str):
    objeto = objeto.lower()

    # ---- BASE DE DATOS SIMPLE DE RESIDUOS ----
    categorias = {
        "reciclaje": {
            "palabras": [
                "botella", "plastico", "carton", "papel", "lata",
                "aluminio", "vidrio", "tetrapak", "pet", "envase"
            ],
            "mensaje": "♻️ Este objeto sí es reciclable. Llévalo al contenedor de reciclaje."
        },
        "organico": {
            "palabras": [
                "cascara", "manzana", "platano", "restos", "comida",
                "pan", "hueso", "verdura", "fruta"
            ],
            "mensaje": "🌱 Este objeto es orgánico. Debe ir al contenedor de residuos orgánicos."
        },
        "no_reciclable": {
            "palabras": [
                "pañal", "papel higienico",
                "cepillo de dientes", "esponja", "toalla sanitaria"
            ],
            "mensaje": "🚫 Este objeto no es reciclable y debe ir al contenedor común."
        },
        "peligroso": {
            "palabras": [
                "bateria", "pila", "aceite", "medicina", "quimico",
                "spray", "insecticida"
            ],
            "mensaje": "⚠️ Esto es un residuo peligroso. Debes llevarlo a un punto limpio o centro de acopio."
        }
    }

    for categoria, data in categorias.items():
        for palabra in data["palabras"]:
            if palabra in objeto:
                await ctx.send(data["mensaje"])
                return

    await ctx.send(
        "❓ No reconozco ese objeto. Intenta describirlo mejor, por ejemplo:\n"
        "`botella de plástico` · `cáscara de plátano` · `pila AA`"
    )

@bot.command()
async def informacion(ctx):
    menu = (
        "📘 Opciones de información:\n"
        "1️⃣ Info sobre tala de árboles 🌳\n"
        "👉 Escribe el número de la opción"
    )
    await ctx.send(menu)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "1":
        await message.channel.send(
            "🌳 Tala de árboles:\n"
            "La tala indiscriminada destruye ecosistemas, afecta la biodiversidad "
            "y acelera el cambio climático."
        )

    await bot.process_commands(message)
@bot.command()
async def imagen(ctx):
    carpeta = "imagenes" 
    imagen_random = random.choice(os.listdir(carpeta))
    with open(f"{carpeta}/{imagen_random}", "rb") as img:
        archivo = discord.File(img)
    await ctx.send(file=archivo)

bot.run("")
