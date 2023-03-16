import unittest
# 两个数相加
from test_sum import TestDemo

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDemo))

runner=unittest.TextTestRunner()
runner.run(suite)