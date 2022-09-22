#네이버 쇼핑 애플 최저가 찾기 만들기


from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pyautogui

now = datetime.now()
date = now.date

keyword = pyautogui.prompt("검색어를 입력하세요.  ")
lastpage = pyautogui.prompt("마지막 페이지를 입력해주세요.  ")
pageNum = 1


with open("news.txt","w",encoding="utf8") as news:

    for i in range(1,int(lastpage) * 10, 10) :   #range(시작 ,끝, 단계)
        print(f"\n**********  {pageNum}페이지입니다.  **********\n ")
        response = requests.get(f"https://search.shopping.naver.com/search/all?query=%EC%95%A0%ED%94%8C= + {keyword}&start={i}")
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        links = soup.select(".news_tit")

        news.write(f"{str(date)}의 {keyword}의 언론사 헤드라인입니다. \n\n")
        news.write(f"\n**********  {pageNum}페이지입니다.  **********\n ")
        for link in links:
            title = link.text
            url = link.attrs['href'] #href의 속성값을 가져온다.
            print(title)
            news.write(title + '\n')
        pageNum = pageNum +1