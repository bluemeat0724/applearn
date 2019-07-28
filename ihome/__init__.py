# coding:utf-8
from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
# 解决数据库编码问题1366错误 https://www.cnblogs.com/shiqi17/p/9409228.html
import pymysql
import mysql.connector

from flask_session import Session
from flask_wtf import CSRFProtect


import redis


#创建数据库对象
db = SQLAlchemy()

#创建Redis连接对象
redis_store=None

# 工厂模式
def create_app(config_name):
    """
    安参数判断项目启动模式，创建flask应用对象
    :param config_name:str 配置模式名字 （”develop","product")
    :return:
    """
    app = Flask(__name__)
    #根据配置模式名字获取配置参数类
    config_class=config_map.get(config_name)
    app.config.from_object(config_class)
    #使用app初始化db
    db.init_app(app)

    #初始化redis工具
    globals redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask-session,将session数据保存到redis中
    Session(app)

    # 补充csrf防护
    CSRFProtect(app)

    #注册蓝图
    from ihome import api_1_0
    app.register_blueprint(api_1_0,url_prefix="/api/v1.0")

    return app