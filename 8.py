import sqlite3

connection=sqlite3.connect("Student.db")
cursor=connection.cursor()

#cursor.execute("""CREATE TABLE STUDENTINFO6(SID INT PRIMARY KEY,
  #              NAME VARCHAR(20),
   #             SEM INT,
     #           DOB TEXT)""")

Items=[(5,"A",5,"06-09-2000"),(10,"B",6,"07-10-1999")]

cursor.executemany("INSERT INTO STUDENTINFO6 VALUES(?,?,?,?)",Items)
choice=0
while(choice!=-1):
    print("1.DISPLAY \n 2.SEARCH \n 3.UPDATE \n 4.DELETE -1 to EXIT")
    choice=int(input("Enter choice:"))

    if choice==1:
        cursor.execute("SELECT * FROM STUDENTINFO6")
        tupleA=cursor.fetchall()
        print("SID:","   NAME","   SEM","     DOB")
        for tuple1 in tupleA:
            sid,name,sem,dob=tuple1
            print(sid,"       ",name,"    ",sem,"        ",dob)

    elif choice==2:
        sid1=int(input("ENTER STRUDENTS ID:"))
        li=[]
        li.append(sid1)
        cursor.execute("SELECT SID,NAME,SEM,DOB FROM STUDENTINFO6 WHERE SID=?",li)
        tupleA=cursor.fetchall()
        print("SID:","   NAME","   SEM","     DOB")
        for tuple1 in tupleA:
            sid,name,sem,dob=tuple1
            print(sid,"       ",name,"    ",sem,"        ",dob)

    elif choice==3:
        sid=int(input("Enter old SID:"))
        
        sid1=int(input("Enter updated sid"))
        name1=input("Enter updated name")
        sem1=int(input("Enter updated sem"))
        dob1=input("Enter updated dob")

        li=[sid1,name1,sem1,dob1,sid]
        cursor.execute("UPDATE STUDENTINFO6 SET SID=?,NAME=?,SEM=?,DOB=? WHERE SID=?",li)

    elif choice==4:
        sid=int(input("Enter sid of row to be deleted:"))
        li=[sid]
        cursor.execute("DELETE FROM STUDENTINFO6 WHERE SID=?",li)
    
    
#connection.commit()
cursor.close()

