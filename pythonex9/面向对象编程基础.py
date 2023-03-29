# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/14 9:50
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 面向对象编程基础.py
# @Software : PyCharm

''''''
'''
面向过程：
        是一种以事件为中心的编程思想，重点关注功能实现步骤，第一步....,第二步.....
面向对象:
        是一种对象为中心的编程思想，不关注过程怎么实现，只关注最后结果。
        核心思想：封装，把同一类事物的属性和方法封装到一个类里面,通过实例和类调用.
        核心概念：
            类：
                例如：人类、犬类、机械类
                人类：
                1)静态特征
                2)动态特征
                代码:
                1）属性:
                        1.类属性：一个类的所有对象都拥有同样的值，定义成类属性
                        2.实例属性:一个类里面的对象拥有不同的值，定义成实例属性, 定义在构造方法里面
                2）方法:
                    1.构造方法 __init__ / 初始化方法：
                        在实例化对象的过程中会自动调用。作用： 1. 给实例属性赋值.  2.所有需要在实例对象后就拥有的属性，都可以定义

                    2.实例方法: 类里面的普通方法,没有任何修饰器。第一个形参必须是self. 这个形参会自动传入当前的
                                调用方式：1.1可以被对象调用.   2. 不能被类直接调用  3.调用其他的属性(类属性和实例属性)和方法(类方法、实例方法、静态方法)必须使用self

                    3.类方法 ： 一个类所有的对象都拥有的方法，定义成类方法。
                            特点：1. 必须使用@classmethod 装饰器 . 2.第一个参数必须是cls ,cls代表当前这个类，不需要手动传参
                            调用方式: 1.可以被类调用  2.也可以被对象调用 .  3. 通过cls调用类属性/类方法/ 静态方法   4 . 不能调用实例属性/方法

                    4.静态方法: 跟类无关的工具方法,定义成静态方法
                            特点：1.必须使用@staticmethod 装饰器  2.就是一个普通的函数，没有必须的第一个参数
                            调用方式: 1.不能调用类里面的任何属性和方法 2.对象和类都可以调用静态方法


            对象：从类里面实例化出来的一个具体的对象.
'''
'''面向对象三大特性：
    1) 封装 :  把同一类的属性和方法封装到一个类里面
    2) 继承 : 子类可以继承父类的属性和方法
              被继承的类叫父类/基类/超类
              继承的类叫子类/导出类.
              继承后子类会拥有多个父类,当多个父类有重复的属性/方法时，以继承的第一个父类为准.
    3) 多态 :  当子类和父类拥有共同的属性/方法的时候,子类会覆盖父类的属性/方法。  子类和父类相同的属性，子类覆盖父类.
'''
class People:
    eyes = 2  # 类属性
    nose = 1  # 类属性
    def __init__(self, name, sex):  # 构造方法/初始化方法
        self.name = name  # self.name 是实例属性，把形参name 的值，赋值给实例属性self.name.
        self.sex = sex
    def play_game(self):  # 实例方法 p1
        # 打印P1对象，返回这个对象在内存空间的地址
        print(self)  #
    @classmethod  # 类方法必须使用@classmethod 修饰器
    def eat(cls):
        print('人类都会吃饭')
    # @staticmethod
    # def run(sel):
p1 = People('张三', '男')
print(p1)
p1.eat()
p2 = People('李四', '男')
print(p2)
p2.eat()


import socket
import struct


