'''import psycopg2
def insertRecord(no,name,dept):
    conn=None
    try:
        conn=psycopg2.connect(database='company',port='5432',user='postgres',password='NANDANI1*POST',host='127.0.0.1')
        cur=conn.cursor()
        query='insert into hr_dept(hr_num,hr_name,hr_dept)\
            values(%s,%s,%s)'
        cur.execute(query,(no,name,dept))
        conn.commit()
        print('total no. of rows inserted:',cur.rowcount);
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
insertRecord(134,'Ronit','Sales')'''
'''from psycopg2.extras import execute_values
def insertRecord(data):
    conn=None
    try:
        conn=psycopg2.connect(database='company',port='5432',user='postgres',password='NANDANI1*POST')
        cur=conn.cursor()
        query='insert into hr_dept(hr_num,hr_name,hr_dept) values (%s)'
        execute_values(cur,query,data)
        conn.commit()
        print('the number of rows inserted',cur.rowcount);
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
insertRecord([(113,'ravi','finance'),(135,'ramesh','sales'),(176,'Ram','sales')])'''

import psycopg2
def delete(num):
    conn=None
    try:
        conn=psycopg2.connect(database='company',\
            user='postgres',password='NANDANI1*POST',port='5432',host='127.0.0.1')
        cur=conn.cursor()
        query='DELETE FROM hr_dept WHERE hr_num=%s'
        cur.execute(query,(num,))
        conn.commit()
        print('Total number of rows deleted',cur.rowcount)
        cur.close()
    except(Exception,psycopg2.DataError) as error:
        print(error)
    finally:
        if conn is not None:      
            conn.close
delete(132)

import psycopg2
def select(f_name):
    conn=None
    try:
        conn=psycopg2.connect(database='lis',\
            user='postgres',password='NANDANI1*POST',port='5432',host='127.0.0.1')
        cur=conn.cursor()
        query='SELECT author_fname,author_lname,isbn_no FROM book_authors WHERE author_fname=%s'
        cur.execute(query,(f_name,))
        row=cur.fetchone()
        print(print('authorFN=',row[0],',authorLN=',row[1],',author_isb_no=',row[2]))
        conn.commit()
        print('Total number',cur.rowcount)
        cur.close()
    except(Exception,psycopg2.DataError) as error:
        print(error)
    finally:
        if conn is not None:      
            conn.close
select('Robert C')


