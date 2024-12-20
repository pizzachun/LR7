
import sqlite3

def getConnection():
    return sqlite3.connect('base.db')

def getCursor(connect):
    return connect.cursor()

def fillDB(connect):
    cur=connect.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS user(
        fio TEXT,
        gift TEXT,
        price INTEGER,
        status TEXT
    );
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Иванов Иван', 'часы', 500, 'yes');
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Петров Петр', 'ручка', 600, 'yes');
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Сидоров Александр', 'мяч', 700, 'yes');
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Александров Иван', 'Термокружка', 650, 'yes');
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Романов Роман', 'Книга', 550, 'yes');
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Григорьев Григорий', 'Термос', 450, 'yes');
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Дмитриев Дмитрий', 'Свитер', 500, 'yes');
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Данилов Данил', 'шахматы', 670, 'yes');
                ''')
    cur.execute('''
                INSERT INTO user(fio, gift, price, status)
                VALUES ('Николаев Николай Petr', 'Парфюм', 590, 'yes');
                ''')
    connect.commit()



def getResult(connect):
    sql = 'SELECT * FROM user;'
    cur =connect.cursor()
    cur.execute(sql)
    myresult = cur.fetchall()
    print(myresult)
    return myresult

def closeConnection(connect):
  if connect is not None:
    connect.commit()
    connect.close()
  return True

