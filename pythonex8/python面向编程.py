# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/12 14:35
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : python 面向编程.py
# @Software : PyCharm


# 11.1 面向对象编程
# 11.11.1
class Women:
    pass


# 11. 定义属性
# 1.类变量
# 2.对象变量
# 3.局部变量
# 1.1
class women:
    classmen = '犬类'  # ji即类变量 ，是该变量中所有变量所共用的.


# 1.2
class Dog:
    classname = "犬类"

    def __init__(self, name, color):  # __init__() 意思是构造方法
        # 该self.name 是对象变量，前面是以self 来修饰，属于对象所有方法
        # name 是局部变量，只在定义的方法中有用
        self.name = name
        self.color = color

    # 实例方法
    def eat(self):
        print(f"{self.name}正准备把啃骨头的狗，吃掉它")

    def bark(self):
        print(f'爸爸八八八爸爸')


# 11.1.2 根据类生成对象
dog1 = Dog('小黄', '黄色')  # 该类生成的对象是调用上面 构造方法的类量.
# 调用对象的属性和方法|| 通过对象调用
print(dog1.name)
print(dog1.color)
print(dog1.classname)
dog1.eat()
dog1.bark()

dog2 = Dog('旺财', '黑色')
print(dog2.name)
print(dog2.color)


class User:
    def __init__(self, first_name, last_name):  # __init__() 意思是构造方法
        # 该self.name 是对象变量，前面是以self 来修饰，属于对象所有方法
        # name 是局部变量，只在定义的方法中有用
        self.first_name = first_name
        self.last_name = last_name
        self.__money  = 10000    # 如果不给别人操作，可以在money 前面加__money  ,即把类变量变成私密变量。


    def describe_user(self):
        print(f"{self.first_name}{self.last_name}")

    def greet_user(self):
        print(f"hello,{self.first_name}{self.last_name}")


user1 = User("张", "天爱")
user1.describe_user()
user1.greet_user()
# print(user1.money)
# user1.lend()

# 继承
class HuskyDog(Dog):
    def destroy(self):
        print(f"{self.name}正在拆家")


dog3 = HuskyDog("二哈","灰白")
print(dog3.name)
dog3.eat()
dog3.destroy()


if __name__ == "main"