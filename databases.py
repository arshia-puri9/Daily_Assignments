#Databases:
#Q.1
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    print(con)
except sqlite3.DatabaseError as e:
    if con:
        print('Problem ') 
finally:
    con.close()
    print('db created')

#Q.2- 
data=[]
for i in range(1,11):
   # print('Details of student {}'.format(i))
    data.append((input('Name:'),int(input('Marks:'))))

#Q.3-
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query='create table Students(name varchar(15),marks number(3) check (marks>=0 and marks<=100))'
    cursor.execute(query)
    print('CREATED')
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE')
                #Inserting Values
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query='insert into Students (name,marks) values (?,?)'
    cursor.executemany(query,info)
    con.commit()
    print('INSERTED')
    quer="select * from Students"
    cursor.execute(quer)
    data=cursor.fetchall()
    for row in data:
        print("NAME:{} , MARKS:{}" .format(row[0],row[1]))
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('3rd DONE')


#Q.4- Print the names of all the students who scored more than 80 marks.    
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query="select * from Students where marks > 80"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print("NAME:{} , MARKS:{}" .format(row[0],row[1]))
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("Problem occured:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("ALL DONE")



















