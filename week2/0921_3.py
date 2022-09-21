import requests
from bs4 import BeautifulSoup

codes = ['035720','035420','005930','000660','066570']

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')

    print(price)