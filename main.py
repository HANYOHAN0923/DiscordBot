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
from lib.user import *
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
    embed.add_field(name = bot.command_prefix + "명령어", value = "Obunga Bot의 명령어를 확인합니다", inline = False)
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
    embed.add_field(name = bot.command_prefix + "패치노트", value = "패치 내역을 확인합니다", inline = False)
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
    embed.add_field(name = bot.command_prefix + "착취 @유저이름", value = "특정 유저의 자산을 퍼센트 단위로 착취합니다", inline = False)
    embed.add_field(name = bot.command_prefix + "주식매입/매각 주식이름", value = "추후 추가 예정인 명령어입니다", inline = False)
    embed.add_field(name = bot.command_prefix + "전직 직업", value = "추후 추가 예정인 명령어입니다", inline = False)
    embed.add_field(name = bot.command_prefix + "스킬 @유저이름", value = "추후 추가 예정인 명령어입니다", inline = False)
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
        level, exp, money, loss, dolor, yen, yuan, euro, pound, real, ruble, rupee, waves, btc, eth, doge, ltc, etc, lunc, sand, bnb, xrp = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description = user.name, color = 0x62D0F6)
        embed.add_field(name = ":crossed_swords: 레벨", value = level)
        embed.add_field(name = "순위", value = str(rank) + "/" + str(userNum))
        embed.add_field(name = "경험치", value = str(exp) + "/" + str(level*level + 6*level))
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
        embed.add_field(name = "============================================", value = None, inline = False)
        embed.add_field(name = ":coin: 웨이브 (WAVES)", value = waves, inline = True)
        embed.add_field(name = ":coin: 비트코인 (BTC)", value = btc, inline = True)
        embed.add_field(name = ":coin: 이더리움 (ETH)", value = eth, inline = True)
        embed.add_field(name = ":coin: 도지 (DOGE)", value = doge, inline = True)
        embed.add_field(name = ":coin: 라이트 (LTC)", value = ltc, inline = True)
        embed.add_field(name = ":coin: 이더리움클래식 (ETC)", value = etc, inline = True)
        embed.add_field(name = ":coin: 루나클래식 (LUNC)", value = lunc, inline = True)
        embed.add_field(name = ":coin: 샌드박스 (SAND)", value = sand, inline = True)
        embed.add_field(name = ":coin: 비앤비 (BNB)", value = bnb, inline = True)
        embed.add_field(name = ":coin: 리플 (XRP)", value = xrp, inline = True)

        await ctx.send(embed=embed)

@bot.command()
async def 내정보(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, exp, money, loss, dolor, yen, yuan, euro, pound, real, ruble, rupee, waves, btc, eth, doge, ltc, etc, lunc, sand, bnb, xrp = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        expToUP = level*level + 6*level
        boxes = int(exp/expToUP*20)
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description = ctx.author.name, color = 0x62D0F6)
        embed.add_field(name = ":crossed_swords: 레벨", value = level)
        embed.add_field(name = "순위", value = str(rank) + "/" + str(userNum))
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
        embed.add_field(name = ":coin: 비앤비 (BNB)", value = bnb, inline = True)
        embed.add_field(name = ":coin: 리플 (XRP)", value = xrp, inline = True)

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
            embed.add_field(name = "보낸 사람: " + ctx.author.name, value = "현재 자산: " + str(format(int(getMoney(ctx.author.name, senderRow)),',')))
            embed.add_field(name = "→", value = ":moneybag:")
            embed.add_field(name="받은 사람: " + user.name, value="현재 자산: " + str(format(int(getMoney(user.name, receiverRow)),',')))
                    
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
    result, _color, bot1, bot2, user1, user2, price = dice(arg1, arg2)

    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "Obunga의 숫자 ", value = ":game_die: " + bot1 + "+" + bot2, inline = False)
    embed.add_field(name = ctx.author.name+"의 숫자 ", value = ":game_die: " + user1 + "+" + user2, inline = False)

    if result == "승리":
        userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
        modifyMoney(ctx.author.name, userRow, price)
        embed.set_footer(text="결과: " + result + " " + str(format(price,',')) + "만원을 상금으로 받았습니다")
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

                modifyMoney(ctx.author.name, userRow, int(betting))

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

                    modifyMoney(ctx.author.name, userRow, int(0.8*betting))

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
async def 랭킹(ctx):
    rank_lvl = ranking()
    embed = discord.Embed(title = "유저 랭킹", description = None, color = 0x4A44FF)

    embed.add_field(name = "--------------레벨 랭킹--------------", value=":crossed_swords:  :crossed_swords:  :crossed_swords:  :crossed_swords:  :crossed_swords:  :crossed_swords:  :crossed_swords:", inline=False)
    for i in range(0,len(rank_lvl)):
        if i%2 == 0:
            name = rank_lvl[i]
            lvl = rank_lvl[i+1]
            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="레벨: "+str(lvl), inline=False)

    rank_money = ranking_money()
    embed.add_field(name = "--------------자산 랭킹--------------", value=":moneybag:  :moneybag:  :moneybag:  :moneybag:  :moneybag:  :moneybag:  :moneybag:", inline=False)
    for i in range(0,len(rank_money)):
        if i%2 == 0:
            name = rank_money[i]
            money = rank_money[i+1]

            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="보유자산: "+str(format(int(money),',')), inline=False)

    await ctx.send(embed=embed) 

