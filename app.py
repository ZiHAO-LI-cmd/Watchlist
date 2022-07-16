from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)


@app.route('/')         # 为这个函数绑定对应的 URL
@app.route('/index')
@app.route('/home')
def hello():  # 返回值作为响应的主体，默认会被浏览器作为 HTML 格式解析
    return 'Hello'
    # return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):                # 在视图函数里获取到<name>
    return f'User: {escape(name)}'  # escape() 函数对 name 变量进行转义处理

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'

if __name__ == '__main__':
    app.run()
