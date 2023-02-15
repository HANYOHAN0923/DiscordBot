import requests
from bs4 import BeautifulSoup as bs

URL = {
    "웨이브" : "https://coinmarketcap.com/currencies/waves/",
    "비트코인" : "https://coinmarketcap.com/currencies/bitcoin/",
    "이더리움" : "https://coinmarketcap.com/currencies/ethereum/",
    "도지" : "https://coinmarketcap.com/currencies/dogecoin/",
    "라이트" : "https://coinmarketcap.com/currencies/litecoin/",
    "이더리움클래식" : "https://coinmarketcap.com/currencies/ethereum-classic/",
    "루나클래식" : "https://coinmarketcap.com/currencies/terra-luna/",
    "샌드박스" : "https://coinmarketcap.com/currencies/the-sandbox/",
    "리플" : "https://coinmarketcap.com/currencies/xrp/",
}

def coin(_name):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    html = session.get(URL[_name], headers=headers).content
    soup = bs(html, "html.parser")

    div = soup.find("div","sc-1prm8qw-0 cyZVgY priceTitle")
    
    # HMTL문서에서 span 값 가져오기
    list_div = list(div)
    split_span1 = str(list_div[0]).split("<span>")
    split_span2 = str(split_span1[1]).split("</span")
    str_price = split_span2[0]

    remove1 = str_price.replace("$","")
    remove2 = remove1.replace(",","")
    float_price = float(remove2)


    return str_price, float_price