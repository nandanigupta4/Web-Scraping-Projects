import psycopg2
def Create_Table():
    conn=None
    try:
        conn=psycopg2.connect(database='company',port='5432',user='postgres',password='NANDANI1*POST',host='127.0.0.1')
        cur=conn.cursor()
        query='create table HR_dept\
            (hr_num int primary key not null,\
                hr_name varchar(50) not null,\
                    hr_dept varchar(50) not null)'
        cur.execute(query)
        conn.commit()
        print('Table created successfully')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
Create_Table()     
