from flask import render_template, request
from win32com import client
import os
import pythoncom
from .. import home_bp
from ....model import article


@home_bp.route('/index')
@home_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    keyboard = request.args.get('keyboard', '', type=str)
    article_list, count = article.get_article_pagination_list(page, 13, keyboard, 1)

    return render_template('home/index/index.html', page=page, article_list=article_list, count=count)


@home_bp.route('/officeToPdf')
def office_to_odf():
    pythoncom.CoInitialize()
    doc_name = request.args.get('file')
    pdf_name = doc_name + '.pdf'

    try:
        word = client.DispatchEx("Word.Application")

        if os.path.exists(pdf_name):
            # os.remove(pdf_name)
            return pdf_name

        worddoc = word.Documents.Open(doc_name, ReadOnly=1)
        worddoc.SaveAs(pdf_name, FileFormat=17)
        worddoc.Close()

        return pdf_name
    except:
        return 'translate fail'
