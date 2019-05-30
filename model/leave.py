# -*- coding: utf-8 -*-
from .model import Model
from ..common import functions
import time


def get_leave_list():
    """获取留言列表
    :return:
    """
    where = {'status': 1}
    leave_list = Model('leave_word').where(where).order('create_time DESC').get()['detail']
    for leave in leave_list:
        leave['create_time'] = functions.time_to_str(leave['create_time'])
    return leave_list


def add_leave(data):
    """添加留言
    :param data:
    :return:
    """
    data['create_time'] = str(int(time.time()))
    res = Model('leave_word').insert(data)
    return res


def reply(leave_id, reply):
    """回复留言
    :param leave_id:
    :param reply:
    :return:
    """
    res = Model('leave_word').update({'id': leave_id}, {'reply': reply})
    return res