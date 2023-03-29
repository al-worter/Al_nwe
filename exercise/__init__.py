r = 25
area =3.1415 * r * r
print(area)
print("{:.2f}".format(area))

# import turtle
# turtle.pensize(2)
# turtle.circle(10)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(160)

#turtle 图形库绘制 图形
# '''实例1：绘制五角星'''
# from turtle import *
# color('red','red')
# begin_fill()
# for i in range(5):
#     fd(200)
#     rt(144)
# end_fill()

'''实例2：温度转换
    # 1 可以  直接的做成 华氏温度跟摄氏温度转换 ，温度值转换
    # 2 将温度信息发布的声音或图象形式进行理解和转换
    # 3 监控温度信息发布渠道，实时获取并转换温度值
    F 表示华氏度，C表示摄氏度，82F表示华氏82度，28C表示摄氏28度
    C = (F-32)/1.8
    F = C*1.8+32
'''
temstr = input("请输入带有符号的温度值：")
if temstr[-1] in ["F","C"]:
    C = (eval(temstr[0:-1])-32)/1.8
    print("转换后的温度{:2f}C".format(C))   # {：。2f} 表示将变量C填充到这个位置时，取小数点后两位
elif temstr[-1] in ['C','c']:
    F = 1.8*eval(temstr[0:-1])+32            # eval()  评估函数 意为 去掉参数最外侧引号并执行余下语句的函数
    print("转换后的温度时{:.2f}F".format(F))
else:
    print("输入格式错误")
