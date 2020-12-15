from flask import Flask, jsonify, redirect
from flask import request
from flask_session import Session
import random
import randomizer
import redis

app = Flask(__name__)
redis_session = redis.Redis(host='localhost', port=6379, db=0)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)


@app.route('/', methods=['POST'])
def index():
    data = request.form['URI']
    URI = randomizer.randomizer(data)
    redis_session.set(URI, data)

    return "http://localhost:5000/" + URI


@app.route('/<short_url>')
def redirection(short_url):
    URI = redis_session.get(short_url)

    if URI:
        URI = URI.decode("UTF-8")

    if URI:
        return redirect(URI, code=302)
    else:
        return '"status" : "no stored longform url"'


@app.route('/shorten', methods=['POST'])
def alternative_index():
    data = request.headers.get('URI')
    URI = randomizer.randomizer(data)
    redis_session.set(URI, data)

    return "http://localhost:5000/" + URI


if __name__ == '__main__':
    app.run()
