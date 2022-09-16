#####리스트

'''
num1 = 10
num2 = 20
num3 = 30
num_1 = [10,20,30,15,25]
num_1.sort() #정렬
print(num_1)
num_1.reverse()
print(num_1)
num_1.clear()
print(num_1)
date_1 = [401,"Node",777,"JSP"]
print(date_1)
pg = ["Node.js","PHP","Java"]
print(pg)
print(pg.index("Java"))
pg.append("Python") #데이터 끝에 추가
print(pg)
pg.insert(1,"Oracle") # 인덱스 위치에 데이터 추가
print(pg)
pg.pop() #맨뒤부터 데이터 삭제 
print(pg)
pg.append("PHP")
print(pg)
print(pg.count("PHP"))
'''

#####사전 : key, value

'''
member = {1 : "홍길동", 2 : "길동"}
print(member[2])       # 키 값 호출
print(member[1])       # 값이 없으면 프로그램 종료
print(member.get(3))   # None을 발생하고 프로그램 계속 실행
print(3 in member)     # 값이 있는지 여부 확인 /False
print(1 in member)     # True
member1 = {"A" : "홍길동", "B" : "길동"}
print(member1["A"])
member1["C"] = "도레미"
print(member1["C"])
print(member1.keys())
print(member1.values())
print(member1.items())
del member1["C"]       # 해당되는 키 삭제
member1.clear()        # 전체 삭제
print(member1)
#####튜플   :  수정,삭제 불가능 !!!  - 리스트보다 데이터 처리 속도는 빠름
member2 = ("도레미","파솔라")
print(member2[0])
print(member2[1])
name = "시도레"
colleage = "DCU"
grade = 3
(name, colleage, grade) = ("시도레","DCU", "3")
print(name, colleage, grade)
'''

#####세트             :  중복된 값 허용하지 않음 !!

number_1 = {1,2,3,1,1}
print(number_1, type(number_1))
number_1 = tuple(number_1)
print(number_1,type(number_1))

number_1 = set(number_1)
print(number_1,type(number_1))


number_2 = set({1,3,2,3,2})
print(number_2)