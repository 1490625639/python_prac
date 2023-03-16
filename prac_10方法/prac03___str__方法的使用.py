"""__str__方法 特点：打印对象时，自动调用  print(对象名) ——str__自动调用
    ——str__方法必须有返回值，只能返回字符串
    """
class Cat:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("%s爱吃小鱼干"% self.name)
    def __str__(self):
        print("使用print打印对象自动调用")
        return "名字是%s"%self.name
        # return 122    注意 str魔法方法只能返回字符串
    # 如果当前函数中没有STR方法，一定会打印地址，但是这里有，自动调用了str方法
jv=Cat("jvmao")
print(jv)
