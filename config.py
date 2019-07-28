class Config(object):
    '''配置信息'''

    SECRET_KEY = '0effca18c82e499f8282c619f5dbed71'

    # 数据库连接
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:W@1958113@localhost:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #redis
    REDIS_HOST="192.168.43.181"
    REDIS_PORT=6379

    #flask-session配置
    SESSION_TYPE="redis"
    SESSION_REDIS=redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USE_SINGER=True #对cookie中的session_id进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400 #session 数据有效期：秒

class DevelopmentConfig(Config):
    """开发模式配置信息"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境配置信息"""
    pass

config_map={
    "develop":DevelopmentConfig,
    "product:":ProductionConfig
}