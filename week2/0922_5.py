import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

# print(soup.title)
# print(soup.title.get_text()) 타이틀 전체 가져오기
# print(soup.a) #첫번째 a태그 가져오기
print(soup.a.attrs) # a속성 가져오기