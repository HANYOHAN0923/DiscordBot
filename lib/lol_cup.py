import requests
from bs4 import BeautifulSoup as bs
import discord
from datetime import datetime

def search_match():
    page = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A1%A4%EB%93%9C%EC%BB%B5")
    soup = bs(page.text, "html.parser")

    matches = []

    total_match = soup.findAll('span', 'text')
    total_match_list = list(total_match)

    for i in total_match_list:
        x = str(i)
        y = x.replace("</span>","")
        matches.append(y.replace('<span class="text">',''))

    today = datetime.now()

    t_hour = int(today.hour)
    t_month = int(today.month)
    t_day = int(today.day)

    if t_hour > 15:
        t_day += 1

    embed = discord.Embed(title=f"오늘의 경기", description=f"{t_month}월 {t_day}일 {matches[0]} 일정", color=0xAEE3D4)

    remove = matches[0]
    teams = []

    for i in matches:
        if i != remove:
            teams.append(i)

    hour = 6
    index_x = 0
    index_y = 1

    for x in range(0, int(len(teams)/2)):
        embed.add_field(value = f"{teams[index_x]} VS {teams[index_y]}", name=f"제 {x+1}경기 0{hour}:00 AM", inline=True)
        index_x += 2
        index_y += 2
        hour += 1
    
    return embed