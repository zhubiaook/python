"""
删除FastDFS中过期的图片

Version: 0.1
Author: Slynxes
Date: 2018-12-10
"""
import pymysql
import datetime
from pymongo import MongoClient
import os

now = datetime.datetime.now()
delta = datetime.timedelta(days=10)
n_days = now - delta


def delete_sql():
    conn = pymysql.connect(
        host='mysql.local.com',
        port=3306,
        user='root',
        password='123',
        db='business',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = f'''select local_url, dahua_url, ctime 
        from offline_picture where ctime < '{exp_date}'
        '''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            local_url = row[0]
            ctime = row[2]
            print(f'local_url = {local_url}, ctime = {ctime}')
    except (pymysql.err.OperationalError, pymysql.ProgrammingError,
            pymysql.InternalError, pymysql.IntegrityError, TypeError) as error:
        print('Error: unable to fetch data.')
        print(f'{error}')

    conn.close()


def delete_mongodb():
    conn = MongoClient(
        host='192.168.0.24',
        port=27017,
        # username='',
        # password='',
    )
    db = conn.qirong
    collection = db.offlinePicture.find(
        {'ctime': {'$lt': n_days}},
        {'localUrl': 1, 'ctime': 1}
    )
    for row in collection:
        local_url = row['localUrl']
        path = '/data/fdfs/file/data' + local_url[10:]
        print(path)


if __name__ == '__main__':
    delete_mongodb()
