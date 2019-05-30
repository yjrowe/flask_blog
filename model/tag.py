# -*- coding: utf-8 -*-
from .model import Model


def get_tag_cloud():
    """获取标签云列表
    :return:
    """
    res = Model('tag').get()
    return res['detail']


