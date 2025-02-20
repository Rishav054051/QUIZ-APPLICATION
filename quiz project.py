import datetime as dt
import time
import random 
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="quiz")
mycursor=mydb.cursor()





#ADD A QUESTION
def addques():
    Question=input("Enter the ques:-")
    Option_A=input("Enter Option_A:-")
    Option_B=input("Enter Option_B:-")
    Option_C=input("Enter Option_C:-")
    Option_D=input("Enter Option_D:-")
    Correct_answer=input("Enter Correct_Answer:-")
    difficulty=input("enter difficulty:-")
    a="insert into quiz(Question,Option_A,Option_B,Option_C,Option_D,Correct_answer,difficulty) values(%s,%s,%s,%s,%s,%s,%s)"
    b=(Question,Option_A,Option_B,Option_C,Option_D,Correct_answer.lower(),difficulty.lower())
    mycursor.execute(a,b)
    mydb.commit()
    print("QUESTION ADDED")

#RULES
def rules():
    print("-------------------------------")
    print("THE RULES ARE AS FOLLOWS:")
    print("1.THERE ARE LIMITED QUESTIONS.")
    print("2.FOR EVERY QUESTION YOU HAVE TO ENTER ONLY THE CORRECT OPTION AS THE ANSWER.")
    print("3.YOU WILL BE GIVEN FOUR OPTIONS FOR EVERY QUESTION.")
    print("4.THE SCORE WILL BE DISPLAYED AT THE END OF THE QUIZ.")
    print("5.YOU CAN CHOOSE THE DIFFICULTY AS PER YOUR COMFORT.")
    print("-------------------------------")
    print("-------------------------------")

#PLAY QUIZ EASY
def playquizeasy():
    time.sleep(2)
    print("LETS START")
    print("-------------------------------")
    time.sleep(2)
    print("HERE IS UR FIRST QUESTION")
    print("-------------------------------")
    time.sleep(2)
    O=0        
    mycursor.execute("select * from quiz where difficulty='easy'")
    result=mycursor.fetchall()
    random.shuffle(result)    
    for x in result:
        print(x[0])
        print("A.",x[1].capitalize())
        print("B.",x[2].capitalize())
        print("C.",x[3].capitalize())
        print("D.",x[4].capitalize())
        print("-------------------------------")
        f=input("enter your answer as option=")
        if(f.lower()=='a'):
             f=x[1]
        elif(f.lower()=='b'):
             f=x[2]
        elif(f.lower()=='c'):
             f=x[3]
        elif(f.lower()=='d'):
             f=x[4]

        if(f.lower()==x[5].lower()):
            time.sleep(1.5)
            print("CORRECT ANSWER")
            O=O+1
            time.sleep(1)
        else:
            time.sleep(1.5)
            print("INCORRECT ANSWER, THE CORRECT ANSWER IS",x[5])
            time.sleep(1)
    time.sleep(1)
    print("-------------------------------")
    print("YOUR SCORE IS:",O)
    time.sleep(0.5)
    print("-------------------------------")

#PLAY QUIZ MEDIUM
def playquizmedium():
    time.sleep(2)
    print("LETS START")
    print("-------------------------------")
    time.sleep(2)
    print("HERE IS UR FIRST QUESTION")
    print("-------------------------------")
    time.sleep(2)
    O=0      
    mycursor.execute("select * from quiz where difficulty='medium'")
    result=mycursor.fetchall()
    random.shuffle(result)
    for x in result:
         print(x[0])
         print("A.",x[1].capitalize())
         print("B.",x[2].capitalize())
         print("C.",x[3].capitalize())
         print("D.",x[4].capitalize())
         print("-------------------------------")
         f=input("enter your answer as option=")
         if(f.lower()=='a'):
              f=x[1]
         elif(f.lower()=='b'):
              f=x[2]
         elif(f.lower()=='c'):
              f=x[3]
         elif(f.lower()=='d'):
              f=x[4]

         if(f.lower()==x[5].lower()):
             time.sleep(1.5)
             print("CORRECT ANSWER")
             O=O+1
             time.sleep(1)
         else:
             time.sleep(1.5)
             print("INCORRECT ANSWER, THE CORRECT ANSWER IS",x[5])
             time.sleep(1)
    time.sleep(1)
    print("-------------------------------")
    print("YOUR SCORE IS:",O)
    time.sleep(0.5)
    print("-------------------------------")

