from turtle import update
import pymysql

#데이터베이스 연결

conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password='autoset',
                        db ='dcu',
                        charset = 'utf8')

curs = conn.cursor(pymysql.cursors.DictCursor) #딕셔너리 형태로 결과를 반환 판다스로 데이터프레임 형태로

            ########### 테이블 생성 #######

sql = '''create table boards (
    idx int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title varchar(255),
    name varchar(255),
    email varchar(255),
    memo text,
    wdate varchar(255),
    hit int(11),
    pw varchar(255)
    )
    '''
#sql = "show tables"


              ######### 데이터 입력 ###########
#sql = "insert into user(name,email,phone) values(%s,%s,%s)"

#curs.execute(sql,('jehyun','jehyun@naver.com','010-1111-2222'))
#curs.execute(sql,('je','je@naver.com','010-2222-3333'))
#curs.execute(sql,('hyun','hyun@naver.com','010-3333-4444'))
#curs.execute(sql,('abc','abc@naver.com','010-4444-5555'))
#curs.execute(sql,('def','def@naver.com','010-5555-6666'))
#curs.execute(sql,('ghi','ghi@naver.com','010-6666-7777'))
#curs.execute(sql,('jkl','jkl@naver.com','010-7777-8888'))
#curs.execute(sql,('mnop','mnop@naver.com','010-8888-9999'))

             #########글을 불러내기 ############3

#sql = "select * from user order by name"
curs.execute(sql)
#rows = curs.fetchall() # 모든 데이터를 한번에 가져올때 사용
#rows = curs.fetchone() #하나의 행만 가져올떄 사용
#rows = curs.fetchmany(3) #원하는 행의 수를 가져올때 사용

#conn.commit()  #한번 더 확인 질문 
#print(rows)

#df = DataFrame(rows)
#df = df.to_excel("1004.xlsx")

           ############# 글 수정 ###########

#sql = "update user set phone =%s where name=%s"
#curs.execute(sql,('폰없음','jehyun'))
#conn.commit()           

           ########## 글 삭제 #############

#sql = "delete from user where id = %s"
#curs.execute(sql,(88))
#conn.commit()

            ######### 테이블 삭제 ##########


conn.close()

#for data in curs:
#    print(data)