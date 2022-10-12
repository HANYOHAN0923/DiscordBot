import requests
from bs4 import BeautifulSoup as bs

forex = {
    '달러': 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=달러&oquery=환율&tqi=hzMlFsp0J1Zssmwilk0ssssst84-408509',
    '엔화': 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=엔화&oquery=달러&tqi=hzMlqdp0YihssSfeUe8sssssty8-318354',
    '위안화': 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=위안화&oquery=엔화&tqi=hzMlrdp0YiRssi6L1h4ssssssXw-518438',
    '유로': 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=유로&oquery=위안화&tqi=hzMlVsp0J1ZssmYlNLsssssssdl-354957',
}

def foreignCurrency(ctx):
    page = requests.get(forex[ctx])
    soup = bs(page.text, "html.parser")

    find_currency_span = soup.find('div', 'rate_tlt')
    str_currency_span = str(find_currency_span)
    str_currency_span_splitList = str_currency_span.split('strong')
    str_currency_select = str_currency_span_splitList[1]
    str_currency = str_currency_select.strip("/"">""<")
    return str_currency