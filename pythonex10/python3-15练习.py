# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/15 17:53
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : python3-15练习.py
# @Software : PyCharm
import re
import pymysql


# 1.连接自己的数据库,进行添加数据,删除数据,修改数据,查询数据的操作.
def python1():
    db = pymysql.connect(
        host='localhost',  # 要连接的主机名字
        port=3306,  # 端口号,必须传入int
        user='root',  # 数据库的用户名
        password='123456',  # 数据库的密码,必须传入字符串
        db='company2',  # 要连接的数据库名
        charset='utf8'  # 指定字符串
    )
    link = db.cursor()  # 使用连接对象，创建游标对象
    # 数据进行增删该改查操作
    link.execute('select * from course2')  # 查询后，所有的查询结果都保存在游标对象里
    link.execute('insert into course values("02","马纠结")')  # 增加内容的操作
    link.execute('delete from course where couid=02')  # 删除操作
    link.execute('update course set couname= "马牛逼" where couid=01 ')  # 修改操作
    db.commit()  # 提交
    link.close()  # 关闭游标对象
    db.close()  # 关闭链接对象


# python1()
# #2.2.验证用户输入的邮箱是否符合规定:
#     邮箱必须以字母开头,6-10位,可以由字母数字或下划线组成,邮箱是@qq或者@163 后缀是.com或者.cn  (提示:或者使用|来匹配)
#     比如 zy123456@qq.com    zy123456@163.com    zy123456@qq.cn   zy123456@163.cn 是符合规定的,
#     zy%##%123@qq.com  zy1234567@aa.com 这种是不符合规定的
# 扩展:
def python2():
    user1 = input('请您输入邮箱地址,例如:zy123456@qq.com,zy123456@163.com :')
    result = re.match(r'[a-z][a-z\d_]{5,8}@(qq|163)\.(com|cn)$', user1)
    if result:
        print('符合规定')
    else:
        print("不符合规定")


# python2()

# 3.设计一个ConnectDB类 拥有三个实例方法,
# 一个是query(查询)  查询方法设置一个形参,接收sql语句,方法实现对sql语句的执行,并返回出所有的查询结果.
# 一个是modify(修改)   修改方法设置一个形参,接收sql语句,方法实现对sql语句的执行,并commit提交.
# 一个是close(关闭)    关闭方法实现关闭游标对象和连接对象.
#
# 实例化对象,调用上面的方法.
class ConnectDB:
    db = pymysql.connect(
        host='localhost',  # 要连接的主机名字
        port=3306,  # 端口号,必须传入int
        user='root',  # 数据库的用户名
        password='123456',  # 数据库的密码,必须传入字符串
        db='company2',  # 要连接的数据库名
        charset='utf8'  # 指定字符串
    )
    link = db.cursor()
    def __init__(self,sql):
        self.sql = sql
    def query(self, sql):
        self.link.execute(sql)
        list1 = self.link.fetchall()
        # self.scroll(0, 'absolute')
        return list1

    def modify(self, sql):
        self.link.execute(sql)
        self.db.commit()

    def close(self):
        self.link.close()
        self.db.close()


cou = ConnectDB(f'select * from emp')
print(cou.query())
cou.close()
cou1 = ConnectDB(f'update course2 set couname = "马大哈" ')
cou.close()


if __name__ == "__main__":
    python1()
    python2()

