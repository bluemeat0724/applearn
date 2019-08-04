# coding:utf-8
from flask import Flask
from config import config_map#导入初始化映射
from flask_sqlalchemy import SQLAlchemy
# 解决数据库编码问题1366错误 https://www.cnblogs.com/shiqi17/p/9409228.html
import pymysql
import mysql.connector

from flask_session import Session#用于将session书保存到redis中，见config
from flask_wtf import CSRFProtect

import logging
from logging.handlers import RotatingFileHandler
import redis
from ihome.utils.commons import ReConverter

#创建数据库对象
db = SQLAlchemy()

#创建Redis连接对象
redis_store=None


# 配置日志信息

# 设置日志的记录等级
logging.basicConfig(level=logging.INFO)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)

# 工厂模式函数，用于根据不同运行场景，调用 开发-生产 启动模式
def create_app(config_name):
    """
    按参数判断项目启动模式，创建flask应用对象
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
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask-session,将session数据保存到redis中
    Session(app)

    # 补充csrf防护
    # CSRFProtect(app)

    # 为flask添加自定义转换器
    app.url_map.converters["re"]=ReConverter

    # 注册蓝图
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    # 注册提供静态文件的蓝图
    from ihome import web_html
    app.register_blueprint(web_html.html)

    return app