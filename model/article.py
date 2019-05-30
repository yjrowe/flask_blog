# -*- coding: utf-8 -*-
import time
from ..common import functions
from .model import Model


def get_index_photo(offset, page_size):
    """获取左侧相册
    :return:
    """
    where = {'a.category_id': 2, 'b.access_key': 'photo'}
    res = Model('article a').join('b_attachment b', 'a.id', 'b.item_id').where(where).group('a.id').limit(offset, page_size).get()

    return res['detail']


def get_article_category():
    """获取文章类型统计
    :return:
    """
    field = 'COUNT(*) as article_num, a.category_title,a.id'
    res = Model('category a').field(field).join('b_article b', 'a.id', 'b.category_id', 'INNER').group('a.id').get()
    return res['detail']


def get_recommend_article():
    """获取推荐文章
    :return:
    """
    res = Model('article').field('id,article_title').where({'is_recommend': 1}).get()
    return res['detail']


def get_rank_list():
    """获取文章点击排行榜列表
    :return:
    """
    res = Model('article').field('id,article_title').where({'status': 1}).order('views DESC').limit(0, 8).get()
    return res['detail']


def get_article_pagination_list(page, page_size, search, category=1):
    """获取文章分页列表
    :param page:
    :param page_size:
    :param search:
    :param category:
    :return:
    """
    where = {}
    where['status'] = 1
    if search:
        where['article_title'] = ['like', '%' + search + '%']
    if category:
        where['category_id'] = category
    offset = (page - 1) * page_size
    print(where)
    field = 'id,article_title,message,is_top'
    article_list = Model('article').where(where).field(field).limit(offset, page_size).order('is_top DESC').get()['detail']

    for article in article_list:
        article['attachment'] = Model('attachment').where({'item_id': article['id'], 'access_key': 'article'}).limit(0, 1).first()['detail']

    count = Model('article').where(where).count('id')

    return article_list, count


def add_article_views(article_id):
    """添加文章点击次数
    :param article_id:
    :return:
    """
    res = Model('article').query('update b_article set views=views+1 where id = %s' % (int(article_id)))
    return res['valid']


def get_article_info(article_id):
    """获取文章信息
    :param article_id:
    :return:
    """
    res = Model('article').where({'id': int(article_id)}).join('b_users', 'b_users.uid', 'b_article.uid').first()
    res['detail']['add_time'] = functions.time_to_str(res['detail']['add_time'])
    return res['detail']


def get_article_tag(article_id):
    """获取文章标签
    :param article_id:
    :return:
    """
    where = {'a.article_id': int(article_id)}
    res = Model('article_tag a').field('b.tag_name').join('b_tag b', 'b.id', 'a.tag_id', 'INNER').where(where).get()
    return res['detail']


def get_last_article(article_id, category):
    """获取上一条文章
    :param article_id:
    :param category:
    :return:
    """
    where = {'status': 1, 'id': ['<', int(article_id)], 'category_id': category}
    res = Model('article').where(where).order('id desc').limit(0, 1).first()
    return res['detail']


def get_next_article(article_id, category):
    """获取下一条文章
    :param article_id:
    :param category:
    :return:
    """
    where = {'status': 1, 'id': ['>', int(article_id)], 'category_id': category}
    res = Model('article').where(where).order('id asc').limit(0, 1).first()
    return res['detail']


def get_article_comments(article_id):
    """获取文章评论列表
    :param article_id:
    :return:
    """
    comments = Model('article_comments').where({'article_id': article_id}).get()['detail']
    count = 0

    for comment in comments:
        comment['add_time'] = functions.time_to_str(comment['add_time'], '%Y-%m-%d %H:%M:%S')
        count += 1

    return comments, count


def get_photo_info(photo_id):
    """获取照片信息
    :param photo_id:
    :return:
    """
    photo_info = Model('article').where({'id': photo_id}).first()['detail']
    photo_info['add_time'] = functions.time_to_str(photo_info['add_time'])
    return photo_info


def get_photo_list_by_photo_id(photo_id):
    """获取图片列表
    :param photo_id:
    :return:
    """
    photo_list = Model('attachment').where({'access_key': 'photo', 'item_id': photo_id}).get()['detail']
    return photo_list


def add_comment(data):
    return Model('article_comments').insert(data)