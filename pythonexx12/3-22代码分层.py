# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/22 14:10
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-22线性编程.py
# @Software : PyCharm
#
''''''
'''
学习要义: 使用PO/POM模式进行分层设计:
    优点:
        1．减少代码的重复性
        2.提高测试用例的可读性,
        3.提高脚本的可维护性
分层设计后的脚本分为 7 层 :
    1. common/base : 保存公共方法  .( 比如实例化浏览器)   保存的
    2. page :       业务流程  ()
    3. data :       保存测试数据
    4. case :       使用unittest框架写的用例和断言    一一对应page页面,(用unittest框架写用例和断言.不会有元素定位,只需要调用对应page页面的方法.)   有多少个page 就有多少case
    5. log  :       运行期间的日志文件
    6. report:      运行结束后生成的测试报告
    7. run.py :     程序的主入口,用来批量执行所有的用例     
自动化用例的选型:  (自动化测试什么时候介入?:#在需求评审阶段就需要准备介入,需要前端的代码开发,规范代码书写,方便后期自动化测试 .  2. 编写手工测试用例的时候,可以做自动化测试的用例进行标记,整理起来.3.最后进行对用例进行自动化)
    1. 不是所有的手工用例都需要转化为自动化用例.
    2. 考虑到开发的成本,不要选择流程太复杂的用例,如果有必要,可以拆分为多个用例来实现.
    3.可以选择主体流程做自动化用例.
    4.可以选择重复执行步骤的用例,比如字段验证这一类.
    自动化用例和手工用例的占比: 15~30%不等, 依据项目大小.
自动化用例脚本的编写原则:
    1. 一个脚本是一个完整的场景,(从打开浏览器,操作步骤,关闭浏览器)
    2. 一个脚本只验证一个功能点.    
    3. 尽量做功能的正向逻辑验证(如添加加购物车并登录支付)
    4. 脚本之间不要产生太多关联性,每一个脚本尽量互相独立.
    5. 测试过程中产生的测试数据,测试完成后一定要进行清理.  
'''

# 测试完成后一定要进行清理
# # class Solution:
# IP ="114.55.207.244"
# def addr2dec(addr):
#     "十进制IP换成十进制整数"
#     items = [int(x) for x in addr.split(".")]
#     return sum([items[i] << [24, 16, 8, 0][i] for i in range(4)])
#
# def dec2addr(dec):
#     "十进制整数IP转换成字符串IP地址"
#     return ".".join([str(dec >> x & 0xff) for x in [24, 16, 8, 0]])
# # if __name__ == '__main__':
# do = IPtoNum(IP)
# print ipto
# print IPtoNums(ipto)

# IP = "114.55.207.244"
# def addr2dec(addr):
#     "十进制IP换成十进制整数"
#     items = [int(x) for x in addr.split(".")]
#     return sum([items[i] << [24, 16, 8, 0][i] for i in range(4)])
# def dec2addr(dec):
#     "十进制整数IP转换成字符串IP地址"
#     return ".".join([str(dec >> x & 0xff) for x in [24, 16, 8, 0]])
#
# dec = addr2dec(IP)
# print(dec)
# print (dec2addr(dec))

# n = int(input())
# st = input()
# list = []
# lists = st.split(" ")
# for i in range(0,n-1):
#     # print(list)
#     for z in range(0,n):
#         if z == n-1:
#             print(list[z])
#         else:
#             print(list[z],end=' ')
#     a = list[n-1]
#     for j in range(n-1,0,-1):
#         list[j] = list[j-1]
#     list[0] = a
# for z in range(0,n):
#     if z == n-1:
#         print(list[z])
#     else:
#         print(list[z],end=' ')

#矩阵相加，两个3行3列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
# X = [[12, 7, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# Y = [[5, 8, 1],
#      [6, 7, 3],
#      [4, 5, 9]]
# Z = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
# for i in range(3):
#     for j in range(3):
#         Z[i][j] = X[i][j] + Y[i][j]
# print(Z)


# class Solution:
#     def generateMatrix(self , int n):
#         public int[][] generateMatrix (int n){
#             int[][] result = new int[n][n];
#             if(n<1){
#                 return result;
#             }
#             int count=1;
#             int rowStart = 0 , rowEnd = n-1;
#             int colStart = 0 , colEnd = n-1;
#             while(count <= n*n){
#                 for (int i = colStart;i<colEnd;i++){
#                     result[rowStart][i] = count++;
#                 }
#                 for (int i=rowStart+1;i<=rowEnd;i++){
#                     result[i][colEnd] = count++;
#                 }
#                 for(int i=colEnd-1;i>=colStart;i--){
#                     result[rowEnd][i] = count++;
#                 }
#                 for(int i=rowEnd-1;i>rowStart;i--){
#                     result[i][colStart] = count++;
#                 }
#                 rowStart++;
#                 rowEnd--;
#                 colStart++;
#                 colEnd--;
#             }
#             return result
#         }
#

