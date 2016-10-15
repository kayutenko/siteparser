# -*- coding: utf-8 -*-

try:
    from os import getuid

except ImportError:
    def getuid():
        return 4000

from flask import Flask, render_template
from simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

@app.route("/")
def hello():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(port=getuid() + 1000, debug=True)
