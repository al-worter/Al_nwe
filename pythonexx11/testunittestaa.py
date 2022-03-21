# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 15:16
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-21 unittest.py
# @Software : PyCharm
#
''''''
'''
如果用终端的话需要 在后面 使用 python+ + 文件名
    1.什么是unittest?unittest 是一个单元测试框架.
        1) 用来编写和管理自动化测试用例
        2) 提供了很多种断言方式, ( 断言: 判断预期结果和实际结果是否一致).
        3) 提供执行过程的数据,比如执行数量统计,执行花费时间,执行结果...
    2. unittest  由以下部分组成
        1) Test Fixture:用于测试执行前的环境初始化(指的是执行用例前的前提条件,
            比如:打开实例浏览器对象,打开被测网址,准备测试数据等.)
            和环境清理(关闭浏览器,清理测试过程中产生的测试数据.)
            环境初始化:
                setUp: 在执行每条用例之前会自动调用
                setUpClass: 必须使用@classmethod装饰器是在所有用例执行前自动调用
            环境清理:
                tearDown: 在执行每条用例 之后会自动调用
        2) Test Case : 一条测试用例就是一个Test Case, 注意,用例必须是以test 开头 ,不然不会被识别.
                执行结果:
                    . 代表通过(如果用例没有写断言,都默认通过)
                    F 代表不通过(代码没有报错,只是预期结果和实际结果不一致)
                    E 代表代码报错
                断言方式:
                    1. assertEqual() 判断预期结果等于实际结果．需要传入两个参数,第一个是预期结果,第二个是实际结果.
                       assertNotEqual() 判断预期结果不等于实际结果．需要传入两个参数,第一个是预期结果,第二个是实际结果.
                    2.assertIn()  判断预期结果包含在实际结果里面．需要传入两个参数,第一个是预期结果,第二个是实际结果.
                      assertNotIn() 判断预期结果不包含在实际结果里面．需要传入两个参数,第一个是预期结果,第二个是实际结果.
                    3.assertTrue() 判断实际结果是True只需要传入实际结果.
                      assertFalse() 判断实际结果是False只需要传入实际结果
                    unittest 用例的执行顺序:是按照用例的名称来执行的.(pytest 的用例是按照编写顺序执行)
        3) Test Suite: 测试套件,把所有的用例都统计到一起
        4) Test Runner: 执行对象,可以同一执行所有的用例.
'''
# 1.导入unittest 标准库
import unittest


# 2.新建测试类  必须继承unittest.TestCase类 ,如果不继承,则不会被unittest识别为一个测试类.
class TestMoudle(unittest.TestCase):

    def setUp(self):  # 环境初始化.
        self.a = 3
        self.b = 4
        print('in setUp')

    def tearDown(self):  # 环境清理
        print('in tearDown')

    def test01(self):  # 用例1
        print('test01')
        response = 7  # 预期结果
        result = self.a + self.b  # 实际结果
        self.assertEqual(response, result, f'预期结果是{response},实际结果是{result}')  # 判断预期结果和实际结果相等，-成功

    def test02(self):  # 用例2
        print('test02')
        response = 8  # 预期结果
        result = self.a + self.b  # 实际结果
        self.assertEqual(response, result, f'预期结果是{response},实际结果是{result}')  # —-失败第三个参数只有在用例失败的情况下会显示.

    def test03(self):
        print('test03')
        response = 7  # 预期结果
        result = self.a + self.b  # 实际结果
        self.assertEqual(response, result)  # 判断预期结果不等于实际结果--失败

    def test04(self):
        print('test04')
        response = '成功'  # 预期
        result = '邮件发送成功'  # 实际结果
        self.assertIn(response, result)  # 判断预期结果包含在实际结果里面 ___ 成功

    def test05(self):
        print('test05')
        response = '失败'  # 预期
        result = '邮件发送成功'  # 实际结果
        self.assertNotIn(response, result)  # 判断预期结果不包含在实际结果里面 ___ 成功

    def test06(self):
        print('test06')
        result = True
        self.assertTrue(result)  # 判断实际结果是True  ---成功

    def test07(self):
        print('test07')
        result = True
        self.assertFalse(result)  # 判断实际结果是False  ---失败

    @classmethod
    def setUpClass(cls):  # 所有用例执行前自动调用
        print('setUpClass')

    @classmethod  # 所有用例执行后自动调用
    def tearDownClass(cls):
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main()  # 直接使用unittest.main()调用,会自动识别测试类里面的用例.
