from discord.ext import commands
import discord
import os
import tomllib


# Custom Python Library
from lib.sb import sb
from lib.money import foreignCurrency
from lib.godgame import godgame
from lib.hairlossbeam import hairlossbeam
from lib.recommendfood import recommendfood
from lib.search_lol_userInfo import search_lol_userInfo
from lib.search_tft_userInfo import search_tft_userInfo
from lib.leavework import countTime
from lib.user_manage import * #from lib.user import * => excel to firestore
from lib.lol_cup import *
from lib.gamble import *
from lib.patch_note import patch_note
from lib.fishing import *
from lib.exchange import exchange
from lib.coin import *

with open("config.toml", mode="rb") as file:
    data = tomllib.load(file)

    DISCORD_TOKEN = data["API_KEY"]["DISCORD_TOKEN"]
    RIOT_LOL_TOKEN = data["API_KEY"]["RIOT_LOL_TOKEN"]
    RIOT_TFT_TOKEN = data["API_KEY"]["RIOT_TFT_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} online!')

@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title = "Obunga Bot#1375", description = "오분가 봇이 시크릿 주주 서버와 함께 합니다", color = 0x6E17E3) 
    embed.add_field(name = bot.command_prefix + "탈모빔 유저이름", value = "특정 유저에게 탈모빔을 날립니다. 확률이 존재합니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "갓겜판독기 게임이름", value = "특정게임이 갓겜인지 알려줍니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "병신판독기 이름", value = "특정 인물이 병신인지 알려줍니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "메뉴추천 양식 / 한식 / 중식 / 일식 / 아무거나", value = "메뉴를 추천해줍니다", inline = False)
    embed.add_field(name = bot.command_prefix + "롤전적검색 롤닉네임 ", value = "롤 전적 검색 기능입니다. 소환사 이름은 공백 없이 입력해주세요.", inline = False)
    embed.add_field(name = bot.command_prefix + "롤체전적검색 롤닉네임 ", value = "롤체 전적 검색 기능입니다. 소환사 이름은 공백 없이 입력해주세요", inline = False)
    embed.add_field(name = bot.command_prefix + "퇴근", value = "공붕이들을 위한 퇴근까지 남은 시간을 알려줍니다. 혹시 본인도 직장인이다 하면 알려주세요. 따로 퇴근시간 만들어 드립니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "회원가입", value = "디스코드 신분과 계좌를 만듭니다", inline = False)
    embed.add_field(name = bot.command_prefix + "내정보", value = "내 정보를 조회합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "정보 @유저이름", value = "특정 유저의 잔고를 조회합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "송금 @유저이름 금액", value = "특정 유저에게 작성한 금액만큼 송금합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "오분가", value = "열구의 발작 버튼입니다. 그의 본능을 깨우지마세요.", inline = False)
    embed.add_field(name = bot.command_prefix + "랭킹", value = "현재 보유 자산과 레벨을 기준으로 유저들의 랭킹을 보여줍니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "낚시", value = "낚시를 합니다. 낚시는 미끼를 필요로 합니다.", inline = False)
    embed.add_field(name = bot.command_prefix + "미끼구매 개수", value = "낚시에 필요한 미끼를 입력한 개수만큼 구입합니다. (1미끼 = 5000)", inline = False)
    embed.add_field(name = bot.command_prefix + "도박 배팅금액", value = "도박을 통해 성공을 하면 배팅 금액을 잃을 수도, 배팅금액의 1.5배의 금액을 얻을 수도 있습니다.\n 최소 배팅 금액은 10원이며 당첨확률은 3분의 1입니다. \n 금액 대신 올인을 작성하는 것을 통해 전재산을 배팅할 수 있습니다", inline = False)
    embed.add_field(name = bot.command_prefix + "주사위 숫자1 숫자2", value = "리스크 없이 돈을 벌어볼까요? 오분가는 2개의 주사위를 굴립니다. 주사위의 합, 조합, 순서를 맞춰서 상금을 얻어보세요!", inline = False)
    embed.add_field(name = bot.command_prefix + "환율 외화이름", value = "외화의 살 때와 팔 때의 가격을 보여줍니다. (가격은 현생의 시세와 같으며 5분 단위로 업데이트 됩니다)", inline = False)
    embed.add_field(name = bot.command_prefix + "외화매수/매도 외화이름 매입/매각금액", value = "특정 외화를 매입/매각할 때 사용하는 명령어입니다. 매입/매각금액은 원화가 아닌 외화를 기준으로 정수로 작성해주세요", inline = False)
    embed.add_field(name = bot.command_prefix + "코인시세 코인이름", value = "현재 코인의 시세를 보여줍니다. (외화와 다르게 실시간 업데이트 됩니다)", inline = False)
    embed.add_field(name = bot.command_prefix + "코인매수/매도 코인이름 매입/매각개수", value = "특정 코인을 매입/매각할 때 사용하는 명령어입니다. 매입/매각은 모두 달러를 통해서만 가능합니다. ", inline = False)
    embed.add_field(name = bot.command_prefix + "착취/협박 @유저이름", value = "특정 유저의 자산을 퍼센트 단위로 착취합니다 / 고승환의 커터칼 아이템을 사용하는 명령어입니다", inline = False)
    embed.add_field(name = bot.command_prefix + "아이템구매 아이템이름 개수", value = "해당 아이템을 구입합니다. 구입한 아이템은 바로 사용됩니다", inline = False)
    embed.add_field(name = bot.command_prefix + "알까기", value = "낙동강 타조알을 사용하는 명령어입니다.", inline = False)
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


@bot.command(name='환율')
async def cmd4(ctx, arg):
    buy, sell = foreignCurrency(arg)
    embed = discord.Embed(title="환율 : " + arg, description = None, color = 0xffff00)
    embed.add_field(name = "살 때", value = str(buy))
    embed.add_field(name = "---", value = ":moneybag:")
    embed.add_field(name = "팔 때", value = str(sell))
    await ctx.send(embed = embed)


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

# LCK 일정으로 바꿔주기 (이적 시즌에는 이적 글 올라오면 바로 가져오기)
@bot.command(name="롤드컵")
async def cmd9(ctx):
    await ctx.send(embed = search_match())

@bot.command(name="오분가")
async def cmd10(ctx):
    await ctx.send(file=discord.File("./assets/images/obunga.jpg"))

@bot.command(name="조유리")
async def cmd10(ctx):
    await ctx.send(file=discord.File("./assets/images/jyr.jpg"))

@bot.command(name="패치노트")
async def cmd11(ctx):
    await ctx.send(embed = patch_note())

@bot.command(name="!p")
async def cmExtra(ctx):
    pass

@bot.command()
async def 회원가입(ctx):
    print("회원가입이 가능한지 확인합니다.")
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    if userStatus:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await ctx.send("이미 가입하셨습니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("")

        signUp(ctx.author.name, ctx.author.id)

        print("회원가입이 완료되었습니다.")
        print("------------------------------\n")
        await ctx.send("회원가입이 완료되었습니다.")
'''
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
'''
@bot.command()
async def 정보(ctx, user: discord.User):
    userStatus = checkUser(user.name, user.id)

    if not userStatus:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        level, exp, money, loss, dolor, yen, yuan, euro, pound, real, ruble, rupee, waves, btc, eth, doge, ltc, etc, lunc, sand, bnb, xrp = userInfo(user.name)
        grap = checkGrap(user.name)
        userNum = checkUserNum()
        kc = checkKC(user.name)
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description = user.name, color = 0x62D0F6)
        embed.add_field(name = ":crossed_swords: 레벨", value = level)
        embed.add_field(name = "경험치", value = str(exp) + "/" + str(level*level + 6*level))
        embed.add_field(name = "=========================보유 자산=========================", value="=======================================================", inline = False)
        embed.add_field(name = ":moneybag: 보유 원화", value = format(int(money),','), inline = True)
        embed.add_field(name = ":dollar: 보유 달러", value = f'{dolor:.2f}', inline = True)
        embed.add_field(name = ":yen: 보유 엔화", value = yen, inline = True)
        embed.add_field(name = ":moneybag: 보유 위안화", value = yuan, inline = True)
        embed.add_field(name = ":euro: 보유 유로", value = euro, inline = True)
        embed.add_field(name = ":pound: 보유 파운드", value = pound, inline = True)
        embed.add_field(name = ":moneybag: 보유 헤알", value = real, inline = True)
        embed.add_field(name = ":moneybag: 보유 루블", value = ruble, inline = True)
        embed.add_field(name = ":moneybag: 보유 루피", value = rupee, inline = True)
        embed.add_field(name = ":slot_machine: 도박으로 날린 돈", value = loss, inline = False)
        embed.add_field(name = "=========================보유 코인=========================", value="=======================================================", inline = False)
        embed.add_field(name = ":coin: 웨이브 (WAVES)", value = waves, inline = True)
        embed.add_field(name = ":coin: 비트코인 (BTC)", value = btc, inline = True)
        embed.add_field(name = ":coin: 이더리움 (ETH)", value = eth, inline = True)
        embed.add_field(name = ":coin: 도지 (DOGE)", value = doge, inline = True)
        embed.add_field(name = ":coin: 라이트 (LTC)", value = ltc, inline = True)
        embed.add_field(name = ":coin: 이더리움클래식 (ETC)", value = etc, inline = True)
        embed.add_field(name = ":coin: 루나클래식 (LUNC)", value = lunc, inline = True)
        embed.add_field(name = ":coin: 샌드박스 (SAND)", value = sand, inline = True)
        embed.add_field(name = ":coin: 리플 (XRP)", value = xrp, inline = True)
        embed.add_field(name = ":hand_splayed: 착취의 손아귀", value = str(grap), inline = True)
        embed.add_field(name = ":knife: 고승환의 커터칼", value = str(kc), inline=True)

        await ctx.send(embed=embed)

@bot.command()
async def 내정보(ctx):
    userStatus = checkUser(ctx.author.name, ctx.author.id)

    if not userStatus:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, exp, money, loss, dolor, yen, yuan, euro, pound, real, ruble, rupee, waves, btc, eth, doge, ltc, etc, lunc, sand, bnb, xrp = userInfo(ctx.author.name)
        grap = checkGrap(ctx.author.name)
        kc = checkKC(ctx.author.name)
        userNum = checkUserNum()
        expToUP = level*level + 6*level
        boxes = int(exp/expToUP*20)
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description = ctx.author.name, color = 0x62D0F6)
        embed.add_field(name = ":crossed_swords: 레벨", value = level)
        embed.add_field(name = "XP: " + str(exp) + "/" + str(expToUP), value = boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline = False)
        embed.add_field(name = "=========================보유 자산=========================", value="=======================================================", inline = False)
        embed.add_field(name = ":moneybag: 원화", value = format(int(money),','), inline = True)
        embed.add_field(name = ":dollar: 달러", value = f'{dolor:.2f}', inline = True)
        embed.add_field(name = ":yen: 엔화", value = yen, inline = True)
        embed.add_field(name = ":moneybag: 위안화", value = yuan, inline = True)
        embed.add_field(name = ":euro: 유로", value = euro, inline = True)
        embed.add_field(name = ":pound: 파운드", value = pound, inline = True)
        embed.add_field(name = ":moneybag: 헤알", value = real, inline = True)
        embed.add_field(name = ":moneybag: 루블", value = ruble, inline = True)
        embed.add_field(name = ":moneybag: 루피", value = rupee, inline = True)
        embed.add_field(name = ":slot_machine: 도박으로 날린 돈", value = loss, inline = False)
        embed.add_field(name = "=========================보유 코인=========================", value="=======================================================", inline = False)
        embed.add_field(name = ":coin: 웨이브 (WAVES)", value = waves, inline = True)
        embed.add_field(name = ":coin: 비트코인 (BTC)", value = btc, inline = True)
        embed.add_field(name = ":coin: 이더리움 (ETH)", value = eth, inline = True)
        embed.add_field(name = ":coin: 도지 (DOGE)", value = doge, inline = True)
        embed.add_field(name = ":coin: 라이트 (LTC)", value = ltc, inline = True)
        embed.add_field(name = ":coin: 이더리움클래식 (ETC)", value = etc, inline = True)
        embed.add_field(name = ":coin: 루나클래식 (LUNC)", value = lunc, inline = True)
        embed.add_field(name = ":coin: 샌드박스 (SAND)", value = sand, inline = True)
        embed.add_field(name = ":coin: 리플 (XRP)", value = xrp, inline = True)
        embed.add_field(name = ":hand_splayed: 착취의 손아귀", value = str(grap), inline = True)
        embed.add_field(name = ":knife: 고승환의 커터칼", value = str(kc), inline=True)

        await ctx.send(embed=embed)

@bot.command()
async def 송금(ctx, user: discord.User, money):
    if int(money) <= 0:
        await ctx.send("송금 불가능 단위")
        return 0
        
    print("송금이 가능한지 확인합니다.")
    senderStatus = checkUser(ctx.author.name, ctx.author.id)
    receiverStatus = checkUser(user.name, user.id)

    if not senderStatus:
        print("DB에서", ctx.author.name, "을 찾을수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 송금이 가능합니다.")
    elif not receiverStatus:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        print("송금하려는 돈: ", money)

        s_money = getMoney(ctx.author.name)
        r_money = getMoney(user.name)
        print("Done")

        if s_money >= int(money) and int(money) != 0:
            print("돈이 충분하므로 송금을 진행합니다.")
            print("")

            remit(ctx.author.name, user.name, money)

            print("송금이 완료되었습니다. 결과를 전송합니다.")

            embed = discord.Embed(title="송금 완료", description = "송금된 돈: " + money, color = 0x77ff00)
            embed.add_field(name = "보낸 사람: " + ctx.author.name, value = "현재 자산: " + str(format(int(getMoney(ctx.author.name)),',')))
            embed.add_field(name = "→", value = ":moneybag:")
            embed.add_field(name="받은 사람: " + user.name, value="현재 자산: " + str(format(int(getMoney(user.name)),',')))
                    
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
async def 주사위(ctx, arg1, arg2):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    if userStatus:
        if checkRKC(ctx.author.name):
            modifyRKC(ctx.author.name, -1)
            await ctx.send("두더지의 협박으로 인해 진행할 수 업습니다!!!")
            return 0

        # 위스키 주사위
        if checkWIS(ctx.author.name):
            rmItem(ctx.author.name, "열구의위스키")

            result1, _color1, bot11, bot21, user11, user21, price1 = dice(arg1, arg2)
            result2, _color2, bot12, bot22, user12, user22, price2 = dice(arg1, arg2)

            embed1 = discord.Embed(title = "주사위 결과", description = None, color = _color1)

            if result1 == "아이템 획득":
                addItem(ctx.author.name, "착취의 손아귀", price1)
                embed1.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
                embed1.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")

            if result1 == "승리":
                modifyMoney(ctx.author.name, price1)
                embed1.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot11 + "+" + bot21, inline = False)
                embed1.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user11 + "+" + user21, inline = False)
                embed1.set_footer(text="결과: " + result1 + " " + str(format(price1,',')) + "만원을 상금으로 받았습니다")
            else:
                embed1.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot11 + "+" + bot21, inline = False)
                embed1.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user11 + "+" + user21, inline = False)
                embed1.set_footer(text="결과: " + result1)
            await ctx.send(embed=embed1)

            embed2 = discord.Embed(title = "주사위 결과", description = None, color = _color2)

            if result2 == "아이템 획득":
                addItem(ctx.author.name, "착취의 손아귀",price2)
                embed2.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
                embed2.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")

            if result2 == "승리":
                modifyMoney(ctx.author.name, price2)
                embed2.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot12 + "+" + bot22, inline = False)
                embed2.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user12 + "+" + user22, inline = False)
                embed2.set_footer(text="결과: " + result2 + " " + str(format(price2,',')) + "만원을 상금으로 받았습니다")
            else:
                embed2.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot12 + "+" + bot22, inline = False)
                embed2.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user12 + "+" + user22, inline = False)
                embed2.set_footer(text="결과: " + result2)
            await ctx.send(embed=embed2)
            return 0


        # 강화 주사위
        if checkVita(ctx.author.name):
            rmItem(ctx.author.name, "강동완의발포비타민")

            result, _color, bot1, bot2, user1, user2, price = enhancedDice(arg1, arg2)

            embed = discord.Embed(title = "강화 주사위 결과", description = None, color = _color)

            if result == "아이템 획득":
                addItem(ctx.author.name, "착취의 손아귀",price)
                embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
                embed.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")

            if result == "승리":
                modifyMoney(ctx.author.name, price)
                embed.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot1 + "+" + bot2, inline = False)
                embed.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user1 + "+" + user2, inline = False)
                embed.set_footer(text="결과: " + result + " " + str(format(price,',')) + "만원을 상금으로 받았습니다")
            else:
                embed.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot1 + "+" + bot2, inline = False)
                embed.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user1 + "+" + user2, inline = False)
                embed.set_footer(text="결과: " + result)
            await ctx.send(embed=embed)
            return 0


        # 일반 주사위
        result, _color, bot1, bot2, user1, user2, price = dice(arg1, arg2)

        embed = discord.Embed(title = "주사위 결과", description = None, color = _color)

        if result == "아이템 획득":
            addItem(ctx.author.name, "착취의 손아귀",price)
            embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")

        if result == "승리":
            modifyMoney(ctx.author.name, price)
            embed.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot1 + "+" + bot2, inline = False)
            embed.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user1 + "+" + user2, inline = False)
            embed.set_footer(text="결과: " + result + " " + str(format(price,',')) + "만원을 상금으로 받았습니다")
        else:
            embed.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot1 + "+" + bot2, inline = False)
            embed.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user1 + "+" + user2, inline = False)
            embed.set_footer(text="결과: " + result)
        await ctx.send(embed=embed)
    else:
        await ctx.send("주사위는 회원가입 후 진행 가능합니다.")

