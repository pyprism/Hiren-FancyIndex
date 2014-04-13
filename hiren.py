__author__ = 'prism'
from flask import Flask ,render_template , request
import movie.imdb as info
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result' , methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        mov = request.form['movie']
        year = request.form['year']
    if year == "":
        return info.searchByTitle(mov)
    else:
        info.titleAndYear(mov,int(year))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)