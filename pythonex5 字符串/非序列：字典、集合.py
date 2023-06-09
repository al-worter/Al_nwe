# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/10 15:21
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 非序列：字典、集合.py
# @Software : PyCharm

# 8.1 非序列： 字典   dict={}
# 字典是可变的非序列数据结构，没有index 索引，存储的都是键key 和值value构成的值对
#  key键不能重复 ，而值value 可以有重复


dict1 = {
    '姓名': '姚明',
    '身高': 2.26,
    '体重': 120
}
print(dict1['身高'])
print(dict1['姓名'])

dict2 = {
    '刘翔': {
        '年龄': 45,
        '身高': 2.26,
        '体重': 120
    },
    '詹姆斯': {
        '年龄': 55,
        '身高': 2.11,
        '体重': 140
    }
}

print(dict2['刘翔']['身高'])
print(dict2['詹姆斯']['年龄'])

# 增  加新元素
# 对不存在的键+赋值
dict1['年龄'] = 42
print(dict1)
# 改  元素||| 已有的 赋值就是改，没有的键值就是增
# 对已存在的键赋值
dict1['体重'] = 100
print(dict1)
# 删除字典元素 || 即把键和值一起删
dict1 = {'姓名': '姚明', '身高': 2.26, '体重': 100, '年龄': 42}
dict1.pop('年龄')
print(dict1)

print('-----------------------------------')
# 查询字典的方法 : 1. 遍历查询；
# for循环直接遍历字典，得到的是 key，
dict1 = {
    '姓名': '姚明',
    '身高': 2.26,
    '体重': 130,
    '年龄': 42
}
for key in dict1:
    print(key)

# items()

# 8.2非序列 ： 集合
# 集合是无序的可变数据结构，用{}定义，元素不可以重复
set1 = {1, 2, 3, 3, 4, 4, 5}
print(set1)
