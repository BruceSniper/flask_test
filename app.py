from flask import Flask
from flask import request

# 工厂模式：是一个很常用的用于创建对象的设计模式
app = Flask(__name__)

# (1) 实现 api，并且演示 api的get， post， 以及request里的param， query， body
# (2) 数据库实例的创建，利用工厂模式去创建flask这个实例，下一期会讲crud操作

# https://flask.palletsprojects.com/en/1.1.x/tutorial/database/

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/name', methods=['GET', 'POST'])
def get_name():
    if request.method == 'POST':
        return 'luotuo from POST'
    else:
        return 'luotuo from GET'


@app.route('/fans')
def get_fans():
    return '10000'


# 用户资料endpoint
@app.route('/userProfile', methods=["GET", "POST"])
def get_profile():
    if request.method == 'GET':
        name = request.args.get('name', '')
        print(name)
        if name == 'luotuo':
            return dict(name='luotuo from GET', fans=100000)
        else:
            return dict(name='bushi luotuo from GET', fans='1000000')

    elif request.method == 'POST':
        print(request.form)
        print(request.data)
        print(request.json)
        name = request.json.get('name')
        if name == 'luotuo':
            return dict(name='luotuo from POST', fans=100000)
        else:
            return dict(name='bushi luotuo from POST', fans='1000000')
    return '1'
    # return 'name:luotuo, fans: 100000'


if __name__ == '__main__':
    app.run()
