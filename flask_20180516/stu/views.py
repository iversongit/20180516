import random

from flask import Blueprint,render_template,redirect,url_for
from stu.models import Student,db


stu = Blueprint('stu',__name__)

@stu.route('/')
def index():
    return render_template('index.html')

@stu.route('/score/')
def scores():
    scores_list = [21,45,66,77,88,99,76,78]
    content_h2 = '<h2>yeah yeah yeah</h2>'
    content_h3 = '   <h3>oh oh oh</h3>   '
    # scores:为前端页面可以识别的变量名，scores_list为函数中定义的变量
    return render_template("score.html",scores=scores_list,content_h2=content_h2,content_h3=content_h3)

@stu.route('/createtable/')
def create_db():
    db.create_all() # 在指定的数据库中创建表格，数据为空
    return '创建成功'

@stu.route('/droptable/')
def drop_db():
    db.drop_all() # 删除指定数据库中的表
    return '删除成功'

@stu.route('/createstu/')
def create_stu():  # 在数据库中添加信息
    stu = Student()
    stu.s_name = '员工%d' % random.randint(0,1000)
    stu.s_age = '%d' % random.randint(0,20)
    db.session.add(stu) # 将创建的实例添加到数据库对应的表中
    try:
        db.session.commit()
    except:
        # 如果提交不成功，则回滚操作
        db.session.rollback()
    return "创建学生实例成功"

@stu.route('/stulist/')
def stu_all():

    stus = Student.query.all() # 查找到全部学生信息
    return render_template("stulist.html",stus=stus)

@stu.route('/studetail/')
def stu_detail():
    # # sqlalchemy支持原生sql语句
    # sql = 'select * from student where s_name="员工699";'
    # stus = db.session.execute(sql)

    # 使用filter
    # 方法1
    # stus = Student.query.filter(Student.s_name=="员工699")
    # 方法2
    stus = Student.query.filter_by(s_name='员工10')
    return render_template("stulist.html", stus=stus)

@stu.route('/updatestu/') # 修改学生信息
def update_stu():
    # 方法1
    # stu = Student.query.filter_by(s_id=1).first()
    # stu.s_name = "李二狗"
    # db.session.commit()

    # 方法2
    Student.query.filter(Student.s_id==2).update({'s_name':'王小锤'})  # 更新操作不用.first
    db.session.commit()  # 如果没有提交，只会更新浏览器的值(缓存)，而不会更新数据库的值
    return redirect(url_for("stu.stu_all"))

@stu.route('/deletestu/')
def delete_stu():
    stu = Student.query.filter(Student.s_id==1).first()  # -- 不加.first则为BaseQuery数据类型
    db.session.delete(stu)
    db.session.commit()
    return redirect(url_for("stu.stu_all"))