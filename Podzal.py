#!/usr/bin/env python
# coding: utf-8

import discord
from discord.ext import commands
import pandas as pd
import commands as cd

token = pd.read_csv("token.txt", header = None)[0][0]

bot = commands.Bot(command_prefix='!')

        
@bot.command(brief = "To call the command: !podz #ofpodz names")
async def podz(ctx, arg1, *args):
    y = int(arg1)
    x = []
    for n in args:
        x.append(n)
    ls, st = cd.podzal(y,x)
    string = '\n'.join(str(x) for x in st)
    await ctx.send(string)

    
bot.run(token)




