class Person:
    "人类"
    def __init__(self,name,weight):
        "初始化方法"
        self.name=name
        self.weight=weight
    def __str__(self):
        return "姓名:%s,体重:%s"%(self.name,self.weight)

    def __str__(self):
        """打印对象的描述信息"""
        return "姓名是%s,体重是%.2f公斤"%(self.name,self.weight)
    def run(self):
        print("%s爱跑步,每次跑步减肥0.5公斤"%self.name)
        self.weight-=0.5
    def eat(self):
        print("%s是一个吃货,每次吃体重增加一公斤"%self.name)
        self.weight+=1
# 使用类模板创建对象
xiaoming=Person("小明",75)
print(xiaoming)

xiaoming.run()
print(xiaoming)

xiaoming.eat()
print(xiaoming)
xiaomei=Person("小妹",45.0)
# 可以使用一个类模板创建多个对象,每个对象的内存空间彼此独立,互不干扰
print(xiaomei)
print(xiaomei.eat())
print(xiaomei.run())