@bot.command()
async def 도박(ctx, money):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    win = gamble()
    result = ""
    betting = 0
    _color = 0x000000
    if userStatus:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        cur_money = getMoney(ctx.author.name)

        if money == "올인":
            betting = cur_money
            if win:
                result = "성공"
                _color = 0x00ff56
                print(result)

                modifyMoney(ctx.author.name, int(betting))

            else:
                result = "실패"
                _color = 0xFF0000
                print(result)

                modifyMoney(ctx.author.name, -int(betting))
                addLoss(ctx.author.name, int(betting))

            embed = discord.Embed(title = "도박 결과", description = result, color = _color)
            embed.add_field(name = "배팅금액", value = betting, inline = False)
            embed.add_field(name = "현재 자산", value = getMoney(ctx.author.name), inline = False)

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

                    modifyMoney(ctx.author.name, int(0.8*betting))

                else:
                    result = "실패"
                    _color = 0xFF0000
                    print(result)

                    modifyMoney(ctx.author.name, -int(betting))
                    addLoss(ctx.author.name, int(betting))

                embed = discord.Embed(title = "도박 결과", description = result, color = _color)
                embed.add_field(name = "배팅금액", value = betting, inline = False)
                embed.add_field(name = "현재 자산", value = getMoney(ctx.author.name), inline = False)

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
async def 랭킹(ctx):
    rank_lvl = rankingLv()
    embed = discord.Embed(title = "유저 랭킹", description = None, color = 0x4A44FF)

    embed.add_field(name = "--------------레벨 랭킹--------------", value=":crossed_swords:  :crossed_swords:  :crossed_swords:  :crossed_swords:  :crossed_swords:  :crossed_swords:  :crossed_swords:", inline=False)
    for i in range(0,len(rank_lvl)):
        if i%2 == 0:
            name = rank_lvl[i]
            lvl = rank_lvl[i+1]
            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="레벨: "+str(lvl), inline=False)

    rank_money = rankingMoney()
    embed.add_field(name = "--------------자산 랭킹--------------", value=":moneybag:  :moneybag:  :moneybag:  :moneybag:  :moneybag:  :moneybag:  :moneybag:", inline=False)
    for i in range(0,len(rank_money)):
        if i%2 == 0:
            name = rank_money[i]
            money = rank_money[i+1]

            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="보유자산: "+str(format(int(money),',')), inline=False)

    await ctx.send(embed=embed) 

