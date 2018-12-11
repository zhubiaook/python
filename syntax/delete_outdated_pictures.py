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


def delete_sql(exp_date, now_str):
    """
    从MySQL中读取图exp_days天前的图片路径
    判断该图片是否存在，存在则删除
    记录日志
    :param exp_date:
    :param now_str:
    :return:
    """
    conn = pymysql.connect(
        host='mysql.local.com',
        port=3306,
        user='USER',
        password='PASSWORD',
        db='DATABASE',
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
            file = '/data/fdfs/file/data' + local_url[10:]
            if os.path.isfile(file):
                os.remove(file)
                content = now_str + ' ' + file
                write_log('/data/fdfs/logs/remove.log', content)
    except (pymysql.err.OperationalError, pymysql.ProgrammingError,
            pymysql.InternalError, pymysql.IntegrityError, TypeError) as error:
        print('Error: unable to fetch data.')
        print(f'{error}')
    conn.close()


def delete_mongodb(exp_days, now_str):
    """
    从MongoDB中读取图exp_days天前的图片路径
    判断该图片是否存在，存在则删除
    记录日志
    :param exp_days:
    :param now_str:
    :return:
    """
    conn = MongoClient(
        host='mongo.local.com',
        port=27017,
        # username='USER',
        # password='PASSWORD',
        # authSource='admin',
        # authMechanism='SCRAM-SHA-256'
    )
    db = conn.qirong
    collection = db.offlinePicture.find(
        {'ctime': {'$lt': exp_days}},
        {'localUrl': 1, 'ctime': 1}
    )
    for row in collection:
        local_url = row['localUrl']
        file = '/data/fdfs/file/data' + local_url[10:]
        if os.path.isfile(file):
            os.remove(file)
            content = now_str + ' ' + file
            write_log('/data/fdfs/logs/remove.log', content)


def write_log(log_path, content):
    """
    记录日志
    :param log_path:
    :param content:
    :return:
    """
    with open(log_path, 'a') as fpo:
        fpo.write(content + '\n')


if __name__ == '__main__':
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=10)
    r_exp_days = now - delta
    r_now_str = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    delete_mongodb(r_exp_days, r_now_str)
