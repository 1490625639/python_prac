# 测试夹具是一种代码结构，在某些特定的情况下会自动执行
import unittest
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print("测试方法执行前都会运行一遍")
        print("2 输入网址")
    def tearDown(self) -> None:
        print("每个方法执行之后都会执行的方法")
        print("4 关闭当前界面")
    def test(self):
        print("3 输入正确的用户名和密码")
    @classmethod
    def setUpClass(cls) -> None:
        print("类级别：在每个测试类中的所有方法执行前后都会调用的结构")
        print("1.打开浏览器")
    @classmethod
    def tearDownClass(cls) -> None:
        print("5 关闭浏览器")
