from flask import Flask, url_for, request
app = Flask(__name__)


# 注册路由
# view function, 视图函数
@app.route('/')
@app.route('/hello')
def index():
    return "<h1>Hello Flask!</h1"


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """
    string:
    int:
    float:
    path: 类似string, 但可以接受斜杠
    uuid: 接受UUID字符串
    """
    return f'Post: {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'

@app.route('/project')
def project():
    return 'The project page'


@app.route('/about/')
def about():
    """
    /about 被重定向为 /about/
    :return:
    """
    return 'The about page'


with app.test_request_context():
    print(url_for('about'))
    print(url_for('show_user_profile', username='zhubiao'))

def do_the_login():
    return 'Post'

def show_the_login():
    return 'Not Post'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login()

