import  os
if os.path.exists("prac_5面向对象.py"):
    os.rename("prac_5面向对象.py","prac_5一个类创建多个对象，--多个变量对象的引用.py")


class Cat:
    def eat(self):
        print("小猫会叫")

    def drink(self):
        print("小猫会喝水")

# 创建对象
jvcat = Cat()
# 可以看到，输出的是一个地址，：结论 对象名就是一个变量名，保存当前内存对象空间的引用地址
print(jvcat)
print(Cat())
bosimao=Cat()
print(bosimao)
print(Cat())
# 使用一个类模板可以创建多个对象， 每一个对象都有自己的内存空间，并且互不干扰
# 调用类方法
jvcat.eat()
