from discord.ext import commands
import discord
import os
from dotenv import load_dotenv


# Custom Python Library
import lib.sb as sb
import lib.money as money
import lib.godgame as godgame
import lib.hairlossbeam as hairlossbeam
import lib.recommendfood as recommendfood
import lib.search_lol_userInfo as search_lol_userInfo
import lib.search_tft_userInfo as search_tft_userInfo
import lib.recommendfood as recommendfood

import lib.user as user

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
RIOT_TOKEN = "RGAPI-8a42353b-0e5d-47dc-8730-1de8741c79f9"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} online!')


@bot.command(name='탈모빔')
async def cmd1(ctx, arg):
    await ctx.send(hairlossbeam.hairlossbeam(arg))


@bot.command(name="갓겜판독기")
async def cmd2(ctx,arg):
    await ctx.send(godgame.godgame(arg))


@bot.command(name="병신판독기")
async def cmd3(ctx,arg):
    await ctx.send(sb.sb(arg))


@bot.command(name='외화')
async def cmd4(ctx, arg):
    await ctx.send(money.foreignCurrency(arg))


@bot.command(name="메뉴추천")
async def cmd5(ctx, arg):
    return ctx.send(recommendfood.recommendfood(arg))


@bot.command(name='롤전적검색')
async def cmd6(ctx, arg):
    embed = search_lol_userInfo.search_lol_userInfo(arg, RIOT_TOKEN)
    await ctx.send(embed = embed)


@bot.command(name= "롤체전적검색")
async def cmd7(ctx, arg):
    await ctx.send(embed = search_tft_userInfo.search_tft_userInfo(arg, RIOT_TOKEN))

@bot.command(name= "계좌개설")
async def cmd8(ctx):
    user.signup(ctx.author.name, ctx.author.id)

bot.run(DISCORD_TOKEN)