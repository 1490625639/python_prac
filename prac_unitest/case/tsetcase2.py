""""unitest 中的testcase使用练习"""

import unittest
# 自定义测试类,需要继承unitest类中的testcase模块
class TestDemo2(unittest.TestCase):
    # 书写test方法,即用例代码,目前没有真正的测试代码,这里用print方法代替
    def test_method2_1(self):
        print("测试方法1")
    # 注意:::书写测试方法 必须以 test_开头 (本质上是以 test开头)
    def test_method2_2(self):
        print("测试方法2")
# 执行测试用例
# 1.将光标放在类名的后边运行,执行的是整个类的测试方法
# 2.将光标放在方法的后边运行,执行的是当前的方法

"""常见的错误:
1:代码文件的命名不规范    会出configuration框
    (1):代码文件以数字开头,
    (2):代码文件名字中有空格
    (3):代码名字中有中文
    (4):其他的标志符号
    (只能以数字,字母,下划线组成,不能数字开头)
解决:修改代码文件名字
2:代码运行没有结果         右键运行没有unitests for 提示

解决一:重新新建一个代码文件,将代码复制进去.
解决二:编辑configuration框,把python运行的这个文件删除,然后重运行,直到出现unitests fot

3:没有找到用例

解决:测试方法不是以test_开头的,或者单词写错了.
"""