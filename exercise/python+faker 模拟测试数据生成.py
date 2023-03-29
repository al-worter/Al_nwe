''''''
'''
import csv
from faker import Faker
f = Faker(locale='zh-CN')
for i in range(1, 6):
    name = f.name()
    phone = f.phone_number()
    ssn = f.ssn()
    job = f.job()
    print('姓名：%s' % name, '手机号：%s' % phone, '身份证号：%s' % ssn, '工作：%s' % job)
list = Faker()
'''
'''方法一：'''
# -*- coding: utf-8 -*-
# import csv
# from faker import Faker
# import datetime
# file = open("test_data1.csv", "w", newline="")     # 考虑 在with open 的情况下 是否需要 mode = ""  ，encoding = ""
# # 创建文件，分别是文件名、w打开方式(w代表新建，如果已存在，就删除重写)、newline(如果不加，每行数据就会多一空白行)
# fwrite = csv.writer(file)
# # 获取写文件的对象
# fwrite.writerow(["序号", "ID", "姓名","工作","日期","IPv4","邮箱","手机号"])
# # 写入标题头
# for i in range(1, 11):
#     user_id = 'slt' + str(i).zfill(5)
#     # id组成方式：slt00001。str(i)是数字，str.zfill(5)字符串长度5，原字符串右对齐，前面填充0
#     user_name = Faker(locale='zh_CN').name()
#     # Faker生成随机姓名的方法
#     user_work = Faker(locale='zh_CN').job()
#     user_date = Faker(locale='zh_CN').date()
#     user_ipv4 = Faker(locale='zh_CN').ipv4()
#     user_email = Faker(locale='zh_CN').email()
#     user_ipone = Faker(locale='zh_CN').phone_number()
#     fwrite.writerow([i, user_id, user_name,user_work,user_date,user_ipv4,user_email,user_ipone])
#     # 写入一行一行的数据
# file.close()
# 关闭保存文件


'''方法二：'''
from faker import Faker
import xlwt
import sys

def getInformationDict(num):
    InformationDict = {}
    faker = Faker(locale='zh_CN')  # 添加
    for _ in range(int(num)):
        InformationDict[faker.name()] = getInformationList()
    return storedData(InformationDict)

'''创建一个列表，列表中包含各类人物信息'''
def  getInformationList():
    InformationList = []
    faker = Faker(locale='zh_CN')
    InformationList.append(faker.phone_number())
    InformationList.append(faker.date(pattern="%Y-%m-%d", end_datetime=None))
    InformationList.append(faker.province())
    return InformationList

def storedData(InformationDict):
    filename = xlwt.Workbook(encoding='utf-8')
    worksheet = filename.add_sheet('sheet1')
    worksheet.write(0, 0, label="姓名")
    worksheet.write(0, 1, label="电话号码")
    worksheet.write(0, 2, label="生日")
    worksheet.write(0, 3, label="所属省份")
    i = 1
    try:
        for name in InformationDict:
            worksheet.write(i, 0, label=name)
            worksheet.write(i, 1, label=InformationDict[name][0])
            worksheet.write(i, 2, label=InformationDict[name][1])
            worksheet.write(i, 3, label=InformationDict[name][2])
            i = i + 1
    except IndexError:
        return "Error:列表索引超出了取值范围"
    else:
        filename.save('D:\pythonwork\exercise\DataFile.xls')
        return "执行成功"


if __name__ == '__main__':
    num = sys.argv[1]
    print(getInformationDict(num))
