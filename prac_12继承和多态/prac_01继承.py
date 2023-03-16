for i in range(2,6):
    file=open("prac_0%i继承.py"%i,"w",encoding="utf-8")
file.close()
# 面向对象三大特性：封装继承多态
# 继承优点:1实现代码重用，2简化代码结构，
"""语法:     class 子类名(父类名):
        子类可以调用父类的方法,不需再次开发"""

# 实现单继承:
class Animal:
    def __init__(self):
        "初始化方法"
        self.name="动物"
        self.age=3
    def eat(self):
        print("%s 都爱吃"%self.name )
class Cat(Animal):
    def catch(self):
        print("小猫抓老鼠")

# 使用父类属性创建对象
animal=Animal()
# 父类的对象可以访问自己的属性
print(animal.name)
# 父类对象可以调用自己的方法
animal.eat()
# 父类对象无法调用子类方法
# print(animal.catch())

print("----"*20)
# 使用子类模板创建对象
jvcat=Cat()
# 子类对象可以访问父类属性
print(jvcat.name)
print(jvcat.age)
# 子类对象可以访问到父类方法
jvcat.eat()
# 继承不是复制,访问子类属性时,先到子类中查找.子类没有该属性,则去父类中查找