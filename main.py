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
from lib.user import *
from lib.lol_cup import search_match
from lib.gamble import *
from lib.patch_note import patch_note

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
RIOT_LOL_TOKEN = os.getenv("RIOT_LOL_TOKEN")
RIOT_TFT_TOKEN = os.getenv("RIOT_TFT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} online!')

@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title = "Obunga Bot#1375", description = "오분가 봇이 시크릿 주주 서버와 함께 합니다", color = 0x6E17E3) 
    embed.add_field(name = bot.command_prefix + "명령어", value = "Obunga Bot의 명령어를 확인합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "탈모빔 유저이름", value = "특정 유저에게 탈모빔을 날립니다. 확률이 존재합니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "갓겜판독기 게임이름", value = "특정게임이 갓겜인지 알려줍니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "병신판독기 이름", value = "특정 인물이 병신인지 알려줍니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "외화 외화이름", value = "특정 외화 시세를 알려줍니다(달러, 엔화, 위안화, 유로).", inline = False)
    embed.add_field(name = bot.command_prefix + "메뉴추천 양식 / 한식 / 중식 / 일식 / 아무거나", value = "메뉴를 추천해줍니다", inline = False)
    embed.add_field(name = bot.command_prefix + "롤전적검색 롤닉네임 ", value = "롤 전적 검색 기능입니다. 소환사 이름은 공백 없이 입력해주세요.", inline = False)
    embed.add_field(name = bot.command_prefix + "롤체전적검색 롤닉네임 ", value = "롤체 전적 검색 기능입니다. 소환사 이름은 공백 없이 입력해주세요", inline = False)
    embed.add_field(name = bot.command_prefix + "퇴근", value = "공붕이들을 위한 퇴근까지 남은 시간을 알려줍니다. 혹시 본인도 직장인이다 하면 알려주세요. 따로 퇴근시간 만들어 드립니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "회원가입", value = "디스코드 신분과 계좌를 만듭니다", inline = False)
    embed.add_field(name = bot.command_prefix + "내정보", value = "내 정보를 조회합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "정보 @유저이름", value = "특정 유저의 잔고를 조회합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "송금 @유저이름 금액", value = "특정 유저에게 작성한 금액만큼 송금합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "패치노트", value = "패치 내역을 확인합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "오분가", value = "열구의 발작 버튼입니다. 그의 본능을 깨우지마세요.", inline = False)
    embed.add_field(name = bot.command_prefix + "레벨/돈랭킹", value = "현재 보유 자산과 레벨을 기준으로 유저들의 랭킹을 보여줍니다. (나중에 두개 합칠 예정)", inline = False)
    embed.add_field(name = bot.command_prefix + "도박 배팅금액", value = "도박을 통해 성공을 하면 배팅 금액을 잃을 수도, 배팅금액의 1.5배의 금액을 얻을 수도 있습니다.\n 최소 배팅 금액은 10원이며 당첨확률은 3분의 1입니다. \n 금액 대신 올인을 작성하는 것을 통해 전재산을 배팅할 수 있습니다", inline = False)
    embed.add_field(name = bot.command_prefix + "주사위 숫자", value = "리스크 없이 돈을 벌어볼까요? 오분가는 2개의 주사위를 굴립니다. 그 합을 맞추면 50만원의 상금을 얻습니다.", inline = False)
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
    await ctx.send(recommendfood(arg))


@bot.command(name='롤전적검색')
async def cmd6(ctx, arg):
    await ctx.send(embed = search_lol_userInfo(arg, RIOT_LOL_TOKEN))


@bot.command(name= "롤체전적검색")
async def cmd7(ctx, arg):
    await ctx.send(embed = search_tft_userInfo(arg, RIOT_TFT_TOKEN))

@bot.command(name="퇴근")
async def cmd8(ctx):
    await ctx.send(countTime())

@bot.command(name="롤드컵")
async def cmd9(ctx):
    await ctx.send(embed = search_match())

@bot.command(name="오분가")
async def cmd10(ctx):
    await ctx.send(file=discord.File("./assets/images/obunga.jpg"))

@bot.command(name="패치노트")
async def cmd11(ctx):
    await ctx.send(embed = patch_note())

@bot.command(name="!p")
async def cmExtra(ctx):
    pass

@bot.command()
async def 회원가입(ctx):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await ctx.send("이미 가입하셨습니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("")

        Signup(ctx.author.name, ctx.author.id)

        print("회원가입이 완료되었습니다.")
        print("------------------------------\n")
        await ctx.send("회원가입이 완료되었습니다.")

@bot.command()
async def 탈퇴(ctx):
    print("탈퇴가 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        DeleteAccount(userRow)
        print("탈퇴가 완료되었습니다.")
        print("------------------------------\n")

        await ctx.send("탈퇴가 완료되었습니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")

        await ctx.send("등록되지 않은 사용자입니다.")

@bot.command()
async def 정보(ctx, user: discord.User):
    userExistance, userRow = checkUser(user.name, user.id)

    if not userExistance:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        level, exp, money, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description = user.name, color = 0x62D0F6)
        embed.add_field(name = ":crossed_swords: 레벨", value = level)
        embed.add_field(name = "경험치", value = str(exp) + "/" + str(level*level + 6*level))
        embed.add_field(name = "순위", value = str(rank) + "/" + str(userNum))
        embed.add_field(name = ":moneybag: 보유 자산", value = money, inline = False)
        embed.add_field(name = ":slot_machine: 도박으로 날린 돈", value = loss, inline = False)

        await ctx.send(embed=embed)

@bot.command()
async def 내정보(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, exp, money, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        expToUP = level*level + 6*level
        boxes = int(exp/expToUP*20)
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description = ctx.author.name, color = 0x62D0F6)
        embed.add_field(name = ":crossed_swords: 레벨", value = level)
        embed.add_field(name = "순위", value = str(rank) + "/" + str(userNum))
        embed.add_field(name = "XP: " + str(exp) + "/" + str(expToUP), value = boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline = False)
        embed.add_field(name = ":moneybag: 보유 자산", value = money, inline = False)
        embed.add_field(name = ":slot_machine: 도박으로 날린 돈", value = loss, inline = False)

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
async def 주사위(ctx, arg):
    if int(arg) <= 0:
        await ctx.send("올바른 값을 입력해주세요")

    result, _color, bot1, bot2, a, b = dice(int(arg))

    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "Obunga의 숫자 " + bot1 + "+" + bot2, value = ":game_die: " + a, inline = False)
    embed.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + b, inline = False)

    if result == "승리":
        userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
        modifyMoney(ctx.author.name, userRow, 500000)
        embed.set_footer(text="결과: " + result + "50만원을 상금으로 받았습니다")
    else:
        embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.command()
