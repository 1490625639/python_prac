import os
if os.path.exists("prac_2面向对象.py"):
    os.rename('prac_2面向对象.py','prac_2定义简单的类（不含方法）.py')

# 类是更大的一个封装
"""格式：
class 类名：
    def 方法一（self，参数列表）：
        pass
    def 方法一（self，参数列表）：
        pass"""
class Person:
    def run(self):
        # self参数不用自己传，python自己传，但是自己写的参数要传
        print("跑步方法")
    def eat(self,food,fruit):
        print("这里是吃方法%s",food)
    def sleep(self):
        print("睡觉方法")
# 创建对象    格式  对象变量=类名（）
#     对象变量名保存的是对对象内存地址的引用
# 通过对象来调用方法 格式  对象变量。方法名（）

# 对象=类名（）
# 对象。方法名（）
zhangsan=Person()
zhangsan.run()
zhangsan.eat('老八奥里给',"agiao的泪")