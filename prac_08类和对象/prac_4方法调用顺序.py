import os
if os.path.exists("prac_4面向对象.py"):
    os.rename("prac_4面向对象.py","prac_4方法调用顺序.py")
class Cat:
    def eat(self):
        print("小猫会叫")
    def drink(self):
        print("小猫会喝水")
jvcat=Cat()
jvcat.eat()
jvcat.drink()

"""
    1经过断点调试后发现，定义类模板后，python解释器会进入类模板扫描一遍，为了找到方法，定义方法
    但是不会访问方法内部代码，类模板只被初始化一次
    2当使用类模板创建对象，通过对象。方法名（）调用方法时候，才会进入方法内部执行代码
    3方法中的代码执行完毕后，回到调用方法的地方，继续向下执行
        """