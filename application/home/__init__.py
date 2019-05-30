# -*- coding: utf-8 -*-
from flask import Blueprint, g

home_bp = Blueprint(__name__, 'home')
from .views import index
from .views import article as article_view
from .views import about
from .views import leave
from ...model import user
from ...model import article
from ...model import link
from ...model import attachment


@home_bp.context_processor
def my_context_processor():
    return dict(
        user_info=user.get_user_info(1),
        photo_list=article.get_index_photo(0, 6),
        article_category=article.get_article_category(),
        recommend_list=article.get_recommend_article(),
        friendly_link_list=link.get_friendly_links(),
        follow_info=attachment.get_follow_info(),
        rank_list=article.get_rank_list()
    )
