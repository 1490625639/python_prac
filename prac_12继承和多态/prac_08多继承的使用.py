# 一个子类有多个父类     孩子继承父母优缺点
# 格式:     class 子类名(父类名1,父类名2,父类名3)
#             pass
class Horse:
    def __init__(self):
        self.name="马马马"
    def horse(self):
        print("我是小马die")
class Lv:
    def lv(self):
        print("我是小吕ma")

class Luozi(Horse,Lv):
    pass
xiaoluo=Luozi()
print(xiaoluo.horse())
print(xiaoluo.lv())
print(xiaoluo.name)
# 多继承中,子类可以访问所有父类的所有属性和所有方法,不包含私有属性和私有方法
