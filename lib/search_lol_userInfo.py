import discord
from discord.ext import commands
import json
import requests

def search_lol_userInfo(arg, RIOT_TOKEN):
    userInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + arg
    res = requests.get(userInfoUrl, headers={"X-Riot-Token":RIOT_TOKEN})
    resjs = json.loads(res.text)

    if res.status_code == 200:
        UserIconUrl = "http://ddragon.leagueoflegends.com/cdn/11.3.1/img/profileicon/{}.png"
        embed = discord.Embed(title=f"플레이어 {resjs['name']} 님의 정보", description=f"**{resjs['summonerLevel']} LEVEL**", color=0xFF9900)

        UserInfoUrl_2 = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + resjs["id"]
        res_2 = requests.get(UserInfoUrl_2, headers={"X-Riot-Token":RIOT_TOKEN})
        res_2js = json.loads(res_2.text)

        if res_2js == []: # User Unranked
            embed.add_field(name=f"{resjs['name']} 님은 언랭크입니다.", value="**언랭크 유저의 정보는 출력하지 않습니다.**", inline=False)

        else: # User Ranked
            for rank in res_2js:
                if rank["queueType"] == "RANKED_SOLO_5x5":
                    print(rank)
                    embed.add_field(name="솔로랭크", value=f"**티어 : {rank['tier']} {rank['rank']} - {rank['leaguePoints']} LP**\n"
                                                           f"**승 / 패 : {rank['wins']} 승 {rank['losses']} 패**", inline=True)

                else:
                    print(rank)
                    embed.add_field(name="자유랭크", value=f"**티어 : {rank['tier']} {rank['rank']} - {rank['leaguePoints']} LP**\n"
                                                            f"**승 / 패 : {rank['wins']} 승 {rank['losses']} 패**", inline=True)

        embed.set_author(name=resjs['name'], url=f"http://fow.kr/find/{arg.replace(' ', '')}", icon_url=UserIconUrl.format(resjs['profileIconId']))
        return embed

    else: # Nonexist User
        error = discord.Embed(title="존재하지 않는 소환사명입니다.\n다시 한번 확인해주세요.", color=0xFF9900)
        return error
