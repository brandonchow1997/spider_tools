import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL, ' \
      'PRIMARY KEY (id)) '
cursor.execute(sql)
db.close()


def save_to_mysql(info):
    id = 'xxxxxxx'
    user = 'xxx'
    age = 'xxx'

    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
    cursor = db.cursor()
    sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
    try:
        cursor.execute(sql,(id, user, age))
        db.commit()
    except:
        db.rollback()
    db.close()
