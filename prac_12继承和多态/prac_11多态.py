# 多态：不同的子类对象调用相同的父类方法名，产生不同的执行结果
class Dog:
    def __init__(self,name):
        self.name=name
    def game(self):
        print("普通狗是简单的玩耍")
class XiaoTianDog(Dog):
    def __init__(self,name):
        self.name=name
    def game(self):
        print("哮天犬在天上玩耍")
class Person:
    def __init__(self,name):
        self.name=name
    def paly_withdog(self,dog):
        print("%s和%s一起玩"%(self.name,dog.name))
            # 狗调用game方法
            # 不同的的对象调用同一个方法,产生不同的结果状态称为多态
        dog.game()
wagncai=Dog("jiawang")

changwei=Person("常委")

xtq=XiaoTianDog("小天小犬")

print(changwei.paly_withdog(wagncai))
print("-----"*20)
print(changwei.paly_withdog(xtq))

"""多态成立的三个条件:1 要有继承
                2:要有方法的重写
                3:要有父类的对象或子类的对象作为方法的参数
                python中的多态时"鸭子模型",格式要求没那么严格
                """