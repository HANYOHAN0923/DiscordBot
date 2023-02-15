import requests
from bs4 import BeautifulSoup as bs
import discord

def search_match():
    # match
    page = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=lck")
    soup = bs(page.text, "html.parser")

    matches = []

    total_match = soup.findAll('span', 'text')
    
    for match in total_match:
        matches.append(match.text)

    find_days = soup.find("li","_tab state_focus")
    days = find_days.select_one("span").text.split(".")
    month = days[0]
    day = days[1]
    date = days[2]

    # ranking
    page2 = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjFE&pkid=475&os=29545047&qvt=0&query=2023%20LoL%20%EC%B1%94%ED%94%BC%EC%96%B8%EC%8A%A4%20%EC%BD%94%EB%A6%AC%EC%95%84%20%EC%8A%A4%ED%94%84%EB%A7%81%20%EC%A0%95%EA%B7%9C%EC%88%9C%EC%9C%84")
    soup = bs(page2.text, "html.parser")

    # ranking team
    ranking_team = []
    ranking_team_list = soup.findAll("span","text")
    for ranking in ranking_team_list:
        ranking_team.append(ranking.text)

 
    ranking_info = []
    ranking_list = soup.findAll("td")
    
    index = 0

    for i in range(len(ranking_team)):
        del ranking_list[index - i]
        index += 5

    for num in ranking_list:
        ranking_info.append(num.text)
    print(ranking_info)


    embed = discord.Embed(title=f" {month}월 {day}일 {date}요일 경기 일정", color=0x000080)
    embed.set_thumbnail(url="https://search.pstatic.net/common?type=ofullfill&size=174x174&quality=75&direct=true&ttype=input&src=http%3A%2F%2Fbdata.statiz.co.kr%2FeSports%2Fstats%2FeSports%2Flogo%2F202212%2F2022120710410644.png")
    embed.add_field(value = f"{matches[1]} VS {matches[2]}", name=f"제 1 경기 17:00 {matches[0]}", inline=False)
    embed.add_field(value = f"{matches[4]} VS {matches[5]}", name=f"제 2 경기 19:30 {matches[3]}", inline=False)

    embed.add_field(value = f" ", name=f"======================= 정규순위 =======================", inline=False)

    index = 0
    for i in range(0,10):
        embed.add_field(name = f"{i+1}위 {ranking_team[i]}", value=f" 승: {ranking_info[index]} 패: {ranking_info[index+1]} 승률: {ranking_info[index+2]} 득실: {ranking_info[index+3]}", inline=False)
        index += 4
    return embed