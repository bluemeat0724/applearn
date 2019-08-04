import redis

class Config(object):
    '''配置信息'''

    SECRET_KEY = '0effca18c82e499f8282c619f5dbed71'

    # 数据库连接
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:W@1958113@localhost:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #redis
    REDIS_HOST="127.0.0.1"
    REDIS_PORT=6379

    #flask-session配置
    SESSION_TYPE="redis"
    SESSION_REDIS= redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT) #redis实例连接
    SESSION_USE_SINGER=True #对cookie中的session_id进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400 #session 数据有效期：秒

class DevelopmentConfig(Config):
    """开发模式配置信息"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境配置信息"""
    pass

#构建名字与类的映射关系
config_map={
    "develop":DevelopmentConfig,
    "product:":ProductionConfig
}