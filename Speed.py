from time import *
import random as r

def mistake(para,user):
      error=0
      for i in range(len(para)):
            try:
                  if para[i] != user[i]:
                        error=error+1
            except:
                  error=error+1
      return error


def speed_time(Stime,Etime,user):
      time_delay=Etime-Stime
      time_r=round(time_delay,2)
      speed=len(user)/time_r
      return round(speed,2)

while True:
      ck=input("READY TO TEST: YES/NO").upper()
      if (ck=='YES'):
            test=["A for apple",
                  "B for ball",
                  "C for cat"]
            test1=r.choice(test)
#print(test1)
            print("_______*****Typing Speed*****_________")
            print(test1)
            time_1=time()
            print()
            testinput=input("Enter the Text :")
            time_2=time()
            print('Time :',speed_time(time_1,time_2,testinput) , "W/sec")
            print("Error :",mistake(test1,testinput))
      elif (ck=='NO'):
            print("--------THANK YOU-----------------------------")
            break
