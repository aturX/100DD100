import logging

from flask import Flask, flash, redirect, render_template, \
     request, url_for

"""
1. WSGI 容器 Gunicorn （服务器）

$ pip install gunicorn
  $ cat myapp.py
    def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
  $ gunicorn -w 4 myapp:app
  [2014-09-10 10:22:28 +0000] [30869] [INFO] Listening at: http://127.0.0.1:8000 (30869)



"""


app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    app.logger.debug('日志 debugging')
    app.logger.warning('日志 warning  ')
    app.logger.error('日志 error')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            # 类似java ModelAndView
            # 模板中 使用 get_flashed_messages()   接收 信息
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    handler = logging.FileHandler('flask.log')
    app.logger.addHandler(handler)
    # debug 基本日志 不显示
    app.logger.debug('日志 debugging')
    app.logger.warning('日志 warning  ')
    app.run(host="0.0.0.0", port="6666")

