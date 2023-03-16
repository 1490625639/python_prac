class Person(object):
    def __init__(self,name):
        self.name=name
    def  eat(self):
        print("%s爱吃美食"%self.name)
xiao=Person("xixi").eat()
xiaoming=Person("小明")
# 创建的对象在内存空间实际存在,叫做实例对象
print(xiaoming)
# 实例对象中的属性叫做实例属性
print(id(xiaoming.name))
# 实例对象可以调用的方法并且具有self参数,是实例方法
print(id(xiaoming.eat()))
print("8"*20)


xiaowang=Person("小王")
print(xiaowang)
print(id(xiaowang))
print(id(xiaowang.eat()))

"""总结:一个类模板可以有多个实例对象,
每个实例对象的内存空间彼此独立,互不干扰
实例属性保存在实例对象的内存空间中,
实例方法保存在类模板中
但是: 使用实例对象调用实例方法时.是一个动态绑定的过程"""