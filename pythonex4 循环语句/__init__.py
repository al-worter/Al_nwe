# un =1
# n = 0
# while un<101:
#     number = un%2
#     if number ==0:
#         n =n- un
#     else:
#         n = n+un
#     un = un+1
# print(n)
# n = 1      #定义一个初始变量n并赋值为1
# sum = 0    #   定义sum初始变量并赋值为0
# while n <101 :   # 因为我们是要求1-100的和，所以使用while循环，让n取1-100内的数值
#     temp = n % 2  #定义的变量temp，用来判断n值是奇数还是偶数，temp是代表n/2的余数
#     if temp == 0: #接着对temp进行判断，如果temp为0，说明n是整数，temp不为0的话为奇数。
#         sum = sum -n  #当n为偶数时，n值为负，n值前面为“-”
#     else :   #n为奇数时n取正，n前面符号为“+”
#         sum = sum + n
#     n = n + 1  #上面命令执行结束后对n进行复制，知道n=101时，不符合n<101条件，此时跳出while循环！
# print(sum) #打印出1-2+3-4+5-6+7-8....99的值
list =[]
for i in range(1,9):
    b = i
    list.append(b)
print(list)

b = [1,2,3,4,5]
print(b[:-1][:2])
print(b[3:][::-1])