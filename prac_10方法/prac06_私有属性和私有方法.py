class Women:
    def __init__(self,name):
        self.name=name
        # 前置双下划线的是私有属性
        self.__age=23
    def eat(self):
        # 在内的内部可以访问私有属性
        print("%s是一个吃货，她今年%s岁了"%(self.name,self.__age))
        # 在类的内部可以通过self访问私有方法
        self.__secret()
    def __secret(self):
        print("个人秘密不透漏")
meinv=Women("我i")
print(meinv.name)
# 在类的外部无法直接访问到私有属性
# print(meinv.__age)
print(meinv.eat())
# 在类的外部无法直接访问到私有方法
# print(meinv.__secret)