@bot.command()
async def 미끼구매(ctx, arg):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    total_price = buyBait(arg)
        
    if userExistance:
        cur_money = getMoney(ctx.author.name, userRow)

        if total_price > cur_money:
            print("돈이 부족합니다.")
            await ctx.send("돈이 부족합니다.")

        else:
            modifyMoney(ctx.author.name, userRow, -total_price)
            addBait(ctx.author.name, userRow, arg)
            await ctx.send("미끼 " + arg +"개 구매 성공")
        
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("낚시는 회원가입 후 이용 가능합니다.")

@bot.command()
async def 낚시(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 낚시할 수 있습니다.")

    if checkBait(userRow):
        await ctx.send("미끼가 부족합니다.")
        return 0

    fish, result, _color, deg = fishing()
    delBait(ctx.author.name, userRow)
    print(fish)
    print(result)
    print(deg)

    embed = discord.Embed(title = str(ctx.author.name)+"님의 낚시 결과", description = None, color = _color)
    
    if fish == "fail" or result == "fail":
        embed.add_field(name = "실패", value = "나의 고기고기 물고기는 어디에, 물고기가 도망갔습니다!", inline = False)
        embed.set_footer(text="보상: 유미의 고기고기 물고기는 어디에")
    elif fish == "미끼":
        addBait(ctx.author.name, userRow, result)
        embed.add_field(name = "아이템 획득", value = "낚시꾼이 버리고 간 미끼통을 낚았습니다!", inline = False)
        embed.set_footer(text="보상: 미끼 10개 (사용아이템)")
    elif fish == "착취":
        addGrap(ctx.author.name, result)
        embed.add_field(name = "아이템 획득", value = "어둠이 느껴지는 이 물건, 누군가를 파괴할 수 있는 힘이 잠재된 것 같습니다!", inline = False)
        embed.set_footer(text="보상: 착취의 손아귀 아이템 (사용아이템)")
    else:
        modifyMoney(ctx.author.name, userRow, result)
        embed.add_field(name = "성공", value = deg + " 등급의 " + fish + "를 낚았습니다.", inline = False)
        embed.set_footer(text="보상: " + str(format(result,',')))
    
    await ctx.send(embed=embed)

@bot.command()
async def 외화매수(ctx, kind, money):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    _money = int(money)
    _color = 0xFF7F00

    buy_cur, sell_cur = foreignCurrency(kind)
    total_exchange = buy_cur * _money
    
    if userExistance:
        cur_money = getMoney(ctx.author.name, userRow)

        if total_exchange > cur_money:
            print("돈이 부족합니다.")
            await ctx.send("돈이 부족합니다.")
        
        else:
            _c = exchange(kind)
            modifyMoney(ctx.author.name, userRow, -total_exchange)
            buyForeignCurrency(ctx.author.name, userRow, _money, _c)
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
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    _money = int(money)
    _color = 0xFF7F00

    if userExistance:
        _c = exchange(kind)
        cur_money = getForeignCurrency(ctx.author.name, userRow, _c)

        if _money > cur_money:
            print("돈이 부족합니다")
            await ctx.send("해당 외화가 충분하지 않습니다.")

        else:
            buy_cur, sell_cur = foreignCurrency(kind)
            total_exchange = sell_cur * _money
            modifyMoney(ctx.author.name, userRow, total_exchange)
            sellForeignCurrency(ctx.author.name, userRow, _money, _c)
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
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    _color = 0xFF7F00

    str_coin, float_coin = coin(arg)
    total_money = float_coin * int(amount)


    if userExistance:
        cur_money = getDollar(ctx.author.name, userRow)
    
        if total_money > cur_money:
            print("돈이 부족합니다.")
            await ctx.send("보유 달라가 부족합니다.")
        
        else:
            modifyDollar(ctx.author.name, userRow, -total_money)
            modifyCoin(ctx.author.name, userRow, int(amount), arg)
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
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    _color = 0xFF7F00

    str_coin, float_coin = coin(arg)

    if userExistance:

        cur_coin = getCoin(ctx.author.name, userRow, arg)

        if int(amount) > cur_coin:
            print("해당 코인 잔고가 부족합니다.")
            await ctx.send("해당 코인 잔고가 부족합니다.")
        
        else:
            total_money = float_coin * int(amount)
            modifyDollar(ctx.author.name, userRow, total_money)
            modifyCoin(ctx.author.name, userRow, -int(amount), arg)
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
        userExistance, userRow = checkUser(message.author.name, message.author.id)
        channel = message.channel
        if userExistance:
            levelUp, lvl = levelupCheck(userRow)
            if levelUp:
                print(message.author, "가 레벨업 했습니다")
                print("")
                modifyMoney(message.author.name, userRow, int(lvl)*100000)
                embed = discord.Embed(title = "레벨업", description = None, color = 0x00A260)
                embed.set_footer(text = f"홀리 쉿~! {message.author.name} {str(lvl)} 레벨 달성!!!")
                await channel.send(embed=embed)
            else:
                modifyExp(userRow, 1)
                print("------------------------------\n")

        await bot.process_commands(message)

@bot.command()
async def 착취(ctx, user: discord.User):
    print("착취 시전자와 타겟 정보 조회")
    senderExistance, senderRow = checkUser(user.name, user.id)
    receiverExistance, receiverRow = checkUser(ctx.author.name, ctx.author.id)

    print("착취가 가능한지 조회합니다")
    if checkGrap(receiverRow) == 0:
        await ctx.send("착취 아이템이 없습니다.")
        return 0
    
    print("착취 범위 설정 중...")
    n = randint(10,40) / 100
    print(f"시전자는 타겟의 {n*100}%를 착취합니다.")
    
    if not senderExistance:
        print("DB에서", ctx.author.name, "을 찾을수 없습니다")
        print("------------------------------\n")
        await ctx.send("착취는 회원가입 이후 사용할 수 있습니다.")
    elif not receiverExistance:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name  + " 은(는) 등록되지 않은 유저입니다.")
    else:
        print("두 유저들의 돈 정보를 가져옵니다.")
        s_money = getMoney(user.name, senderRow)
        r_money = getMoney(ctx.author.name, receiverRow)

        money = int(s_money * n)
        print("착취 금액: ", money)

        remit(user.name, senderRow, ctx.author.name, receiverRow, money)
        rmGrap(receiverRow)
        print("착취 완료되었습니다. 결과를 전송합니다.")

        embed = discord.Embed(title="착취의 손아귀", description = "지목한 유저의 자산을 성공적으로 착취했습니다.", color = 0x023020)
        embed.add_field(name = "착취 사용 결과", value = "유저" + str(user.name) + "의 자산 " + str(int(n*100)) + "%의 금액 ₩" + str(format(money,',')) + "을 착취했습니다.")

        await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다")

bot.run(DISCORD_TOKEN)
