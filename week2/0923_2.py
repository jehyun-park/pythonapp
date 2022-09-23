import requests
from bs4 import BeautifulSoup

with open("webtoon.txt","w",encoding="utf8") as web :
    pageNum = 1
    for i in range(1,6):
        web.write(f"\n\n ***** {pageNum}페이지 입니다. *****\n\n")
        url = f"https://comic.naver.com/webtoon/list?titleId=783053&weekday=tue&page={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"lxml")

        webtoons = soup.find_all("td",attrs={"class": "title"})
    
        for webtoon in webtoons:
                title = webtoon.a.get_text()
                link = "https://comic.naver.com" + webtoon.a["href"]
                web.write(title +"("+ link +")" +"\n")
                #print(title,link)
        pageNum = pageNum + 1


'''
############# 평점 찾기
total_rates = 0
rates = soup.find_all("div",attrs={"class":"rating_type"})


for rate in rates:
    rate_1 = rate.find("strong").get_text()       
    total_rates += float(rate_1)
print(total_rates/len(rates))
'''

'''
with open("rate.txt","w", encoding="utf8") as rating :
    for rate in rates:
        rate_1 = rate.find("strong").get_text()       
        rating.write(rate + "\n") 
'''


