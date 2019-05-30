from flask import render_template, request
from .. import home_bp
from ....model import user


@home_bp.route('/about')
def about():
    user_info = user.get_user_info(1)
    return render_template('home/about/index.html', user_info=user_info)
