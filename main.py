import discord
from discord.ext import commands
from bot_token import token
from img_class import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def check(ctx):
    if ctx.message.attachments:

        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            img_path = f"img/{file_name}"
            await attachment.save(img_path)


        class_name, score = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=img_path)
        await ctx.send(f"bu bir {class_name.strip()}.")
        
    else:
        await ctx.send("resim göndermediniz")

bot.run(token)