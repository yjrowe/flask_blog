# -*- coding: utf-8 -*-
from .model import Model


def get_user_info(user_id):
    res = Model('users').where({'uid': user_id}).first()
    return res['detail']