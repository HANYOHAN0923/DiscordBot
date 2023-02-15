import requests
import json
import discord
from bs4 import BeautifulSoup as bs

def search_lol_userInfo(arg, RIOT_TOKEN):
    userInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + arg
    result = requests.get(userInfoUrl, headers={"X-Riot-Token":RIOT_TOKEN})
    result_json = json.loads(result.text)

    if result.status_code == 200:
        userIconUrl = "http://ddragon.leagueoflegends.com/cdn/11.3.1/img/profileicon/{}.png"
        embed = discord.Embed(title=f"소환사 {result_json['name']}님의 정보", description=f"**{result_json['summonerLevel']} LEVEL**", color=0xAEE3D4)

        userRankInfo = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + result_json["id"]
        resultRank = requests.get(userRankInfo, headers={"X-Riot-Token":RIOT_TOKEN})
        resultRank_json = json.loads(resultRank.text)

        if resultRank_json == []:
            embed.add_field(name=f"해당 유저는 언랭크입니다.", value="**언랭크 유저의 정보는 출력하지 않습니다.**", inline=False)
        else:
            for rank in resultRank_json:
                if rank["queueType"] == "RANKED_SOLO_5x5":
                    embed.add_field(name="솔로랭크", value=f"**티어 : {rank['tier']} {rank['rank']} - {rank['leaguePoints']} LP**\n"
                                                           f"**승 / 패 : {rank['wins']} 승 {rank['losses']} 패**", inline=True)
                else:
                    embed.add_field(name="자유랭크", value=f"**티어 : {rank['tier']} {rank['rank']} - {rank['leaguePoints']} LP**\n"
                                                            f"**승 / 패 : {rank['wins']} 승 {rank['losses']} 패**", inline=True)
        embed.set_author(name=result_json['name'], url=f"http://fow.kr/find/{arg.replace(' ', '')}", icon_url=userIconUrl.format(result_json['profileIconId']))
        return embed
    else:
        error = discord.Embed(title="오류가 발생했습니다.", description="소환사 이름이 존재하지 않거나, 통신에 오류가 있습니다.", color=0xEF5A68)
        return error

def search_tft_userInfo(arg, RIOT_TOKEN):
    userInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + arg
    result = requests.get(userInfoUrl, headers={"X-Riot-Token":RIOT_TOKEN})
    result_json = json.loads(result.text)

    if result.status_code == 200:
        UserIconUrl = "http://ddragon.leagueoflegends.com/cdn/11.3.1/img/profileicon/{}.png"
        embed = discord.Embed(title=f"소환사 {result_json['name']} 님의 정보", description=f"**{result_json['summonerLevel']} LEVEL**", color=0x9CDEF8)

        userRankInfo = "https://kr.api.riotgames.com/tft/league/v1/entries/by-summoner/" + result_json["id"]
        resultRank = requests.get(userRankInfo, headers={"X-Riot-Token":RIOT_TOKEN})
        resultRank_json = json.loads(resultRank.text)
        
        if resultRank_json == []: # User Unranked
            embed.add_field(name=f"해당 유저는 언랭크입니다.", value="**언랭크 유저의 정보는 출력하지 않습니다.**", inline=False)

        else: # User Ranked
            for rank in resultRank_json:
                if rank["queueType"] == "RANKED_TFT":              
                    embed.add_field(name="솔로랭크", value=f"**티어 : {rank['tier']} {rank['rank']} - {rank['leaguePoints']} LP**\n"
                                                          f"**승 / 패 : {rank['wins']} 승 {rank['losses']} 패**", inline=True)
                else:
                    embed.add_field(name="듀오 / 초고속모드", value=f"**티어 : {rank['ratedTier']} - {rank['ratedRating']} LP**\n"
                                                            f"**승 / 패 : {rank['wins']} 승 {rank['losses']} 패**", inline=True)

        embed.set_author(name=result_json['name'], url=f"http://fow.kr/find/{arg.replace(' ', '')}", icon_url=UserIconUrl.format(result_json['profileIconId']))
        return embed

    else:
        error = discord.Embed(title="오류가 발생했습니다.", description="소환사 이름이 존재하지 않거나, 통신에 오류가 있습니다.", color=0xEF5A68)
        return error

def select_champion(argLane, argChampion):
    lanes = {'탑':'top', '정글':'jg', '미드':'mid', '원딜':'adc', '서폿':'sup'}
    champions_kr = []
    champions_en = []

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json', headers=headers).json()[0]
    champion_kr_list = requests.get('https://ddragon.leagueoflegends.com/cdn/' + version + '/data/ko_KR/champion.json', headers=headers).json()['data']
    champion_en_list = requests.get('https://ddragon.leagueoflegends.com/cdn/' + version + '/data/en_US/champion.json', headers=headers).json()['data']

    for champion in champion_kr_list:
        champions_kr.append(champion_kr_list[champion]['name'])

    for champion in champion_en_list:
        champions_en.append(champion_en_list[champion]['name'])

    lane_selected = lanes[argLane]
    champion_selected = str(champions_en[champions_kr.index(argChampion)]).lower()
    
    page = requests.get(f"https://www.op.gg/champions/{champion_selected}/{lane_selected}/build?region=kr&tier=platinum_plus", headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
    soup = bs(page.text, "html.parser")
    
    # 승률 픽률 벤률
    total_champ_info = []
    info_champ = soup.findAll("div","css-oxevym ew1oorz5")
    for info in info_champ:
        total_champ_info.append(info.text)

    # 스킬 순서
    skill_sequence_list = []
    skill_master = soup.findAll("span","css-vegv5g e80y3m6")
    for skill in skill_master:
        skill_sequence_list.append(skill.text)
    skill_sequence = " >> ".join(s for s in skill_sequence_list)

    # 티어
    tier = soup.find("span","tier-color")
    
    embed = discord.Embed(title=f"{argChampion} 빌드 - {argLane} ({tier.text})", description=f"승률: {total_champ_info[0]}, 픽률: {total_champ_info[1]}, 밴률: {total_champ_info[2]}", color=0x50bcdf)
    embed.set_thumbnail(url=f'https://opgg-static.akamaized.net/meta/images/lol/champion/{str(champions_en[champions_kr.index(argChampion)])}.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto,f_webp,w_160&v=1676361889636')
    embed.add_field(name="추천 스킬 빌드", value=f"{skill_sequence}", inline=False)

    return embed