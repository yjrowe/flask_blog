from flask import render_template, request, jsonify
import time
from .. import home_bp
from ....model import article as article_model


@home_bp.route('/article')
def article():
    article_id = request.args.get('id', 0, type=int)

    if article_id:
        article_model.add_article_views(article_id)
        article_info = article_model.get_article_info(article_id)
        article_tag = article_model.get_article_tag(article_id)
        last_article = article_model.get_last_article(article_id, 1)
        next_article = article_model.get_next_article(article_id, 1)
        article_comments, comment_num = article_model.get_article_comments(article_id)
        return render_template('home/article/detail.html', article_info=article_info, article_tag=article_tag,
                               last_article=last_article, next_article=next_article, article_comments=article_comments,
                               comment_num=comment_num, id=article_id)
    else:
        page = request.args.get('page', 1, type=int)
        article_list, count = article_model.get_article_pagination_list(page, 13, '', 1)
        return render_template('home/index/index.html', article_list=article_list, count=count)


@home_bp.route('/photo')
def photo():
    photo_id = request.args.get('id')

    if photo_id:
        photo_info = article_model.get_photo_info(photo_id)
        photo_list = article_model.get_photo_list_by_photo_id(photo_id)
        last_article = article_model.get_last_article(photo_id, 2)
        next_article = article_model.get_next_article(photo_id, 2)
        article_comments, comment_num = article_model.get_article_comments(photo_id)
        print(len(photo_list))
        return render_template('home/article/photo_info.html', article_info=photo_info, photo_list=photo_list,
                               last_article=last_article, next_article=next_article, article_comments=article_comments,
                               comment_num=comment_num, count=len(photo_list), id=photo_id)
    else:
        photo_list = article_model.get_index_photo(0, 8)

        return render_template('home/article/photo_list.html', photo_list1=photo_list, len=len(photo_list))


@home_bp.route('/comment', methods=['POST'])
def comment_article():
    data = {}
    data['user_name'] = request.form.get('user_name')
    data['article_id'] = request.form.get('article_id')
    data['message'] = request.form.get('message')
    data['add_time'] = str(int(time.time()))

    if article_model.add_comment(data):
        return jsonify({'status': 1, 'message': '添加成功'})
    else:
        return jsonify({'status': 0, 'message': '添加失败'})