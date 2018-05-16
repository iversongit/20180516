from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # 创建/实例化数据库

class Student(db.Model):  # 创建模型
    s_id = db.Column(db.INTEGER,primary_key=True,autoincrement=True) # id -- int类型
    s_name = db.Column(db.String(20),unique=True)  # 定义字段 姓名 -- string类型
    s_age = db.Column(db.INTEGER,default=18) # 年龄 -- int类型

    __tablename__ = 'student'  # 定义表名