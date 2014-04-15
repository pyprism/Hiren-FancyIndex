__author__ = 'prism'
from flask import Flask ,render_template , request , jsonify
import movie.imdb as info
import os

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

#for CLI apps
@app.route('/cli-movie',methods=['POST' , 'GET'])
def hiren():
    if request.method == 'POST':
        title = request.form['movie']
        year = request.form['year']
    if year == '':
       nisha = info.searchByTitle(title)
       return jsonify(nisha)
    else:
        nisha = info.titleAndYear(title,year)
        return jsonify(nisha)

#default 404 error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)