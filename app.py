import sqlite3
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from draw import URL
import re
import sqlite3
import database

connection = sqlite3.connect('urls.db', check_same_thread=False)
connection.row_factory = sqlite3.Row
curs = connection.cursor()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'This should be a secret random string'

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']
        database.create_table()
        x_url = URL.insert_url(url)
        hasid = hashids.encode(x_url)
        short_url = request.host_url + hasid
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


@app.route('/<id>')
def url_redirect(id):
    original_id = hashids.decode(id)
    original_id = original_id[0]
    url_data = URL.gets_url(original_id)
    new_file=url_data['original_URL']
    return redirect(new_file)



if __name__ == '__main__':
    app.run(port=5800, debug=True)
