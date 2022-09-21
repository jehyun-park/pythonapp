
import requests
from bs4 import Beautifulsoup


keyword = input("검색어를 입력하세요?")
response = requests.get("https://search.naver.com/search.naver?where=news&query=%EB%84%A4%EC%9D%B4%EB%B2%84&sm=tab_opt&sort=2&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0" + keyword)
html = response.text
soup = Beautifulsoup(html,'html.parser')
links = soup.select_one(".news_tit")
for link in links :
    print(link.text)
    title = link.text
    url = link.attrs['href'] #href의 속성값을 가져온다
    print(title,url)