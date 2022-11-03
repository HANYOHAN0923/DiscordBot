import discord
from datetime import datetime

def patch_note():

    today = datetime.now()
    t_month = int(today.month)
    t_day = int(today.day)
    embed = discord.Embed(title="Obunga 2.20 패치버전", description=f"{t_month}월 {t_day}일 오분가 패치 내용", color=0xAEE3D4)
    embed.add_field(value = "주사위 게임의 내용과 보상을 수정하였습니다. \n 1) 주사위 2개의 합을 맞출 경우 100만원. \n 2) 주사위 2개의 합과 주사위 눈의 값이 동일할 경우 5배 지급합니다. \n 3) 주사위 2개의 합과 주사위 눈의 값, 그리고 주사위 값의 순서 또한 같다면 25배 지급합니다.", name="주사위 내용 수정", inline=False)
    embed.add_field(value = "낚시해서 얻을 수 있는 물고기의 종류를 추가하였습니다.", name="낚시 물고기 종류 추가", inline=False)
    embed.add_field(value = "낚시를 하기 위해서는 미끼를 필요로 합니다. 상점에서 구입할 수 있습니다", name="낚시 시스템 변경", inline=False)
    embed.add_field(value = "특정 아이템을 일정 확률로 낚시를 통해 얻을 수 있습니다,", name="낚시 아이템 드랍 추가", inline=False)
    embed.add_field(value = "달러를 통한 코인 거래 기능을 추가하였습니다. 명령어를 참조해주세요.", name="코인 거래 기능 추가", inline=False)
    embed.add_field(value = "기존 원화 수치에 ,를 적용하여 금액을 읽을 때의 가독성을 향상하였습니다.", name="금액 가독성 향상", inline=False)
    embed.set_footer(text="직업과 직업을 통한 유저 간의 PVP기능, 그리고 주식거래 기능이 추가될 예정입니다.")
    return embed