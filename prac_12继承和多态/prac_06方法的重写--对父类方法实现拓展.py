"""对父类方法进行拓展 有两种方法
一:  在需要的位置,     super().父类方法名        关于super,是一个类,super()就是一个super类创建的对象,
二:  父类名.方法(self)

"""
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
        print("捉老鼠")
# 儿子类
class jvcat(Cat):
    def catch(self):
        # super().catch()
        Cat.catch(self)     #不推荐使用,父类修改后,在调用的地方,也调用的地方也需要修改父类名,不方便
        print("波斯猫捉鱼了")
saly=jvcat()
cat=Cat()
# 子类重写了父类的方法后,调用方法时,调用的是自己重写的方法
print(saly.catch())
