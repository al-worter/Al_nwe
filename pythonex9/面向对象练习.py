# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/14 11:06
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 面向对象练习.py
# @Software : PyCharm

# '''
# 设计汽车变速箱练习:
# 定义一个汽车类:
# 属性:牌子,颜色,速度
# 功能:
# 	1.加速,接收增加的速度,将速度添加到成员属性的速度里
# 	2.减速,接收减少的速度,将成员属性的速度减少,当速度小于0,提示车已经停了
# 	3.行驶,打印"一辆XXX颜色的XX正以XX速度行驶",如果当前速度小于0,打印”一辆XXX颜色的XX停在路边.”
# '''


class Car:
    sign = '牌子'
    color = '颜色'
    speed = 0

    def __init__(self, sign, color, speed=120):  # 给形参添加默认值，从那个形参开始后面都需要添加默认值, 除非把默认值的形参放到后面
        print(self)
        self.sign = sign
        self.color = color
        self.speed = speed

    def speed_up(self, now_speed):  # 把增加的速度作为形参  .1.加速,接收增加的速度,将速度添加到成员属性的速度里
        self.speed += now_speed

    def speed_down(self, now_speed):  # 把减的速度作为形参 。减速,接收减少的速度,将成员属性的速度减少,当速度小于0,提示车已经停了
        self.speed -= now_speed  # 先把减小的速度计算出来
        print(self.speed)
        if self.speed <= 0:
            print('车已经停了')

    def run(self):  # 行驶,打印"一辆XXX颜色的XX正以XX速度行驶",如果当前速度小于0,打印”一辆XXX颜色的XX停在路边.”
        if self.speed <= 0:
            print(f'一辆{self.color}的{self.sign}停在路边')
        else:
            print(f"一辆{self.sign}的{self.color}正在以{self.speed}的速度在行驶")

    @classmethod
    def runing(cls):
        print(cls)
        print(f'{cls}')

car = Car('奥迪A7s', '玫瑰金红色', 0)
car.speed_up(120)  # 调用加速度方法，那么此时的self.speed = 120
car.run()
car.speed_down(130)
car.run()

car2 = Car("奥迪RS8S", "黑色", 150)
car2.run()
car2.speed_up(188)
car2.run()

car3 = Car('现代', '黑色')

car4 = Car('宝马', '白色', speed=200)  # 如果要跳过color 给speed传参，需要指定关键字speed
car4.run()

lan = Car('兰博基尼','青黄色')
lan.runing()