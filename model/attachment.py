# -*- coding: utf-8 -*-
from .model import Model


def get_follow_info():
    """获取关注图片信息
    :return:
    """
    res = Model('attachment').where({'access_key': 'follow'}).first()
    return res['detail']