from ihome import db, models
import logging
# from flask import current_app, request

from . import api

@api.route("/index")
def index():
    logging.error('')  # 错误级别
    logging.warning('')  # 警告级别
    logging.info('')  # 消息级别
    logging.debug('')  # 调试级别

    return "index page"
