# if문 if조건

'''
score = input("성적을 입력하세요 : ")

if score == "A+" or score == "A":
    print("Good Grade! Loveyourself")

elif score == "B+" or score == "B" :
    print("Normal Grade! I think you will be getB A+ grade next semseter")

elif score == "C+" or score == "C" : 
    print("Bad Grade :( You need to study hard!")

else :
    print("What the hell ! ")

score = int(input("성적을 입력하세요 : "))

if score  >= 90:
    print("Good Grade! Loveyourself")

elif score >= 80 and score <= 89:
    print("Normal Grade! I think you will be get A+ grade next semseter")

else :
    print("Bad Grade :( You need to study hard!")


'''

########## for 반복문 : for 변수 in 반복대상 : 

'''
for i in [1,2,3] :
    print("번호 : {0}".format(i))

for i1 in range(1,101):
    print("다시 번호 : {0}".format(i1))

name = ["도레미", "파솔라", "시도레"]
for name1 in name:
    print("{0}님 하이".format(name1))
'''

########## while문 : 조건이 만족하는 동안 계속 반복

'''
count = 5

while count >= 1 :
    print("번호 {0}번 입니다.".format(count))
    count -=1
    if count == 0:
        print("번호 끝 !")
'''

###### 한줄 for문

number = [1,2,3,4,5]
number = [i + 100 for i in number]
print(number) 

name = ["도레미", "파솔라", "시도레"]
name = [len(i) for i in name]
print(name)