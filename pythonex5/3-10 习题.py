# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/10 17:04
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-10 习题.py
# @Software : PyCharm

# 1. 获取字符串 '11:12:11> 001 enter chatroom, level2' 中的用户id和等级   # 冒号即切片
# list [start是元素检索起点，end 是指第一个开始排第几号，step 是指步长  start 开始算的第几个]
# str1 = '11:12:11> 001 enter chatroom, level2'
# list1 = str1.split()
# print(list1[1::3])

# str1 = '11:12:11> 001 enter chatroom, level2'
# id = str1[10:13]
# level = str1[-6:]
# print(f'id:{id},等级{level}')
#

print('--------------------------')
# 2. 获取下面字符串中的所有用户id和等级
str2 = '''11:12:11> 001 enter chatroom, level2
11:12:11> 22 enter chatroom, level3
11:12:11> 0004 enter chatroom, level105
11:12:11> 003 enter chatroom, level99'''
# list2 = str2.split('\n')
# print(list2)
# 然后用列表推导式 ：生成指定的列表 list= []   看章节PDF 6 推导式
# list3 = []
# for i in list2:
#     i = i.split()
#     list3.append([i[1], i[4]])
# print(list3)
#
# lines = str2.split('\n')
# print(lines)
# for line in lines:
#     list2 = line.split('')
#     id = list2[1]
#     level = list2[-1]
#     print(f'ID:{list2[1]:5},等级:{list2[-1]:10}')


# print('----------------------------')
# 3. 将字符串 'abcd[0910efg&*(]hijkl[ada2r4545]mn03opq$st' 中的非字母字符去掉
# 需要用到字符串 函数 .isalnum()  即：如果字符串至少有一个字符并且所有字符都是字母或数字则返回True,否则False
#
# str3 = 'abcd[0910efg&*(]hijkl[ada2r4545]mn03opq$st'
# list4 = ''.join(str3)
# print(list4)
# kop = []
# for i in list4:
#     if i.isalpha() is True:
#         kop.append(i)
# print(''.join(kop))

# 方法二：
# str3 = 'abcd[0910efg&*(]hijkl[ada2r4545]mn03opq$st'
# str4 = ''
# for i in str3:
#     if i.isalpha():
#         str4 += i
#         print(str4)
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

#
# str6 = input('请输入一个字符串：')
# str7 = ''
# for i in str6:
#     if i not in str7:
#         str7 += i
# print(str7)
# 5.模拟手机通讯录，模拟手机通讯录的增删改查操作，联系人信息需要包括1.姓名和2.电话即可
# dict1 = {
#     '刘翔': {
#         '性别': '男',
#         '电话': 10000029
#     },
#     '詹姆斯': {
#         '性别': '男',
#         '电话': 22229181
#     },
#     '古爱凌': {
#         '性别': '女',
#         '电话': 213123123
#     }
# }
# # print(dict1)
# # 增
# dict1['张天爱'] ={'性别':'女','电话':'123123'}
# print(dict1)
# # 改
# dict1['张天爱'] = {'性别':'女','电话':'520000'}
# print(dict1)
# # 删
# dict1.pop('刘翔')
# print(dict1)
# # 查  用遍历查询 即 for。
# for key in dict1:
#     print(key)
dict2 = {
    '张三':139999999,
    '张思':142233333,
    '张五':123233333
}
option = int(input('请输入操作:{1.增加联系人；2.删除联系人；3.搜索联系人；4.修改联系人}'))
if option ==1:
    print('------增加联系人------')
    name = input('请输入你要增加的联系人姓名：')   # 直接用
    if name in dict2:
        print('用户已存在')
    else:
        phone = input('请输入要增加的联系人电话：')
        dict2 [name] = phone
elif option == 2:
    print()
elif option == 3:
    print()
elif option ==4:
    print()