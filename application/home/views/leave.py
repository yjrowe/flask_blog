from flask import render_template, request, jsonify, redirect, url_for
import time
from .. import home_bp
from ....model import leave as leave_model


@home_bp.route('/leave', methods=['GET', 'POST'])
def leave():
    if request.method == 'GET':
        leave_list = leave_model.get_leave_list()
        return render_template('home/leave/index.html', leave_list=leave_list)
    else:
        data = {}
        data['user_name'] = request.form.get('user_name')
        data['email'] = request.form.get('email')
        data['content'] = request.form.get('content')
        res = leave_model.add_leave(data)
        if res is True:
            return redirect('/leave')
        else:
            return jsonify('留言失败')