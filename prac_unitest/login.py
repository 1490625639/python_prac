import unittest
def loginmethod(username,password):
    if username=="admin" and password=="123456":
        return "登陆成功"
    else:
        return "登录失败"