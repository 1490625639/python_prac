class Horse:
    def __init__(self):
        self.name="马马马"
    def work(self):
        print("xiao小马泡泡")
class Lv:
    def work(self):
        print("xiao小吕泡泡")

class Luozi(Horse,Lv):
    pass

# 使用骡子类创建对象
xiaoluo=Luozi()
# 当调用了相同的方法名时候
print(xiaoluo.work())

# # MRO方法搜索顺序 : 类名.__mro__ 解析方法顺序表,然后他的方法搜索顺序,是按照mro的输出顺序,从左到右进行检索
# print(Luozi.__mro__)
# (<class '__main__.Luozi'>, <class '__main__.Horse'>, <class '__main__.Lv'>, <class 'object'>)