@bot.command()
async def 미끼구매(ctx, arg):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    total_price = buyBait(arg)
        
    if userStatus:
        cur_money = getMoney(ctx.author.name)

        if total_price > cur_money:
            print("돈이 부족합니다.")
            await ctx.send("돈이 부족합니다.")

        else:
            modifyMoney(ctx.author.name, -total_price)
            addItem(ctx.author.name, "미끼", int(arg))
            await ctx.send("미끼 " + arg +"개 구매 성공")
        
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("낚시는 회원가입 후 이용 가능합니다.")

@bot.command()
async def 낚시(ctx):
    userStatus = checkUser(ctx.author.name, ctx.author.id)

    if not userStatus:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 낚시할 수 있습니다.")
        return 0
    
    if checkRKC(ctx.author.name):
        modifyRKC(ctx.author.name, -1)
        await ctx.send("두더지의 협박으로 인해 진행할 수 없습니다!!!")
        return 0

    if checkBait(ctx.author.name):
        await ctx.send("미끼가 부족합니다.")
        return 0
    
    # 위스키 낚시
    if checkWIS(ctx.author.name):
        rmItem(ctx.author.name, "열구의위스키")

        fish1, result1, _color1, deg1, url1 = fishing()
        fish2, result2, _color2, deg2, url2 = fishing()
        rmItem(ctx.author.name, "미끼")

        embed = discord.Embed(title = str(ctx.author.name)+"님의 낚시 결과", description = None, color = _color1)
        
        if fish1 == "fail" or result1 == "fail":
            embed.add_field(name = "실패", value = "나의 고기고기 물고기는 어디에, 물고기가 도망갔습니다!", inline = False)
            embed.set_image(url=url1)
            embed.set_footer(text="보상: 유미의 고기고기 물고기는 어디에")
        elif fish1 == "미끼":
            addItem(ctx.author.name, fish1, result1)
            embed.add_field(name = "아이템 획득", value = "낚시꾼이 버리고 간 미끼통을 낚았습니다!", inline = False)
            embed.set_image(url=url1)
            embed.set_footer(text="보상: 미끼 10개 (사용아이템)")
        elif fish1 == "착취의 손아귀":
            addItem(ctx.author.name, fish1, result1)
            embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed.set_image(url=url1)
            embed.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")
        elif fish1 == "고승환의 커터칼":
            addItem(ctx.author.name, fish1, result1)
            embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed.set_image(url=url1)
            embed.set_footer(text="보상: 고승환의 커터칼 (사용아이템)")
        else:
            modifyMoney(ctx.author.name, result1)
            embed.add_field(name = "성공", value = deg1 + " 등급의 " + fish1 + "를 낚았습니다.", inline = False)
            embed.set_image(url=url1)
            embed.set_footer(text="보상: " + str(format(result1,',')))
        await ctx.send(embed=embed)
        
        embed2 = discord.Embed(title = str(ctx.author.name)+"님의 낚시 결과", description = None, color = _color2)
        
        if fish2 == "fail" or result2 == "fail":
            embed2.add_field(name = "실패", value = "나의 고기고기 물고기는 어디에, 물고기가 도망갔습니다!", inline = False)
            embed2.set_image(url=url2)
            embed2.set_footer(text="보상: 유미의 고기고기 물고기는 어디에")
        elif fish2 == "미끼":
            addItem(ctx.author.name, fish2, result2)
            embed2.add_field(name = "아이템 획득", value = "낚시꾼이 버리고 간 미끼통을 낚았습니다!", inline = False)
            embed2.set_image(url=url2)
            embed2.set_footer(text="보상: 미끼 10개 (사용아이템)")
        elif fish2 == "착취의 손아귀":
            addItem(ctx.author.name, fish2, result2)
            embed2.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed2.set_image(url=url2)
            embed2.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")
        elif fish2 == "고승환의 커터칼":
            addItem(ctx.author.name, fish2, result2)
            embed2.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed2.set_image(url=url2)
            embed2.set_footer(text="보상: 고승환의 커터칼 (사용아이템)")
        else:
            modifyMoney(ctx.author.name, result2)
            embed2.add_field(name = "성공", value = deg2 + " 등급의 " + fish2 + "를 낚았습니다.", inline = False)
            embed2.set_image(url=url2)
            embed2.set_footer(text="보상: " + str(format(result2,',')))
        await ctx.send(embed=embed2)
        return 0
    

    # 강화 낚시
    if checkVita(ctx.author.name):
        rmItem(ctx.author.name, "강동완의발포비타민")

        fish, result, _color, deg, url = enhancedFishing()
        rmItem(ctx.author.name, "미끼")
        print(fish)
        print(result)
        print(deg)

        embed = discord.Embed(title = str(ctx.author.name)+"님의 강화 낚시 결과", description = None, color = _color)
        
        if fish == "fail" or result == "fail":
            embed.add_field(name = "실패", value = "나의 고기고기 물고기는 어디에, 물고기가 도망갔습니다!", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: 유미의 고기고기 물고기는 어디에")
        elif fish == "미끼":
            addItem(ctx.author.name, fish, result)
            embed.add_field(name = "아이템 획득", value = "낚시꾼이 버리고 간 미끼통을 낚았습니다!", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: 미끼 10개 (사용아이템)")
        elif fish == "착취의 손아귀":
            addItem(ctx.author.name, fish, result)
            embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")
        elif fish == "고승환의 커터칼":
            addItem(ctx.author.name, fish, result)
            embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: 고승환의 커터칼 (사용아이템)")
        else:
            modifyMoney(ctx.author.name, result)
            embed.add_field(name = "성공", value = deg + " 등급의 " + fish + "를 낚았습니다.", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: " + str(format(result,',')))
        
        await ctx.send(embed=embed)
        return 0


    # 바지락 낚시
    if checkBK(ctx.author.name):
        rmItem(ctx.author.name, "바지락칼국수")

        fish, result, _color, deg, url = bkFishing()
        rmItem(ctx.author.name, "미끼")
        print(fish)
        print(result)
        print(deg)

        embed = discord.Embed(title = str(ctx.author.name)+"님의 강화 낚시 결과", description = None, color = _color)
        
        if fish == "fail" or result == "fail":
            embed.add_field(name = "실패", value = "나의 고기고기 물고기는 어디에, 물고기가 도망갔습니다!", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: 유미의 고기고기 물고기는 어디에")
        elif fish == "미끼":
            addItem(ctx.author.name, fish, result)
            embed.add_field(name = "아이템 획득", value = "낚시꾼이 버리고 간 미끼통을 낚았습니다!", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: 미끼 10개 (사용아이템)")
        elif fish == "착취의 손아귀":
            addItem(ctx.author.name, fish, result)
            embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")
        elif fish == "고승환의 커터칼":
            addItem(ctx.author.name, fish, result)
            embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: 고승환의 커터칼 (사용아이템)")
        else:
            modifyMoney(ctx.author.name, result)
            embed.add_field(name = "성공", value = deg + " 등급의 " + fish + "를 낚았습니다.", inline = False)
            embed.set_image(url=url)
            embed.set_footer(text="보상: " + str(format(result,',')))
        
        await ctx.send(embed=embed)
        return 0

    # 일반 낚시
    fish, result, _color, deg, url = fishing()
    rmItem(ctx.author.name, "미끼")
    print(fish)
    print(result)
    print(deg)

    embed = discord.Embed(title = str(ctx.author.name)+"님의 낚시 결과", description = None, color = _color)
    
    if fish == "fail" or result == "fail":
        embed.add_field(name = "실패", value = "나의 고기고기 물고기는 어디에, 물고기가 도망갔습니다!", inline = False)
        embed.set_image(url=url)
        embed.set_footer(text="보상: 유미의 고기고기 물고기는 어디에")
    elif fish == "미끼":
        addItem(ctx.author.name, fish, result)
        embed.add_field(name = "아이템 획득", value = "낚시꾼이 버리고 간 미끼통을 낚았습니다!", inline = False)
        embed.set_image(url=url)
        embed.set_footer(text="보상: 미끼 10개 (사용아이템)")
    elif fish == "착취의 손아귀":
        addItem(ctx.author.name, fish, result)
        embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
        embed.set_image(url=url)
        embed.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")
    elif fish == "고승환의 커터칼":
        addItem(ctx.author.name, fish, result)
        embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
        embed.set_image(url=url)
        embed.set_footer(text="보상: 고승환의 커터칼 (사용아이템)")
    else:
        modifyMoney(ctx.author.name, result)
        embed.add_field(name = "성공", value = deg + " 등급의 " + fish + "를 낚았습니다.", inline = False)
        embed.set_image(url=url)
        embed.set_footer(text="보상: " + str(format(result,',')))
    
    await ctx.send(embed=embed)

@bot.command()
async def 외화매수(ctx, kind, money):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    _money = int(money)
    _color = 0xFF7F00

    buy_cur, sell_cur = foreignCurrency(kind)
    total_exchange = buy_cur * _money
    
    if userStatus:
        cur_money = getMoney(ctx.author.name)

        if total_exchange > cur_money:
            print("돈이 부족합니다.")
            await ctx.send("돈이 부족합니다.")
        
        else:
            _c = exchange(kind)
            modifyMoney(ctx.author.name, -total_exchange)
            tradeForeignCurrency(ctx.author.name, _money, _c)
            embed = discord.Embed(title="거래 완료", description = "외환 거래가 성공했습니다", color = _color)
            embed.add_field(name = "원화" + ctx.author.name, value = str(total_exchange))
            embed.add_field(name = "→", value = ":moneybag:")
            embed.add_field(name= kind, value=str(_money))
            await ctx.send(embed=embed)

    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("외환거래는 회원가입 후 이용 가능합니다.")
    
@bot.command()
async def 외화매도(ctx, kind, money):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    _money = int(money)
    _color = 0xFF7F00

    if userStatus:
        _c = exchange(kind)
        cur_money = getForeignCurrency(ctx.author.name, _c)

        if _money > cur_money:
            print("돈이 부족합니다")
            await ctx.send("해당 외화가 충분하지 않습니다.")

        else:
            buy_cur, sell_cur = foreignCurrency(kind)
            total_exchange = sell_cur * _money
            modifyMoney(ctx.author.name, total_exchange)
            tradeForeignCurrency(ctx.author.name,  -_money, _c)
            embed = discord.Embed(title="거래 완료", description = "외환 거래가 성공했습니다", color = _color)
            embed.add_field(name= kind, value=str(_money))
            embed.add_field(name = "→", value = ":moneybag:")
            embed.add_field(name = "원화", value = str(total_exchange))
            await ctx.send(embed=embed)
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("외환거래는 회원가입 후 이용 가능합니다.")

@bot.command()
async def 코인시세(ctx, arg):
    str, float = coin(arg)

    embed = discord.Embed(title=arg, description = arg + "의 시세를 조회합니다.", color = 0x008000)
    embed.add_field(name = ":coin: " + arg, value = ":dollar: " + str)

    await ctx.send(embed=embed)

@bot.command()
async def 코인매수(ctx, arg, amount):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    _color = 0xFF7F00

    str_coin, float_coin = coin(arg)
    total_money = float_coin * int(amount)

    if userStatus:
        cur_money = getDollar(ctx.author.name)
    
        if total_money > cur_money:
            print("돈이 부족합니다.")
            await ctx.send("보유 달라가 부족합니다.")
        
        else:
            modifyDollar(ctx.author.name, -total_money)
            modifyCoin(ctx.author.name, int(amount), arg)
            embed = discord.Embed(title="거래 완료", description = "코인 거래가 성공했습니다", color = _color)
            embed.add_field(name = "달라" + ctx.author.name, value = str(total_money))
            embed.add_field(name = "→", value = ":coin:")
            embed.add_field(name= arg, value=str(amount))
            await ctx.send(embed=embed)

    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("외환거래는 회원가입 후 이용 가능합니다.")
        
@bot.command()
async def 코인매도(ctx, arg, amount):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    _color = 0xFF7F00

    str_coin, float_coin = coin(arg)

    if userStatus:

        cur_coin = getCoin(ctx.author.name, arg)

        if int(amount) > cur_coin:
            print("해당 코인 잔고가 부족합니다.")
            await ctx.send("해당 코인 잔고가 부족합니다.")
        
        else:
            total_money = float_coin * int(amount)
            modifyDollar(ctx.author.name, total_money)
            modifyCoin(ctx.author.name,  -int(amount), arg)
            embed = discord.Embed(title="거래 완료", description = "코인 거래가 성공했습니다", color = _color)
            embed.add_field(name= arg, value=str(amount))
            embed.add_field(name = "→", value = ":dollar:")
            embed.add_field(name = "달라" + ctx.author.name, value = str(total_money))
            await ctx.send(embed=embed)

    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("외환거래는 회원가입 후 이용 가능합니다.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "!reset":
        await bot.process_commands(message)
        return
    else:
        userStatus = checkUser(message.author.name, message.author.id)
        channel = message.channel
        if userStatus:
            levelUp, lvl = levelUpCheck(message.author.name)
            if levelUp:
                print(message.author, "가 레벨업 했습니다")
                print("")
                modifyMoney(message.author.name, int(lvl)*100000)
                embed = discord.Embed(title = "레벨업", description = None, color = 0x00A260)
                embed.set_footer(text = f"홀리 쉿~! {message.author.name} {str(lvl)} 레벨 달성!!!")
                await channel.send(embed=embed)
            else:
                modifyExp(message.author.name, 1)
                print("------------------------------\n")

        await bot.process_commands(message)

@bot.command()
async def 착취(ctx, user: discord.User):
    print("착취 시전자와 타겟 정보 조회")
    senderStatus = checkUser(ctx.author.name, ctx.author.id)
    receiverStatus = checkUser(user.name, user.id)

    print("착취가 가능한지 조회합니다")
    if checkGrap(ctx.author.name) == 0:
        await ctx.send("착취 아이템이 없습니다.")
        return 0
    
    print("착취 범위 설정 중...")
    n = randint(5,35) / 100
    print(f"시전자는 타겟의 {n*100}%를 착취합니다.")
    
    if not senderStatus:
        print("DB에서", ctx.author.name, "을 찾을수 없습니다")
        print("------------------------------\n")
        await ctx.send("착취는 회원가입 이후 사용할 수 있습니다.")
    elif not receiverStatus:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name  + " 은(는) 등록되지 않은 유저입니다.")
    else:
        print("두 유저들의 돈 정보를 가져옵니다.")
        s_money = getMoney(user.name)
        r_money = getMoney(ctx.author.name)

        money = int(s_money * n)
        print("착취 금액: ", money)

        remit(user.name, ctx.author.name, money)
        rmItem(ctx.author.name, "착취의 손아귀")
        print("착취 완료되었습니다. 결과를 전송합니다.")

        embed = discord.Embed(title="착취의 손아귀", description = "지목한 유저의 자산을 성공적으로 착취했습니다.", color = 0x023020)
        embed.add_field(name = "착취 사용 결과", value = "유저" + str(user.name) + "의 자산 " + str(int(n*100)) + "%의 금액 ₩" + str(format(money,',')) + "을 착취했습니다.")

        await ctx.send(embed=embed)

@bot.command()
async def 아이템구매(ctx, item, amount):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    _amount = int(amount)

    if userStatus:
        if item == "바지락칼국수":
            _money = 500000
        elif item == "강동완의발포비타민":
            _money = 1500000
        elif item == "열구의위스키":
            _money = 1000000
        elif item == "낙동강타조알":
            _money = 700000
        else:
            await ctx.send("없는 아이템입니다.")
            return 0

        cur_money = getMoney(ctx.author.name)

        if _money*_amount > cur_money:
            print("돈이 부족합니다")
            await ctx.send("돈이 부족합니다.")

        else:
            modifyMoney(ctx.author.name, -(_money*_amount))
            addItem(ctx.author.name, item, _amount)
            embed = discord.Embed(title="구매 완료", description = "아이템 구매를 성공했습니다", color = 0x50bcdf)
            embed.add_field(name= "구매 영수증", value="구매 아이템: " + item + " / 개수: " + amount + "/ 금액: " + str(_money*_amount))
            await ctx.send(embed=embed)
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("아이템구매는 회원가입 후 이용 가능합니다.")

@bot.command()
async def 협박(ctx, user: discord.User):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    receiverStatus = checkUser(user.name, user.id)

    if not receiverStatus:
        await ctx.send("대상을 찾을 수 없습니다.")

    if userStatus:
        if checkKC(ctx.author.name) == 0:
            await ctx.send("아이템: 고승환의 커터칼이 부족합니다.")
            return 0
        rmItem(ctx.author.name, "고승환의 커터칼")
        modifyRKC(user.name, 1)
        await ctx.send("고승환의 커터칼로 " + user.name +"을 협박했습니다.")
    else:
        print("DB에서 찾을 수 없는 유저")
        await ctx.send("대상을 찾을 수 없습니다.")

@bot.command()
async def 알까기(ctx):
    userStatus = checkUser(ctx.author.name, ctx.author.id)
    
    if userStatus:
        if checkOE(ctx.author.name):
            result,url = openOE()
            rmItem(ctx.author.name, "낙동강타조알")
            if result == "fail":
                embed = discord.Embed(title="알까기 실패", description = "타조알의 부화가 실패했습니다", color = 0xDB4455)
                embed.set_image(url=url)
                await ctx.send(embed=embed)
                return 0
            elif result == "빡친 타조":
                modifyMoney(ctx.author.name, -1000000)
                embed = discord.Embed(title="알까기 실패", description = "타조가 화났습니다. 타조에게 금품을 갈취 당했습니다.", color = 0xDB445)
                embed.set_image(url=url)
                embed.set_footer(text="₩-1,000,000")
                await ctx.send(embed=embed)
                return 0
            else:
                addItem(ctx.author.name, result, 1)
                embed = discord.Embed(title="알까기 성공", description = result + "를 1개 얻었습니다.", color = 0xffffff)
                embed.set_image(url=url)
                await ctx.send(embed=embed)
                return 0
        else:
            await ctx.send("아이템: 낙동강 타조알이 부족합니다.")
            return 0
    else:
        print("DB에서 조회할 수 없는 유저입니다.")
        await ctx.send("알까기는 회원가입 후 할 수 있습니다.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass

bot.run(DISCORD_TOKEN)
