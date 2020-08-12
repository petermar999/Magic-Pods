#!/usr/bin/env python
# coding: utf-8

import discord
from discord.ext import commands
import pandas as pd

token = pd.read_csv("token.txt", header = None)[0][0]

bot = commands.Bot(command_prefix='!')

        
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(token)