#PLAY QUIZ HARD
def playquizhard():
    time.sleep(2)
    print("LETS START")
    print("-------------------------------")
    time.sleep(2)
    print("HERE IS UR FIRST QUESTION")
    print("-------------------------------")
    time.sleep(2)
    O=0     
    mycursor.execute("select * from quiz where difficulty='hard'")
    result=mycursor.fetchall()
    random.shuffle(result)
    for x in result:
         print(x[0])
         print("A.",x[1].capitalize())
         print("B.",x[2].capitalize())
         print("C.",x[3].capitalize())
         print("D.",x[4].capitalize())
         print("-------------------------------")
         f=input("enter your answer as option=")
         if(f.lower()=='a'):
             f=x[1]
         elif(f.lower()=='b'):
             f=x[2]
         elif(f.lower()=='c'):
             f=x[3]
         elif(f.lower()=='d'):
             f=x[4]

         if(f.lower()==x[5].lower()):
             time.sleep(1.5)
             print("CORRECT ANSWER")
             O=O+1
             time.sleep(1)
         else:
             time.sleep(1.5)
             print("INCORRECT ANSWER, THE CORRECT ANSWER IS",x[5])
             time.sleep(1)
    time.sleep(1)
    print("-------------------------------")
    print("YOUR SCORE IS:",O)
    time.sleep(0.5)
    print("-------------------------------")

#PLAY QUIZ 
def playquiz():
    difficulty=input("enter difficulty EASY/MEDIUM/HARD:-")
    time.sleep(2)
    print("-------------------------------")
    rules()
    if(difficulty.lower()=='easy'):
        time.sleep(3)
        print("-------------------------------")
        playquizeasy()
    elif(difficulty.lower()=='medium'):
        time.sleep(3)
        print("-------------------------------")
        playquizmedium()
    elif(difficulty.lower()=='hard'):
        time.sleep(3)
        print("-------------------------------")
        playquizhard()
        
#OLD USER
def old():
    userid=input("Enter your roll no. provided by the organization=")
    username=input("enter username=")
    mycursor.execute("select * from details;")
    a=mycursor.fetchall()
    for i in a:
        if(userid in i[0]):
            time.sleep(1)
            print("-------------------------------")
            print("Correct Id")
            time.sleep(0.5)
            print("-------------------------------")
            time.sleep(1)
            playquiz()
            break
        elif (userid not in i[0]):
            time.sleep(1)
            print("Incorrect Id")
            time.sleep(0.5)
            print("-------------------------------")
            time.sleep(1)
            


#OLD USER1

def old1():
    userid=input("Enter your roll no. provided by the organization=")
    username=input("enter username=")
    mycursor.execute("select * from details;")
    a=mycursor.fetchall()
    for i in a:
        if(userid in i[0]):
            time.sleep(1)
            print("-------------------------------")
            print("Correct Id")
            time.sleep(0.5)
            print("-------------------------------")
            time.sleep(1)
            playquiz()



#NEW USER    
def new():
    userid=input("Enter your roll no. to create userid=")
    username=input("enter username=")
    cdate=dt.date.today()
    print("-------------------------------")
    mycursor.execute("select * from details;")
    a=mycursor.fetchall()
    for i in a:
        if(userid in i[0]):
            time.sleep(1)
            print("Id already exist")
            time.sleep(0.5)
            print("-------------------------------")
            time.sleep(2)
            print("Now try entering your Id again")
            print("-------------------------------")
            time.sleep(2)
            old()
        elif (userid not in i[0]):
            a="insert into details(UserId,UserName,LoginDate) values(%s,%s,%s)"
            b=(userid,username.lower(),cdate)
            mycursor.execute(a,b)
            mydb.commit()
            time.sleep(2)
            print("done")
            print("-------------------------------")
            time.sleep(1)
            print("Now enter Username to get access")
            print("-------------------------------")
            old1()

     
#MAIN LOOP
while(1>0):
    print("1 if new user")
    print("2 if old user")
    print("3 to add a question")
    n=int(input("enter choice : "))
    if n==1:
        time.sleep(1)
        print("-------------------------------")
        new()
    if n==2:
        time.sleep(1)
        print("-------------------------------")
        old()
    elif n==3:
        password=input("Enter the password of moderator=")
        mycursor.execute("select * from moderator;")
        a=mycursor.fetchall()
        for i in a:
            if(password==i[0]):
                time.sleep(2)
                addques()
            else:
                time.sleep(2)
                print("Wrong Password")
                time.sleep(1)
                print("Try Again")
                print("-------------------------------")
    
        
        




                


        
