# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/10 17:04
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-10 习题.py
# @Software : PyCharm

# 1. 获取字符串 '11:12:11> 001 enter chatroom, level2' 中的用户id和等级
# list [start是元素检索起点，end 是指第一个开始排第几号，step 是指步长  start 开始算的第几个]
# str1 = '11:12:11> 001 enter chatroom, level2'
# list1 = str1.split()
# print(list1[1::3])

print('--------------------------')
# 2. 获取下面字符串中的所有用户id和等级
# str2 = '''11:12:11> 001 enter chatroom, level2
# 11:12:11> 22 enter chatroom, level3
# 11:12:11> 0004 enter chatroom, level105
# 11:12:11> 003 enter chatroom, level99'''
# list2 = str2.split('\n')
# print(list2)
# 然后用列表推导式 ：生成指定的列表 list= []   看章节PDF 6 推导式
# list3 = []
# for i in list2:
#     i = i.split()
#     list3.append([i[1], i[4]])
# print(list3)
#
# print('----------------------------')
# 3. 将字符串 'abcd[0910efg&*(]hijkl[ada2r4545]mn03opq$st' 中的非字母字符去掉
# 需要用到字符串 函数 .isalnum()  即：如果字符串至少有一个字符并且所有字符都是字母或数字则返回True,否则False
#
# str3 = 'abcd[0910efg&*(]hijkl[ada2r4545]mn03opq$st'
# list4 = ''.join(str3)
# print(list4)
# kop = []
# for i in list4:
#     if i.isalnum() is True:
#         kop.append(i)
# print(''.join(kop))
# print('-------------------')
# 4.编写一个程序，要求用户输入一个字符串，将字符串中重复的字符串去除，如输入'abcaadef'，输出为'abcdef'
# str4 = input('请您输入一段字符串：')
# list5 = []
# for j in str4:
#     if j not in list5:
#         list5.append(j)
#     else:
#         pass
# list5 = ' '.join(list5)
# print(list5)

# 5.模拟手机通讯录，模拟手机通讯录的增删改查操作，联系人信息需要包括1.姓名和2.电话即可
dict1 = {
    '刘翔': {
        '性别': '男',
        '电话': 10000029
    },
    '詹姆斯': {
        '性别': '男',
        '电话': 22229181
    },
    '古爱凌': {
        '性别': '女',
        '电话': 213123123
    }
}
# print(dict1)
# 增
dict1['张天爱'] ={'性别':'女','电话':'123123'}
print(dict1)
# 改
dict1['张天爱'] = {'性别':'女','电话':'520000'}
print(dict1)
# 删
dict1.pop('刘翔')
print(dict1)
# 查  用遍历查询 即 for
for key in dict1:
    print(key)

