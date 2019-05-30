# -*- coding: utf-8 -*-
from .model import Model


def get_friendly_links():
    """获取友情链接列表
    :return:
    """
    res = Model('friendly_link').where({'status': 1}).get()
    return res['detail']