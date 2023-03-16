# 子类继承父类的过程中,子类有跟父类相同的方法名,就称子类重写了父类的方法----重写的前提是有继承
"""   出现的原因: 父类的需求不能满足子类的需求
重写父类方法有两种情况:
1 覆盖父类的方法  功能覆盖 :子类重写的方法与父类完全不同
2 对父类方法进行拓展   :在父类方法的基础上进行拓展"""



# 爷爷类
class Animal:
    def __init__(self):
        self.name="动物"
        self.age=22
    def eat(self):
        print("%s都爱吃东西"% self.name)
# 爸爸类
class Cat(Animal):
    def catch(self):
        print("捉老鼠方法")
# 儿子类
class jvcat(Cat):
    def catch(self):
        print("波斯猫不捉老鼠了,改捉鱼了")
saly=jvcat()
cat=Cat()
# 子类重写了父类的方法后,调用方法时,调用的是自己重写的方法
print(saly.catch())
# 父类调用的,还是自己本身的方法
print(cat.catch())