from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/', methods=['POST', 'GET'])
def name():
    error = None
    if request.method == 'POST':
        result = valid_name(request.form['firstname'], request.form['lastname'])
        if result:
            return render_template('input.html', error=error, url=host, result=result)
        else:
            error = 'invalid user input'
    return render_template('input.html', error=error, url=host)


def valid_name(firstname, lastname):
    connection = sql.connect('database.db')
    connection.execute('INSERT INTO users (firstname, lastname) VALUES (?,?);', (firstname, lastname))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()
