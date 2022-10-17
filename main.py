from discord.ext import commands
import discord
import os
from dotenv import load_dotenv


# Custom Python Library
from lib.sb import sb
from lib.money import foreignCurrency
from lib.godgame import godgame
from lib.hairlossbeam import hairlossbeam
from lib.recommendfood import recommendfood
from lib.search_lol_userInfo import search_lol_userInfo
from lib.search_tft_userInfo import search_tft_userInfo
from lib.leavework import countTime
from lib.user import signup, findRow, userInfo, delete, getMoney, remit, checkUser
from lib.lol_cup import search_match

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
RIOT_TOKEN = os.getenv("RIOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} online!')

@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title = "Obunga Bot#1375", description = "열구가 좋아 죽습니다", color = 0x6E17E3) 
    embed.add_field(name = bot.command_prefix + "명령어", value = "Obunga Bot의 명령어를 확인합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "탈모빔 유저이름", value = "특정 유저에게 탈모빔을 날립니다. 확률이 존재합니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "갓겜판독기 게임이름", value = "특정게임이 갓겜인지 알려줍니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "병신판독기 이름", value = "특정 인물이 병신인지 알려줍니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "외화 외화이름", value = "특정 외화 시세를 알려줍니다(달러, 엔화, 위안화, 유로).", inline = False)
    embed.add_field(name = bot.command_prefix + "메뉴추천 양식 / 한식 / 중식 / 일식 / 아무거나", value = "메뉴를 추천해줍니다", inline = False)
    embed.add_field(name = bot.command_prefix + "롤전적검색 롤닉네임 ", value = "롤 전적 검색 기능입니다. 소환사 이름은 공백 없이 입력해주세요.", inline = False)
    embed.add_field(name = bot.command_prefix + "롤체전적검색 롤닉네임 ", value = "롤체 전적 검색 기능입니다. 소환사 이름은 공백 없이 입력해주세요", inline = False)
    embed.add_field(name = bot.command_prefix + "퇴근", value = "공붕이들을 위한 퇴근까지 남은 시간을 알려줍니다. 혹시 본인도 직장인이다 하면 알려주세요. 따로 퇴근시간 만들어 드립니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "계좌개설", value = "거래를 위한 계좌를 만듭니다. 기본 자금으로 3000만원을 받습니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "잔고조회", value = "내 계좌의 잔고를 조회합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "정보 @유저이름", value = "특정 유저의 잔고를 조회합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "송금 @유저이름 금액", value = "특정 유저에게 작성한 금액만큼 송금합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "외화매입/매각 외화이름", value = "추후 추가 예정인 명령어입니다", inline = False)
    embed.add_field(name = bot.command_prefix + "주식매입/매각 주식이름", value = "추후 추가 예정인 명령어입니다", inline = False)
    embed.add_field(name = bot.command_prefix + "코인매입/매각 코인이름", value = "추후 추가 예정인 명령어입니다", inline = False)
    await ctx.send(embed=embed)

@bot.command(name='탈모빔')
async def cmd1(ctx, arg):
    await ctx.send(hairlossbeam(arg))


@bot.command(name="갓겜판독기")
async def cmd2(ctx,arg):
    await ctx.send(godgame(arg))


@bot.command(name="병신판독기")
async def cmd3(ctx,arg):
    await ctx.send(sb(arg))


@bot.command(name='외화')
async def cmd4(ctx, arg):
    await ctx.send(foreignCurrency(arg))


@bot.command(name="메뉴추천")
async def cmd5(ctx, arg):
    return ctx.send(recommendfood(arg))


@bot.command(name='롤전적검색')
async def cmd6(ctx, arg):
    embed = search_lol_userInfo(arg, RIOT_TOKEN)
    await ctx.send(embed = embed)


@bot.command(name= "롤체전적검색")
async def cmd7(ctx, arg):
    await ctx.send(embed = search_tft_userInfo(arg, RIOT_TOKEN))

@bot.command(name="퇴근")
async def cmd8(ctx):
    await ctx.send(countTime())

@bot.command(name="롤드컵")
async def cmd9(ctx):
    await ctx.send(embed = search_match())

@bot.command(name="!p")
async def cmExtra(ctx):
    pass

@bot.command()
async def 계좌개설(ctx):
    await ctx.send("계좌개설 가능여부를 조회합니다")
    if findRow(ctx.author.name, ctx.author.id) == None:
        signup(ctx.author.name, ctx.author.id)
        await ctx.send("회원가입이 완료되었습니다.")
    else:
        await ctx.send("이미 가입하셨습니다. \n 중복 개설은 불가능합니다.")

@bot.command()
async def 잔고조회(ctx):
    money = userInfo(ctx.author.name, ctx.author.id)
    
    if money == None:
        print("사용자 정보가 없습니다.")
        print("------------------------------\n")
        await ctx.send("존재하지 않는 사용자")
    else:
        print("사용자 정보 발견, 메세지를 보냅니다.")
        print("------------------------------\n")
        embed = discord.Embed(title= ctx.author.name, color = 0x62D0F6)
        embed.add_field(name = "잔고", value = money)
        await ctx.send(embed=embed)

@bot.command()
async def 정보(ctx, user: discord.User):
    money = userInfo(user.name, user.id)

    if money == None:
        print("사용자 정보가 없습니다.")
        print("------------------------------\n")
        await ctx.send("등록되지 않은 사용자입니다.")
    else:
        print("사용자 정보 발견, 메세지를 보냅니다.")
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description = user.name, color = 0x62D0F6)
        embed.add_field(name = "보유 자산", value = money)
        await ctx.send(embed=embed)

@bot.command()
async def 송금(ctx, user: discord.User, money):
    if int(money) <= 0:
        await ctx.send("송금 불가능 단위")
        return 0
        
    print("송금이 가능한지 확인합니다.")
    senderExistance, senderRow = checkUser(ctx.author.name, ctx.author.id)
    receiverExistance, receiverRow = checkUser(user.name, user.id)

    if not senderExistance:
        print("DB에서", ctx.author.name, "을 찾을수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 송금이 가능합니다.")
    elif not receiverExistance:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        print("송금하려는 돈: ", money)

        s_money = getMoney(ctx.author.name, senderRow)
        r_money = getMoney(user.name, receiverRow)

        if s_money >= int(money) and int(money) != 0:
            print("돈이 충분하므로 송금을 진행합니다.")
            print("")

            remit(ctx.author.name, senderRow, user.name, receiverRow, money)

            print("송금이 완료되었습니다. 결과를 전송합니다.")

            embed = discord.Embed(title="송금 완료", description = "송금된 돈: " + money, color = 0x77ff00)
            embed.add_field(name = "보낸 사람: " + ctx.author.name, value = "현재 자산: " + str(getMoney(ctx.author.name, senderRow)))
            embed.add_field(name = "→", value = ":moneybag:")
            embed.add_field(name="받은 사람: " + user.name, value="현재 자산: " + str(getMoney(user.name, receiverRow)))
                    
            await ctx.send(embed=embed)
        elif int(money) == 0:
            await ctx.send("0원을 보낼 필요는 없죠")
        else:
            print("돈이 충분하지 않습니다.")
            print("송금하려는 돈: ", money)
            print("현재 자산: ", s_money)
            await ctx.send("돈이 충분하지 않습니다. 현재 자산: " + str(s_money))

        print("------------------------------\n")

@bot.command()
async def reset(ctx):
    delete()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다")

bot.run(DISCORD_TOKEN)