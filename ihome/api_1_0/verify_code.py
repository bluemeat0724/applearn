# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import captcha
from ihome import redis_store,constants
from flask import current_app,jsonify,make_response
from ihome.utils.response_code import RET

# GET 127.0.0.1/api/v1.0/image_codes/<image_code_id>
@api.route("image_codes/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取图片验证码
    :return: 正常：验证码图片 异常：json
    """
    # 获取参数
    # 检验参数
    # 业务逻辑处理
      # 生成验证码图片
    name,text,image_data=captcha.generate_captcha()
      # 将验证码真实值保存到redis中,设置有效期
       # 选用字符串进行记录
       # "image_code_编号1": "真实值"
       # "image_code_编号2": "真实值"
    # redis_store.set("image_code_%s"% image_code_id, text)
    # redis_store.expire("image_code_%s"% image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
    # 上面两步骤合并        记录名字                          有效期                    记录值
    try:
        redis_store.setex("image_code_%s"%image_code_id,constants.IMAGE_CODE_REDIS_EXPIRES,text)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(erron=RET.PWDERR,errmsg='save image code id failed')
    # 返回图片
    resp = make_response(image_data)
    resp.headers["Content-Type"] = "image/jpg"
    return resp
    # 返回值


