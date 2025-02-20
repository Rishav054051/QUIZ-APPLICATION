import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="quiz2")
mycursor=mydb.cursor()

mycursor.execute("CREATE table details (UserId varchar(30),UserName varchar(30))")
mycursor.execute("CREATE table moderator (PASSWORD char(10))")
mycursor.execute("CREATE table quiz (Question varchar(200),Option_A varchar(100),Option_B varchar(100),Option_C varchar(100),Option_D varchar(100),Correct_answer varchar(100),difficulty varchar(10))")

