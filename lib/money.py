import requests
from bs4 import BeautifulSoup as bs

URL = "https://obank.kbstar.com/quics?page=C101423&QSL=F"

for_cur_exchange = {
    "달러": 0,
    "엔화": 1,
    "위안화": 9,
    "유로": 2,
    "파운드": 3,
    "헤알": 31,
    "루블": 21,
    "루피": 24
}

def foreignCurrency(arg):
    # URL에 요청 보내기
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    html = session.get(URL, headers=headers).content
    soup = bs(html, "html.parser")

    # 외화 정보 가져오기
    table = soup.find_all("table","tType01")
    target_table = table[1].select_one('tbody')
    currency_list = list(target_table.find_all("tr"))
    target_currency_total_info = str(currency_list[for_cur_exchange[arg]])

    # 외화 정보에서 매수, 매도만 가져옴 (문자열 잘르기)
    target_currency_total_info_split = target_currency_total_info.split('"tRight')
    target_currency = target_currency_total_info_split[4:6]

    target_currency_status = []
    for x in target_currency:
        a = x.replace('">','')
        b = a.replace('</td>\n<td class=','')
        c = b.replace(',','')
        target_currency_status.append(c)

    buy_cur = target_currency_status[0]
    sell_cur = target_currency_status[1]

    if arg == "엔화":
        return float(buy_cur) / 100, float(sell_cur) / 100

    return float(buy_cur), float(sell_cur)

def exchange(foreign_cur):
    if foreign_cur == "달러":
        return 7
    elif foreign_cur == "엔화":
        return 8
    elif foreign_cur == "위안화":
        return 9
    elif foreign_cur == "유로":
        return 10
    elif foreign_cur == "파운드":
        return 11
    elif foreign_cur == "헤알":
        return 12
    elif foreign_cur == "루블":
        return 13
    else:
        return 14