async def 도박(ctx, money):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    win = gamble()
    result = ""
    betting = 0
    _color = 0x000000
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        cur_money = getMoney(ctx.author.name, userRow)

        if money == "올인":
            betting = cur_money
            if win:
                result = "성공"
                _color = 0x00ff56
                print(result)

                modifyMoney(ctx.author.name, userRow, int(0.6*betting))

            else:
                result = "실패"
                _color = 0xFF0000
                print(result)

                modifyMoney(ctx.author.name, userRow, -int(betting))
                addLoss(ctx.author.name, userRow, int(betting))

            embed = discord.Embed(title = "도박 결과", description = result, color = _color)
            embed.add_field(name = "배팅금액", value = betting, inline = False)
            embed.add_field(name = "현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)

            await ctx.send(embed=embed)
            
        elif int(money) >= 10:
            if cur_money >= int(money):
                betting = int(money)
                print("배팅금액: ", betting)
                print("")

                if win:
                    result = "성공"
                    _color = 0x00ff56
                    print(result)

                    modifyMoney(ctx.author.name, userRow, int(0.5*betting))

                else:
                    result = "실패"
                    _color = 0xFF0000
                    print(result)

                    modifyMoney(ctx.author.name, userRow, -int(betting))
                    addLoss(ctx.author.name, userRow, int(betting))

                embed = discord.Embed(title = "도박 결과", description = result, color = _color)
                embed.add_field(name = "배팅금액", value = betting, inline = False)
                embed.add_field(name = "현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)

                await ctx.send(embed=embed)

            else:
                print("돈이 부족합니다.")
                print("배팅금액: ", money, " | 현재자산: ", cur_money)
                await ctx.send("돈이 부족합니다. 현재자산: " + str(cur_money))
        else:
            print("배팅금액", money, "가 10보다 작습니다.")
            await ctx.send("최소 배팅 단위는 10원 입니다")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("도박은 계좌개설 후 이용 가능합니다.")

    print("------------------------------\n")

@bot.command()
async def 레벨랭킹(ctx):
    rank = ranking()
    embed = discord.Embed(title = "레벨 랭킹", description = None, color = 0x4A44FF)

    for i in range(0,len(rank)):
        if i%2 == 0:
            name = rank[i]
            lvl = rank[i+1]
            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="레벨: "+str(lvl), inline=False)

    await ctx.send(embed=embed) 

@bot.command()
async def 돈랭킹(ctx):
    rank = ranking_money()
    embed = discord.Embed(title = "보유자산 순위", description = None, color = 0x4A44FF)

    for i in range(0,len(rank)):
        if i%2 == 0:
            name = rank[i]
            money = rank[i+1]
            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="보유자산: "+str(money), inline=False)

    await ctx.send(embed=embed) 

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "!reset":
        await bot.process_commands(message)
        return
    else:
        userExistance, userRow = checkUser(message.author.name, message.author.id)
        channel = message.channel
        if userExistance:
            levelUp, lvl = levelupCheck(userRow)
            if levelUp:
                print(message.author, "가 레벨업 했습니다")
                print("")
                modifyMoney(message.author.name, userRow, int(lvl)*100000)
                embed = discord.Embed(title = "레벨업", description = None, color = 0x00A260)
                embed.set_footer(text = f":partying_face: {message.author.name} {str(lvl)} 레벨 달성!")
                await channel.send(embed=embed)
            else:
                modifyExp(userRow, 1)
                print("------------------------------\n")

        await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다")

bot.run(DISCORD_TOKEN)
