from random import *
'''
number = [1,2,3,4,5] # 리스트 형태의 데이터
shuffle(number) # 데이터 섞기
print(number)
print(sample(number,1))
#총인원: 20명 중 3명을 뽑을 예정 3명의 번호를 화면에 출력해라
total = range(1,21)
total = list(total)
shuffle(total)
print(sample(total,3))
lotto = range(1,46) # 1이상 46미만
lotto = list(lotto)
shuffle(lotto)
print(sample(lotto, 6))
happy_lotto = sample(lotto,6)
print("이번주 로또 당첨 번호는 {} 입니다".format(happy_lotto[0:]))
# 참가인원 : 20명 ,1등 1명, 2등 3명 , 총4명 , 1등 선물: 제주도여행권, 2등 선물 :커피쿠폰
############ 수정필요 set 타입으로
total1 = range(1,21)
total1 = list(total1)
shuffle(total1)
total_1 = sample(total1,1)
#etc_number
total_2 = sample(total1,3)
print("1등은 {} 이고 ".format(total_1[0:]), "2등은 {} 입니다.".format(total_2[0:]))
entry_number = list(range(1,21))
shuffle(entry_number)
print(entry_number)
win1_number = sample(entry_number,1)
etc_number = set(entry_number) - set(win1_number)
win2_number = sample(etc_number,3)
print("추첨결과를 알려드리겠습니다.")
print("1등 제주도여행권은 {}번 이고".format(win1_number), "2등 커피 쿠폰은 {}번 입니다.".format(win2_number))
'''

number_1 = set([1,2,3,4,5,6])
number_2 = set([1,3,5,7,9])

print(number_1 & number_2) # 교집합
print(number_1.intersection(number_2))

print(number_1 | number_2) #합집합
print(number_1.union(number_2))

print(number_1 - number_2) #차집합
print(number_1.difference(number_2))

number_1.add(100)   # 값추가

number_1.remove(6)  # 값삭제