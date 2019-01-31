from flask import Flask
app = Flask(__name__)


# 注册路由
# view function, 视图函数
@app.route('/hi')
@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'
