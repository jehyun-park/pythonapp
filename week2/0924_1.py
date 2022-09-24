
from itertools import product
import requests
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all?query=tv&cat_id=&frm=NVSHATC"
response = requests.get(url)
response.raise_for_status()
#print("응답코드 :"+ str(response.status_code))

soup = BeautifulSoup(response.text,"lxml")

products = soup.find_all("div",attrs={"class" : "basicList_info_area__TWvzp"})


for product in products :
        #광고 제외
        #ad = product.find("button",attrs={"class":"ad_ad_stk__pBe5A"})

        #if ad:
        #    print("광고제외")
        #    continue
    
        name = product.find("a",attrs={"class": "basicList_link__JLQJf"}).get_text()
        price = product.find("span",attrs={"class":"price_num__S2p_v"}).get_text()
        review = product.find("em",attrs={"class":"basicList_num__sfz3h"})
        link = product.find("a",attrs={"class":"basicList_link__JLQJf"})["href"]
        store = product.find("a",attrs={"class":"basicList_compare__d2bWN"}).get_text()       
    
        if review.get_text() == "0":
            review = "리뷰X"
            
        else :
             review = review.get_text()
        print(f"제품명 : {name}")
        print(f"가격 : {price}")
        print(f"리뷰 : {review}")
        print(f"{store}")
        print(f"바로가기 : {link}")
        print("-"*98)





'''
with open("product.txt","w",encoding="utf8") as prod:

    for product in products :
        name = product.find("a",attrs={"class": "basicList_link__JLQJf"}).get_text()
        price = product.find("span",attrs={"class":"price_num__S2p_v"}).get_text()
        review = product.find("em",attrs={"class":"basicList_num__sfz3h"}).get_text()
        store = product.find("a",attrs={"class":"basicList_compare__d2bWN"}).get_text()
        prod.write("상품명: "+name+"\n"+"가격: "+price+"\n"+"리뷰: "+review+"\n"+store+"\n\n")
'''


