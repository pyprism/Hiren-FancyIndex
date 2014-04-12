__author__ = 'prism'
from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Hiren"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)