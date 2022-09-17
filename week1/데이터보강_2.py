import pickle

with open("week1/profile.pickle","rb") as profile_file :
    print(pickle.load(profile_file))

with open("week1/test.txt","w",encoding="utf8") as test_file:
    test_file.write("테스트 문장입니다.")        ## close() 사용 하지않아도 됨

with open("week1/test.txt", "r", encoding="utf8") as test_file :
    print(test_file.read())







