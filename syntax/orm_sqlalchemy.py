"""
SQLAlchemy Exercise

Help:
    https://blog.csdn.net/u012762054/article/details/78403794
Version: 0.1
Author: Slynxes
Date: 2018-12-12
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Table, MetaData, Time
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine("mysql+pymysql://root:123@192.168.0.200:3306/mydb",
                       encoding='utf-8', echo=True)

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('password', String(12))
             )


offline_picture = Table('offline_picture', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('local_url', String(200)),
                        Column('dahua_url', String(200)),
                        Column('ctime', Time),
                        Column('mtime', Time)
                        )


class User(object):
    def __init__(self, name, id, password):
        self.id = id
        self.name = name
        self.password = password


class Offline_Picture(object):
    def __init__(self, id, local_url, dahua_url, ctime, mtime):
        self.id = id
        self.local_url = local_url
        self.dahua_url = dahua_url
        self.ctime = ctime
        self.mtime = mtime


mapper(User, user)
mapper(Offline_Picture, offline_picture)
Sessing_class = sessionmaker(bind=engine)
Session = Sessing_class()
user_obj = User(id=2, name="zhubiao", password="123456")
Session.add(user_obj)
Session.commit()



