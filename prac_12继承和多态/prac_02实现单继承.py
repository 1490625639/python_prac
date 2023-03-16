class Animal:
    def __init__(self):
        self.name="动物"
        self.age=23
    def eat(self):
        print("%s都爱吃"%self.name)
class Cat(Animal):
    def catch(self):
        print("小猫抓老鼠方法")
animal=Animal()
# 父类可以调用自己的属性和方法
print(animal.name)
print(animal.age)
# 父类可以盗用自己的方法
print(animal.eat())
# 继承不能调用儿子的方法
print(animal.catch())