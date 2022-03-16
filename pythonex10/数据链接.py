# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/15 14:22
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 数据链接.py
# @Software : PyCharm
'''
# 连接数据库的步骤
#     1)：如果是第一次使用，需要下载安装第三方库pymysql
#       下载方式有两种：1 ,在pychram里面设置-项目-搜索 pymysql 下载，
#       2.在cmd窗口命令：pip install pymysql下载。
      2).导入pymysql  .import pymysql
      3)使用connect方法创建一个连接对象.
      4.使用连接对象,调用cursor方法创建一个游标对象
      5.使用连接对象,调用execute方法执行sql语句.
      6).查询语句:需要fetchall()  ,fetchone(),fetchmany()去读取所有的内容
      7)关闭游标对象link.close(),关闭连接对象db.close().
'''
# 使用数据库    把def函数去掉后需要取消缩进 内容
import re

import pymysql  # 导入pymysql
# 创建连接对象
def conect_db(sql):
    db = pymysql.connect(
        host='localhost',  # 要连接的主机名字
        port=3306,  # 端口号,必须传入int
        user='root',  # 数据库的用户名
        password='123456',  # 数据库的密码,必须传入字符串
        db='company2',  # 要连接的数据库名
        charset='utf8'  # 指定字符串
    )

    # 使用连接对象，创建游标对象
    link = db.cursor()

    # 使用游标对象执行sql语句
    link.execute(sql)  # 查询后，所有的查询结果都保存在游标对象里

    # 使用游标读取查询结果
    # print(link.fetchall())  # 读取所有结果。       查询 操作
    # print('----------------------------------------------')
    # link.scroll(0, 'absolute')
    # print(link.fetchone())  # 读取一行内容  . 由于 它读取到游标指针是到最后一行，已经无法读取需要加上.scroll
    # print(link.fetchmany(1))  # 指定读取多行内容。

    # 对数据库进行修改操作 例如 增删改
    # link.execute('insert into course values("02","马纠结")')    # 增加内容的操作
    # link.execute('delete from course where couid=02')   # 删除操作
    # link.execute('update course set couname= "狗崽子" where couid=01 ')  # 修改操作

    # 用户输入数据,进行插入
    # couid = input('请输入id:')
    # couname = input('请输入名字:')
    # link.execute(f'insert into course values("{couid}","{couname}")')
    # print(f'insert into course values("{couid}","{couname}")')    # 如果使用变量来插入数据，一定要在变量外面再套一层引号.

    # 1.从userinfo 表中读取所有数据，并且插入到userinfo_copy表中。
    # link.execute('select * from course')
    # all = link.fetchall()  # 把读取出来的所有结果保存到all变量中
    # print(all)   # f返回的是元组嵌套元组
    # 2. 将数据插入到userinfo_copy表中 .    %s 将所有字符串 、数字、等类型都占位
    # executemany 需要传入两个参数，第一个参数是格式化的sql语句，语句里面全部使用%s进行占位，不需要区分数据类型.第二个参数就是要插入的数据。
    # link.execute('insert into '输入表名' values(%s,%s) 有几个变量就用多少个变量',all)   #  #适用于需要一次性插入—个元组嵌套元组的场景.

    # 对刚才的修改操作进行提交
    db.commit()  # 用链接对象进行提交. 插入后 需要给内容提交

    link.callproc('t77')   #使用游标对象,请调用callproc()方法执行存储过程
    print(link.fetchall())  # 查看结果

    # 关闭游标对象，
    link.close()

    # 关闭链接对象
    db.close()

    # 练习:用户输入账号名和密码,先判断账号名用正则判断是否是6-10位的纯字母,
    # 如果是,再提示用户输入密码.判断密码是否是6-10位的纯数字,
    # 如果满足,则把用户输入的数据插入到userinfo表中,(在数据库提前建好这张表.)
# couid = input('请输入您的账号:')
# result = re.findall(r"[a-z]{6,10}$", couid, re.I)
# if result:
#     password = input('请输入您的密码:')
#     if re.match(r"\d{6,10}$", password):
#         conect_db(f'insert into course2 values("{couid}","{password}")')
#         print('注册成功')
#     else:
#         print('密码必须是6-10纯数字！')
# else:
#     print('输入失败,检查是否满足账号是否满足6-10位，由纯字母组成')
