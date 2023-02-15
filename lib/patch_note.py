import discord
from datetime import datetime

def patch_note():

    today = datetime.now()
    t_month = int(today.month)
    t_day = int(today.day)
    embed = discord.Embed(title="Obunga Final 패치버전", description=f"{t_month}월 {t_day}일 오분가 패치 내용", color=0xAEE3D4)
    embed.add_field(name="Farewell Obunga",value = "오분가의 마지막 패치입니다. 디코 오분가 서버 내에는 앞으로 오류 수정을 제외하고 다른 컨텐츠 추가는 없을 예정입니다.", inline=False)
    return embed