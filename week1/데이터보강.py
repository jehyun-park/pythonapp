####### pickle
import pickle

'''
profile_file = open("profile.pickle","wb") #바이너리 형식으로 저장
profile = {"이름 : 박제현", "나이 : 24", "학과 : 인빅"}

print(profile)
pickle.dump(profile,profile_file)
profile_file.close()

'''

profile_file = open("week1/profile.pickle","rb")   # rb : 읽어들임
profile = pickle.load(profile_file)

print(profile)
profile_file.close()








