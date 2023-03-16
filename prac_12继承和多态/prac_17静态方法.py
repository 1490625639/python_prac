
"""格式: @staticmethod
    def 静态方法名():
        pass
    @staticmethod 是装饰器,装饰的是静态方法名,告诉python解释器下面的方法是特殊的方法

         """

class Person(object):
    count = 0  # 类属性只会初始化一次
    print("类模板初始化一次")

    def __init__(self,name):
        self.name=name

    #定义静态方法
    @staticmethod
    def fun_static():
        print("静态方法既不需要self参数,也不需要cls参数")
        print("静态方法中不需要用到实例对象的实例属性和实例方法,也不需要用到类对象的类属性和类方法")
        print("静态方法不会破环类的封装性")
        print("定义静态方法,只需要在普通方法上添加一个@staticmethod,没有参数(但是可以手动添加)")
    @staticmethod
    def getsum(a,b):
        print("%d +%d =%d"%(a,b,(a+b)))
#调用静态方法
# 1 类名.静态方法名()
Person.fun_static()

print("--"*20)
# 2 实例对象.静态方法名()
hua=Person("如花")
hua.fun_static()


Person.getsum(1,2)