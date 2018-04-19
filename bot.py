#GIFbot2 by Yeongjin Nam

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

client = discord.Client()
bot = commands.Bot(command_prefix='$')

#on_ready means bot does stuff when loaded
@bot.event
async def on_ready():
    print ('GIFbot2 online!')
    await bot.change_presence(game=discord.Game(name="$help for commands"))

#happens when encounters the event
#on_message means does stuff from message
#@bot.event
#async def on_message(message):
    
    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong!")

@bot.command()
async def say(*, ctx):
    await bot.say(ctx)
    print(ctx)

@bot.command()
async def roll(msg: str):
    sign = 0
    whatsign = ""
    front = ""
    num1 = 0
    num2 = 0
    num3 = 0

    msg = msg.lower()
    try:
        msg.index("+")
        sign = 3
        whatsign = "+"
    except:

        try:
            msg.index("-")
            sign = 1
            whatsign = "-"
        except:

            sign = 0
    try:
        if sign > 0:
            front = msg.split(whatsign)[0]
            num3 = int(msg.split(whatsign)[1])
        else:
            front = msg

        num1, num2 = map(int, front.split("d"))

        dice = [0] * num1
        dice2 = [""] * num1
        total = 0

        for i in range(0, num1):
            dice[i] = random.randint(1, num2)
            total += dice[i]
            dice2[i] = str(dice[i])

        if sign > 0:
            total += ((sign-2)*num3)   

        result = "{" + ', '.join(dice2) + "}"

        if sign > 0:
            result = result + " " + whatsign + " " + str(num3)
        result = result + " = " + str(total)

        await bot.reply(result)


    except Exception:
        await bot.reply("The format is aDb+c or aDb-c!")

@bot.command(pass_context=True)
async def tuturu(ctx):
    rd = random.randint(1,2)
    txt = ""

    if rd == 1:
        txt = "トゥットゥルー♪"
    else:
        txt = "Tu Tu Ru~♪"
    e = discord.Embed(title=txt, color=discord.Colour.blue())
    e.set_image(url='https://i.imgur.com/j6QVxo6.png')

    await bot.say(embed=e)



        



bot.run('NDM0ODEzMjU4NzcyMzgxNzI4.DbQDjA.lRYURqbcp132MT-J-3uL6G-leg8')
