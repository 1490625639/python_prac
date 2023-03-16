# C从B继承得来 B从A继承得来 那么C就具有了A和B得所有属性和方法
class Animal:
    def __init__(self):
        self.name="动物"
        self.age=22
    def eat(self):
        print("%s都爱吃东西"% self.name)
class Cat(Animal):
    def catch(self):
        print("捉老鼠方法")
class jvcat(Cat):
    def sing(self):
        print("波斯猫可以唱歌")
saly=jvcat()
print(saly.name,saly.catch(),saly.sing(),saly.eat(),saly.age)

# 爷爷类对象不能调用儿子的方法 更布不能访问孙子的
# animal=Animal()
# print(animal.catch())

