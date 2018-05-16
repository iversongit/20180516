import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from stu.views import stu

def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(BASE_DIR,"templates")
    static_dir = os.path.join(BASE_DIR,"static")

    app = Flask(__name__,
                template_folder=templates_dir,
                static_folder=static_dir)

    # 将app与蓝图绑定在一起，用于操纵url,并指定url前缀,便于将不同的应用分隔开来
    app.register_blueprint(blueprint=stu,url_prefix="/stu")

    # 访问数据库前的配置(数据库类型，端口、密码等)
    # SQLALCHEMY_DATABASE_URI 配置使用的数据库URL，而配置MySQL的URL格式为
    #    -- mysql://username:password@hostname/database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:5201314@localhost:3306/flask_student'
    # SQLALCHEMY_TRACK_MODIFICATIONS -- 如果设置成 True (默认情况)，
    # Flask-SQLAlchemy 将会追踪对象的修改并且发送信号
    # 这需要额外的内存， 如果不必要的可以禁用它
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 初始化app,将数据库和具体应用绑定在一起
    # 或：将应用置于SQLAlchemy框架下，便于利用orm映射对数据库进行操作
    SQLAlchemy(app=app)
    # db = SQLAlchemy(app)
    return app