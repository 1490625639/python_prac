"""类属性就是给类对象   中定义的属性
通常用来记录这个类相关的特征
类属性不会用于记录具体对象的特征
"""
# 使用类属性可以在不破坏类的封装特性前提下实现某些功能

# 需求:统计当前类模板创建了几个实例对象
class Person(object):
    # 类属性:定义在方法外面,类的内部
    # 作用:主要用来记录类对象的相关特征
    count = 0  # 类属性只会初始化一次
    print("类模板初始化一次")

    def __init__(self, name):
        # 实例属性
        print("初始化方法")
        self.name = name
        # 使用类属性统计当前类模板创建了几个实例对象
        # 访问类属性  使用类名.类属性   访问
        Person.count += 1

    def eat(self):
        print("%s爱吃美食" % self.name)


# 使用类模板创建对象
xiaoming = Person("小明")
xiaowang = Person("小王")
# 在使用类模板创建完对象时，--init方法就已经走了一遍了，此时的count 数量就已经是2了
#
# 类外访问类属性 两种方式
# 1    类名.类属性名   推荐
print(Person.count)
# 2      实例对象.类属性名
print(xiaoming.count)

# 修改类属性：
# 1 类名.类属性=值
Person.count = 5
print(Person.count)

#TODO 2 实力对象.类属性名=值 经过测试,这种方式并不能修改类属性的值,
# 本质上属于给实例对象添加了一个跟类属性同名的实例属性

xiaoming.count = 10
print(Person.count)
