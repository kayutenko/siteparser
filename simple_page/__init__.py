# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

simple_page = Blueprint('simple_page', __name__, template_folder="templates", static_folder='static')

# app = Flask(__name__)

@simple_page.route("/simple_page")
def hello():
    return render_template('page.html')

if __name__ == "__main__":
    simple_page.run(port=getuid() + 1000, debug=True)
