# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/3 下午 08:53
# @Author   : liang yuyu
# @Site     : http://www.cdtest.cn/
# @File     : python ex1.py
# @Software : PyCharm
print('狗仔生疏')
# 基本输出


print('''
排名
成绩
分数
''')
# 多行注释 有三对如右 '''1'''  也可用于print 当中进行多行排列
# 赋值 进行判断
print('.....................................................................')

grade = 60
if grade >= 80:
    print('优秀')
print('不及格')

print('................................................')
# exercise 1
# 用多个print 进行
print('人生若只如初见，')
print('何事秋风悲画扇。')
print('等闲变却故人心，')
print('却道故人心易变。')
# 注销 符号进行打印
print("""
人生若只如初见，
何事秋风悲画扇。
等闲变却故人心，
却道故人心易变。
""")
# 输入某值input 进行打印   grade 分数 ranking 排名
name = input('姓名：')
ranking = input("输入班级排名：")
grade = 99
if grade >= 98:
    print('优秀')
print('不及格')
# print("我的年级分数：",grade),print("我的年级排名：",ranking)
print('您的班级排名：', ranking)
print('您的考试分数：', grade)

print('生日快乐', '2022')
# money = 6
# if money >= 5:
#     print('吃早饭')
# print('直播吃大肥猫,sss')
