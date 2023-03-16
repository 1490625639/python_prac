import os
for i in range(2,7):
    open("prac0%d_del方法的使用.py"%i,"w",encoding="utf-8")
# del方法的使用  对象从内存空间销毁前，自动调用 如果想在销毁前做别的事情，就要用到del方法了
# 作用：清除资源的操作
class Cat:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("%s爱吃小鱼干"%self.name)
    def __del__(self):
        print("程序退出时对象从内存空间销毁")
        # 可以把文件的操作放到这边
        """在程序推出前自动调用
        ——del__方法可以手动调用"""
cat=Cat("老八")
del cat
# print(cat.name)   对象内存空间已经呗销毁,不能呗引用