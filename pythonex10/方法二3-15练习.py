# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 9:54
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-15练习.py
# @Software : PyCharm


# 1.连接自己的数据库,进行添加数据,删除数据,修改数据,查询数据的操作.
import pymysql
db = pymysql.connect(
        host='localhost',  # 要连接的主机名字
        port=3306,  # 端口号,必须传入int
        user='root',  # 数据库的用户名
        password='123456',  # 数据库的密码,必须传入字符串
        db='company2',  # 要连接的数据库名
        charset='utf8'  # 指定字符串
)
link = db.cursor()
link.execute('insert into course values("02","马纠结")')  # 增加内容的操作
link.execute('insert into course values("33","马大哈")')  # 增加内容的操作
link.execute('insert into course values("04","马哈哈")')  # 增加内容的操作
# link.execute('delete from course where couid=03')  # 删除操作
# link.execute('update course set couname= "马牛逼" where couid=01 ')  # 修改操作
db.commit()
link.execute('select * from course2')
print(link.fetchall())
link.close()
db.close()


# #2.2.验证用户输入的邮箱是否符合规定:
#     邮箱必须以字母开头,6-10位,可以由字母数字或下划线组成,邮箱是@qq或者@163 后缀是.com或者.cn  (提示:或者使用|来匹配)
#     比如 zy123456@qq.com    zy123456@163.com    zy123456@qq.cn   zy123456@163.cn 是符合规定的,
#     zy%##%123@qq.com  zy1234567@aa.com 这种是不符合规定的
# 扩展:





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
    def query(self,sql):
        self.link.execute(sql)  # 先执行sql语句
        return self.link.fetchall() # 再返回查询的所有内容.
    def modify(self,sql):
        self.link.execute(sql)
        self.db.commit()    # 提交.

    def close(self):
        self.link.close()
        self.db.close()

conn = ConnectDB()
# conn.modify('insert into course values("09","牛大哄")')
# print(conn.query('select * from course'))
conn.modify('delete from course where couid=04')
print(conn.query('select * from course'))




# 1.连接自己的数据库,进行添加数据,删除数据,修改数据,查询数据的操作.
import pymysql
# db = pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='123456',
#     db='hzdl_company',
#     charset='utf8'
# )
# link = db.cursor()
# link.execute('insert into userinfo values("xiaozhou1","123456")')
# link.execute('update userinfo set password="888888" where username="xiaozhou"')
# link.execute('delete from userinfo where username="xiaozhou"')
# db.commit()
# link.execute('select * from userinfo')
# print(link.fetchall())
# link.close()
# db.close()
# 2.验证用户输入的邮箱是否符合规定:
#     邮箱必须以字母开头,6-10位,可以由字母数字或下划线组成,邮箱是@qq或者@163 后缀是.com或者.cn  (提示:或者使用|来匹配)
#     比如 zy123456@qq.com    zy123456@163.com    zy123456@qq.cn   zy123456@163.cn 是符合规定的,
#     zy%##%123@qq.com  zy1234567@aa.com 这种是不符合规定的
# email = input('输入邮箱:')
# import re
# if re.match(r'[a-z][a-z\d_]{5,9}@(qq|163)\.(com|cn)$',email):
#     print('ok')
# else:
#     print('faild')

# 扩展:
# 3.设计一个ConnectDB类 拥有三个实例方法,
# 一个是query(查询)  查询方法设置一个形参,接收sql语句,方法实现对sql语句的执行,并返回出所有的查询结果.
# 一个是modify(修改)   修改方法设置一个形参,接收sql语句,方法实现对sql语句的执行,并commit提交.
# 一个是close(关闭)    关闭方法实现关闭游标对象和连接对象.
# 实例化对象,调用上面的方法.
class ConnectDB:
    def __init__(self,db_name): # 把要连接的数据库作为形参
        self.db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db=db_name,
        charset='utf8'
        )
        self.link = self.db.cursor()
    # def query(self,sql):
    #     self.link.execute(sql)  # 先执行sql语句
    #     return self.link.fetchall() # 再返回查询的所有内容.
    #
    # def modify(self,sql):
    #     self.link.execute(sql)
    #     self.db.commit()    # 提交.
    def execute_sql(self,sql):
        self.link.execute(sql)  # 先执行,
        if sql.startswith('select'):    # 判断传入的sql语句是以select开头的话.
            return self.link.fetchall() # 就返回读取的所有内容
        else:
            self.db.commit()    # 如果不是查询语句,就提交.
    def close(self):
        self.link.close()
        self.db.close()

conn = ConnectDB('hzdl_company')
# conn.modify('insert into userinfo values("xiaozhou2","123456")')
# print(conn.query('select * from userinfo'))
print(conn.execute_sql('select * from userinfo'))
# conn.execute_sql('insert into userinfo values("xiaozhou3","123456")')
# conn.close()