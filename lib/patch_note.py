import discord
from datetime import datetime

def patch_note():

    today = datetime.now()
    t_month = int(today.month)
    t_day = int(today.day)
    embed = discord.Embed(title="Obunga 1.03 패치버전", description=f"{t_month}월 {t_day}일 오분가 패치 내용", color=0xAEE3D4)
    embed.add_field(value = "코드를 수정 및 로직 개선을 통해 처리 속도를 올렸습니다.", name=f"오분가 성능 개선", inline=False)
    embed.add_field(value = "다양한 명령어들을 추가하였습니다. '!명령어'를 통해서 확인해주세요.", name="명령어 추가", inline=False)
    embed.add_field(value = "특정 유저가 명령어에 불특정된 값을 입력하는 것을 통해 버그가 발생할 경우 롤백할 수 있는 기능을 추가하였습니다.", name="롤백 기능 추가", inline=False)
    
    return embed