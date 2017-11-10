#coding=utf-8
import os
from flask import Flask, request, g, redirect, url_for, abort, \
     render_template, flash
import json
from datetime import timedelta,datetime
import redis

app = Flask(__name__)
r = redis.Redis(host='127.0.0.1', port=6379)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='gugugu'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    data = request.form['address']
    time = datetime.ctime(datetime.now())
    r.set(time, data)
    record = '{}:{}'.format(time, r.get(time))
    return render_template('index.html', record=record)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
