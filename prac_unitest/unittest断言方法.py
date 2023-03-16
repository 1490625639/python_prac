# za在unit test中使用断言的时候，都需要通过self.断言方法 来实现
import unittest

class test_n(unittest.TestCase):
    def test_name(self):
        self.assertEqual('1','2')





"""mathmark = int(input())
#断言数学考试分数是否位于正常范围内
assert 0 <= mathmark <= 100
#只有当 mathmark 位于 [0,100]范围内，程序才会继续执行
print("数学考试分数为：",mathmark)"""