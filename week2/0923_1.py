from cgitb import text
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

'''
print(soup.title)
print(soup.title.get_text()) 타이틀 전체 가져오기
print(soup.a) #첫번째 a태그 가져오기
print(soup.a.attrs)  a속성 가져오기
print(soup.a["href"])
print(soup.find("a",attrs={"class":"Nbtn_upload"}).get_text())

rank1 = soup.find("li",attrs={"class":"rank01"})
print(rank1.a.get_text())

rank2 = rank1.next_sibling.next_sibling   
print(rank2.a.get_text())

rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2_1 = rank3.previous_sibling.previous_sibling
print(rank2_1.a.get_text())

print(rank1.parent) #li rank01의 부모부터 출력해달라 !

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank1_1 = rank2.find_previous_sibling("li")
print(rank1_1.a.get_text())
'''
titles = soup.find_all("a",attrs={"class":"title"})

with open("naver_webtoon.txt","w",encoding="utf8") as naver :

        naver.write("********** 네이버에서 연재중인 웹툰 목록입니다. **********\n\n")
            
        for title in titles :   
            naver.write(title.get_text() + "\n")
