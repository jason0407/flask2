import os

#获取当前路径
basedir = os.path.abspath(os.path.dirname(__file__))

#主要的配置文件
class Config:
    #设置SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    #设置为自动提交每次的事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #后面过期内容需要会有警告故增加
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    @staticmethod
    def init_app(app):
        pass

#开发时的配置文件
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

#测试时的配置文件
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-tests.sqlite')

#正式库时的配置文件
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing' : TestingConfig,
    'production':ProductionConfig,

    'default':ProductionConfig
}