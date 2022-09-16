print("test")

'''
#문자 자료형
print("테스트1")
print("테스트2")

#boolean 자료형
print(5>10)
print(5<10)
print(not(5>10))

#변수 지정
college = "대구가톨릭대학교"   #학교변수지정
department = "소프트웨어학과"  #학과변수지정
grade = 4                     #학년변수지정
'''

#주석처리 한줄일떄는 #으로 처리 여러줄을 한꺼번에 처리할떄는 '''~'''

'''
print("저는" + college +"를 다니고 있고"  + department + "전공입니다")
print("그리고" + str(grade) + "학년 입니다.")

print("저는 ", college,"를 다니고 있고", department, "전공입니다.")
print("그리고", grade,"학년입니다.")

#연산자
print(1+1)
print(5-3)
print(5*2)
print(6/3)

print(2 ** 3) #2의 3제곱
print(5 % 3)  #나머지값
print(5 // 2) #몫
print(10 > 3)
print(4 >=8)
print(10 < 3)
print(5 <= 3)

print(3 == 3) #같다
print(3 + 3 ==6)
print(1 != 3) #같지 않다

print((3>0) and (3>5)) #두 항이 모두 참이면 참
print((3>0) or (3>5)) #두 항중 하나라도 참이면 참
print(not 1 != 3) #반대

#수식
num = 5 + 4 * 3
print(num)
num = num + 2
print(num)

num += 2 #num = num +2
print(num)

num *= 2
print(num)

num /= 2
print(num)

num -=2
print(num)

num %= 2
print(num)
'''

#숫자처리함수
print(abs(-5)) #절대값 5
print(pow(4,2)) #4의 2제곱
print(max(5,10))
print(min(5,10))
print(round(3.14)) #반올림
print(round(3.55))