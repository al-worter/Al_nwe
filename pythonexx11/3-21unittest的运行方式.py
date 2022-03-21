# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 17:09
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-21unittest的运行方式.py
# @Software : PyCharm
''''''
#
'''
    学习要义:
        1.unittest.main()执行当前文件的所有用例.
        2.TetsSuite测试集需要一条一条的统计用例.
        3.discover 测试套件  统计多个文件的用例一起执行
            步骤: 1) 实例化一个测试套件,用来装所有用例
                  2) 实例化一个执行对象
                  3) 使用执行对象调用run方法执行上面的测试套件
                  
        注意: 文件命名需要以字母组成
'''

import unittest

# 1. 实例化一个测试套件对象,并且指定要执行的文件,
# discover 后面需要传入两个参数,第一个参数是文件所在的路径,./ 代表当前文件,第二个参数是要执行的文件称
# discover = unittest.defaultTestLoader.discover('./','3-21unittestaa.py')
discover = unittest.defaultTestLoader.discover('./','test*.py')  # 执行当前路径下所有以test 开头的文件
# 2. 生成一个执行对象
runner = unittest.TextTestRunner()
# 3 .执行文件对象调用run() 方法执行
runner.run(discover)
