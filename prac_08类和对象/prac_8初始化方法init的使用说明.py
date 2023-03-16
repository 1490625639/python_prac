import os
if os.path.exists("prac_8面向对象.py"):
    os.rename("prac_8面向对象.py", "prac_8初始化方法init的使用说明.py")
# -init0方法的使用
class Cat:
    def __init__(self):
        """
        初始化方法
        主要用来初始化数据
        初始化属性数据
        在使用类模板创建对象时自动调用
                魔法方法,特定情况子自动调用
            """
        print("初始化方法主要用来初始化数据")
    def eat(self):

        print("小猫爱吃鱼")
# 创建对象,理论上没有东西
# 可以通过断点看看是否引用init
# 可以看到
# 尽管没有调用方法,但是init默认调用了,
# 就意味着可以在init里面添加一些属性,因为在类外面加属性容易错乱
jvcat=Cat()
"""使用类模板创建对象时
第一步给对象分配内存空间
第二部 调用__init__方法初始化属性数据"""
