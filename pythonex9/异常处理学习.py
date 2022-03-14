# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/14 15:12
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 异常处理.py
# @Software : PyCharm

"""
语法:
    try：
        尝试执行的代码
    except:
        如果try里面的代码报错,才会执行
"""
try:  # 意为 可以把所有出错的代码,写到try里面,如果程序报错了，就去执行except里面的代码
    print('后续的代码')
    print(12)  # 如果try里面没有报错代码会被执行
    print(aa)  # 如果代码报错,则直接调用except
except Exception as e:
    # 只有try里面的代码报错，才会执行except，如果没有报错，直接跳过except里面的代码
    # Exception 时所有错误类型的父类,包含了所有错误的错误类型,as e 代表把代码报错原因保存在了这个e 里面
    print('try里面的代码报错')
    print('报错原因为:', e)
else:
    print('代码没有异常哦')
print('后续代码')


# finally: 不管有没有报错,都会执行finally里面的代码
# print("这是finally")
def yichang():
    try:
        print(11 / 0)
    except Exception as e:
        print("报错原因:", e)
        return
    else:
        print("代码没有异常哦")
        return
    finally:
        print("这是finall")  # finally 一般在前面的控制中都写了 return 里面后, 如果后续还有代码要执行,就需要写在finally里面


yichang()
