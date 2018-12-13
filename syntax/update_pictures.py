"""
判断FastDFS中图片是否存在，
存在则更新MongoDB中recPersonnelRecord中download为3

Version: 0.1
Author: zhubiao
Date: 2018-12-13
"""
import os
import datetime
from pymongo import MongoClient


def update_picture(last_time):
    """
    图片若在文件系统中存在，则跟新download为3
    :param last_time: 时间戳
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
    offline_picture = db.offlinePicture.find(
        {'ctime': {'$gt': last_time}},
        {'localUrl': 1, 'ctime': 1, 'dahuaUrl': 1}
    )

    for row in offline_picture:
        local_url = row['localUrl']
        file = '/data/fdfs/file/data' + local_url[10:]
        if os.path.isfile(file):
            db.recPersonnelRecord.update_many(
                {'pictureUrlCatch': row['dahuaUrl']},
                {'$set': {'download': 3}}
            )


if __name__ == '__main__':
    now = datetime.datetime.now()

    # hours设置距离当前多少个小时
    delta = datetime.timedelta(hours=2)
    r_last_time = now - delta
    update_picture(r_last_time)
