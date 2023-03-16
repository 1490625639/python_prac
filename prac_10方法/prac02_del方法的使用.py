# del 方法的使用场景
# del方法的使用  对象从内存空间销毁前，自动调用 如果想在销毁前做别的事情，就要用到del方法了
# 作用：清除资源的操作,文件的资源，网络套接字资源
class Cat:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("%s爱吃小鱼干"% self.name)
        self.file=open("cat.txt","w",encoding="utf-8")
        # 如果想让下边的方法访问到当前的局部变量，需要把局部变量添加为属性
        # 如何添加，加一个self
        # file.write("%s爱吃小鱼干"%self.name)
        self.file.write([12,234,4,3])


    def __del__(self):
        print("程序退出时对象从内存空间销毁")
        # 可以把文件的操作放到这边
        print("文件关闭前")
        self.file.close()    # 这里会报红因为file在上边的方法中 是局部变量
        print("文件关闭前")
        """在程序推出前自动调用
        ——del__方法可以手动调用"""
cat=Cat("老八")
print(cat.eat())
# del cat
# print(cat.name)   对象内存空间已经呗销毁,不能呗引用