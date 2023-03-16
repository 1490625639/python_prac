# python没有真正的私有
class Women:
    def __init__(self,name):
        self.name=name
        # 前置双下划线的是私有属性
        self.__age=23
        # 对外提供访问私有属性的接口 get/set

    def get_age(self):
        """获取私有属性值"""
        return  self.__age
    def set_age(self,new_age):
        if  new_age <= 0 or new_age>=150:
            print("输入年龄错误")
            return

        self.__age=new_age

    def eat(self):
        # 在内的内部可以访问私有属性
        print("%s是一个吃货，她今年%s岁了"%(self.name,self.__age))
        # 在类的内部可以通过self访问私有方法
        self.__secret()
    def __secret(self):
        print("个人秘密不透漏")
meinv=Women("我i")
# print(meinv.name)
# # 在类的外部无法直接访问到私有属性
# # print(meinv.__age)
# print(meinv.eat())
# # 在类的外部无法直接访问到私有方法
# # print(meinv.__secret)


print(dir(meinv))
# 没有真正意义上的私有,是通过方法重整的方式，
# 把私有属性和私有方法改了名字
# 可以通过名字重整的方式间接访问

# 私有属性：__私有属性名   改为了 _类名__私有属性名
print(meinv._Women__age)
# 私有方法: __私有方法名   改为了 _类名__私有方法名
print(meinv._Women__secret())

# 通过接口获取私有属性值
print(meinv.get_age())
# 通过接口设置私有属性值
meinv.set_age(90)
print(meinv.get_age())