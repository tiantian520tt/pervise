#coding:utf-8
import flask, json
from flask import request

version = "699fa638b80ac31d32e9cff8ce6a79e1"
'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)

# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 的路径、请求方式
@server.route('/database/version', methods=['get'])#'get',
def database_version():
    user_version=request.values.get('version')
    if user_version != version:
        return "False"
    else:
        return "True"

@server.route('/database/get_version', methods=['get'])#'get',
def database_get_version():
    return version
    
if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000, debug=True)