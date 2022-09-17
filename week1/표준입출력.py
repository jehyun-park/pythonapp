###### 표준입출력

'''
print("Python", "Java")
print("Python" + "Java")

print("Python", "Java", sep=",")  #sep : 문장사이 삽입
print("Python", "Java", "Node", sep=" vs ",end =" ") # end : 이어서 쓰기
print("당신의 선택은?!")

scores = {"php" : 0, "Java" : 90, "Python" : 100} #튜플형태의 데이터
for i, score in scores.items() :
    print(i.ljust(6) ,str(score).rjust(3) ,sep=": ")  # ljust : left 정렬 , rjust : right 정렬

for num in range(1,21) :
    print("번호 : " + str(num).zfill(3))

'''
####### 파일입출력

'''
book_file = open("book.txt","w",encoding="utf8") # 파일 쓰기모드 열기   # w : 쓰기
print("Node : 5000won", file=book_file)
print("Java : 10000won", file=book_file)
book_file.close()  

book_file = open("book.txt","a", encoding="utf8")                      # a : 수정
book_file.write("Php : 15,000won")
book_file.write("\nC# : 12,000won")
book_file.close()
book_file = open("book.txt","r",encoding="utf8")                       # r : 읽기
#print(book_file.read())     # 전체 읽어오기

print(book_file.readline(),end="")  # 한줄씩 읽어오기, end : 한 칸 위로 올림
print(book_file.readline())

book_file.close()


book_file = open("book.txt","r" ,encoding="utf8")
while True :
    line = book_file.readline()
    if not line : 
        break               #반복문 탈출
    print(line, end="")
book_file.close()
'''

book_file = open("week1/book.txt","r" ,encoding="utf8")
lines = book_file.readline() #모든 줄을 들고와서 리스트형태로
for line in lines:
    print(line,end="")
book_file.close()









