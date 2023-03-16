# 类方法:针对类方法定义的方法
#     在类方法内部可以直接访问类属性或调用其他的方法
"""格式: @classmethod
    def 类方法名(cls):
        pass

    @classmethon 是装饰器,在不修改源代码的情况下对函数或方法进行修饰,要么在函数调用前添加,要么在函数调用后添加
    cls:类似于self,由哪个类调用的方法,方法内的cls就是哪个类的引用,后边也可以添加参顺,通过类名. 调用类方法时,不用传递
        cls参数,  在方法内部,可以通过cls.  访问类的属性
         """

class Person(object):
    # 类属性:定义在方法外面,类的内部
    # 作用:主要用来记录类对象的相关特征
    count = 0  # 类属性只会初始化一次
    print("类模板初始化一次")

    def __init__(self, name):
        # 实例属性
        print("初始化方法")
    # @classmethod是装饰器,告诉python解释器,这是一个类方法,不要报错
    @classmethod
    def get_count(cls):
        print("1类方法的作用:1处理类属性,或调用其他的类方法")
        print("cls参数保存当前类对象的引用%s"%cls)
        #
        cls.count+=20
        return cls.count

print("Person:",Person )
# 调用类方法:1 类对象.类方法名()
print(Person.get_count())

num=Person.get_count()
print(num)

#实例对象访问类方法
# 调用类方法：2 实例对象.类方法名() 不推荐使用,实例对象一般访问的是实例方法
xiaoming=Person("xi小明")
ret=xiaoming.get_count()
print(ret)