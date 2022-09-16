#랜덤함수

from random import *

'''
print(random()) # 0.0 이상에서 1.0 미만의 값 생성
print(random() *10) # 0.0 이상에서 10 미만의 값 생성
print(int(random() * 10))  # 0.0 이상에서 10미만의 정수
print(int(random()*10) +1 ) # 1 이상에서 11 정수

#1~45까지의 정수
print(int(random()*45)+1) #1이상 46미만의 정수 

print(randrange(1,46)) #1부터 46미만의 정수

print(randint(1,45)) #1부터 45이하

date=randint(2,25)
date1=randrange(2,26)

print("이번달 회의 날짜는 " +  str(date) +"일 입니다")
print("이번달 회의 날짜는"+ str(date1) +"일 입니다")
print("이번달 회의 날짜는",date,"일 입니다")

#문자 슬라이싱 변수 [인덱스]

num = "990507-1111111"
print("성별 : " + num[7])

#변수명 [시작인덱스:종료인덱스]

print("연 : " + num[0:2],"  월 : " + num[2:4],"  일 : " + num[4:6])

print("주민등록앞자리는 : " + num[0:6] ," 주민등록뒷자리는 : " + num[7:14])

print("주민등록앞자리는 :" + num[:6], "주민등록뒷자리는 :" +num[7:])

print("주민등록뒷자리는 :" +num[-7:])

#문자열처리함수
text = "Python Java Node.js"
print(text)
print(text.lower()) #소문자
print(text.upper()) #대문자
print(text[0].isupper()) #0번째 인덱스가 대문자?
print(text[1].islower()) #1번쨰 인덱스가 소문자?
print(len(text)) #띄워쓰기포함 문자길이
print(text.replace("Python","Spring")) #Python -> Spring
print(text.count("a"))

text1 = text.index("h") #h의 인덱스
print(text1)
text2 = text.find("h") #h의 인덱스
print(text2)

#둘의 차이점 : 해당인덱스의 값이 없으면 에러가 발생하면서
#index 프로그램 종료
#find -1을 반환하면서 프로그램 계속 수행

#다양한 포맷으로 문자열출력

#출력1
print("저는 %d학년 입니다."%3) # %d : 정수
print("저는 %s에 다닙니다."%"대구가톨릭대학교") # %s : 문자열
print("이번 학기 성적은 %c 입니다."%"A") #%c : 문자
print("저는 %s에 %s를 다닙니다."%("대가대","인빅과"))

#출력2
print("나는 {}학년 입니다.".format(4))
print("저는 {}에 {}를 다닙니다.".format("대가대","인빅과"))
print("저는 {0}에 {1}를 다닙니다.".format("대가대","인빅과"))

#출력3
print("나는 {grade}학년이며,{college}에 다닙니다.".format(grade=4,college="대가대"))
#출력4(파이썬 3.6부터 지원)
grade = 4
college = "대가대"
print(f"나는 {grade}학년이며 {college}에 다닙니다.")
'''

url = "https://www.naver.com"
pass1= url.replace("https://www.","")
pass1=pass1[:5]
print(pass1)
password=pass1[:3] + str(len(pass1)) + str(pass1.count("e")) + "!"
print(password)

print("{}의 비밀번호는 {}입니다.".format(url,password))

pass2 = url[12:15]
password2 = pass2 + str(len(pass1)) + str(pass1.count("e")) + "!"
print(f"{url}의 비밀번호는 {password2}입니다.")

