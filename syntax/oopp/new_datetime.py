"""
Description

Version: 0.1
Author: slynxes
Date: 2019-01-23
"""
import time as _time


class NewDate(object):
    __slots__ = '_year', '_month', '_day'

    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        t = _time.time()
        return cls.fromtimestamp(t)

    def __repr__(self):
        return "%s.%s(%d, %d, %d)" % (self.__class__.__module__,
                                      self.__class__.__qualname__,
                                      self._year,
                                      self._month,
                                      self._day)
    __str__ = __repr__


class NewDatetime(NewDate):
    __slots__ = NewDate.__slots__ + ('_hour', '_minute', '_second', '_microsecond',
                                     '_tzinfo', '_hashcode', '_fold')

    def __init__(self, year, month, day, hour=0, minute=0, second=0,
                 micresecond=0, tzinfo=None, *, fold=0):
        NewDate.__init__(self, year, month, day)
        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = micresecond
        self._tzinfo = tzinfo
        self._fold = fold

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    @property
    def microsecond(self):
        return self._microsecond

    @property
    def tzinfo(self):
        return self._tzinfo

    @property
    def fold(self):
        return self._fold

    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d, hh, mm, ss)

    @classmethod
    def now(cls):
        t = _time.time()
        return cls.fromtimestamp(t)

    def isoformat(self):
        return "%d-%d-%d %d:%d:%d:%d" % (self._year,
                                         self._month,
                                         self._day,
                                         self._hour,
                                         self._minute,
                                         self._second,
                                         self._microsecond)

    def __repr__(self):
        return "%s.%s(%d, %d, %d, %d, %d, %d)" % (self.__class__.__module__,
                                                  self.__class__.__qualname__,
                                                  self._year,
                                                  self._month,
                                                  self._day,
                                                  self._hour,
                                                  self._minute,
                                                  self._second)

    def __str__(self):
        return self.isoformat()
