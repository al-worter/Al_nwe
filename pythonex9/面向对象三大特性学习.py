# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/14 14:14
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 面向对象三大特性.py
# @Software : PyCharm

# '''
# 面向对象三大特性：
#     1) 封装 :  把同一类的属性和方法封装到一个类里面
#     2) 继承 : 子类可以继承父类的属性和方法
#               被继承的类叫父类/基类/超类
#               继承的类叫子类/导出类.
#               继承后子类会拥有多个父类,当多个父类有重复的属性/方法时，以继承的第一个父类为准.
#     3) 多态 :  当子类和父类拥有共同的属性/方法的时候,子类会覆盖父类的属性/方法。  子类和父类相同的属性，子类覆盖父类.
# '''


class Animal:  # 父类
    def __init__(self, color, sex, age, weight):
        self.color = color
        self.sex = sex
        self.age = age
        self.weight = weight

    def eat(self):
        print('animal is eaating.....')

    def run(self):
        print('runing')


class Cat(Animal):  # 猫类继承了动物类,会拥有动物类所有属性和方法
    # 猫类需要新增一个属性 - height 其他属性不变
    # 第一种方式 : 直接重写构造方法,会产生很多种重复代码
    # def __init__(self, color, sex, age, weight):
    #     self.color = color
    #     self.sex = sex
    #     self.age = age
    #     self.weight = weight
    # 第二种方式 :  在重写构造方法过程中，调用父类的__init__方法
    def __init__(self, color, sex, age, weight, height):
        Animal.__init__(self, color, sex, age, weight)  # 调用父类的构造方法
        self.height = height  # 只用给新增的这个属性赋值

    def eat(self):  # 子类重写了eat 方法
        print('cat is eating...')  # 当子类和父类拥有共同的属性和方法的时候,子类会覆盖父类


class BOsi:
    def call(self):
        print('miao~')

    def runting(self):
        print('bosi is backe runing')


class BoSimao(Cat, BOsi):  # 波斯猫类继承了猫类，所以会同时拥有猫类和动物类的
    pass


# cat
cat = Cat('白色', '公', 3, 20, 100)
cat.eat()
# bosimao
bosimao = BoSimao('白色', '公', 4, 50, 100)  # 后面加传实参 只有前面该bosimao 有设置参数 的，例如 animal(color,age,sex,weight)
bosimao.run()
bosimao.call()
# bosi
bakc = BOsi()
bakc.runting()
