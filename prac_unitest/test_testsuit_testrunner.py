# 导包
import unittest

from tsetcase_using import TestDemo
from tsetcase_using2 import TestDemo1
# 实例化套件对象
suite = unittest.TestSuite()
# 使用套件对象添加套件方法
# 方法一：suite.addtest(类名(方法名))
"""suite.addTest(TestDemo("test_method1"))
suite.addTest(TestDemo("test_method2"))
suite.addTest(TestDemo1("test_method3"))
suite.addTest(TestDemo1("test_method4"))"""
# 方法二：将一个测试类中的所有方法进行添加  套件对象.addTest(unitest.makeSuite(测试类名)
#         缺点makeSuite方法不会提示
suite.addTest(unittest.makeSuite(TestDemo))
suite.addTest(unittest.makeSuite(TestDemo1))
# 实例化运行对象
runner=unittest.TextTestRunner()
# 调用运行对象来执行套件对象
runner.run(suite)
