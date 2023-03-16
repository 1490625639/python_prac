import login
import unittest
from parameterized import parameterized
data=[
    ('admin','123456','登陆成功'),
    ('admin','23456','登录失败'),
    ('admin','123456','登陆成功')
]
class TestLogin(unittest.TestCase):
    @parameterized.expand(data)
    def test(self,username,password,expect):
        self.assertEqual(expect, login.loginmethod(username, password))
if __name__ == '__main__':
    unittest.mian()