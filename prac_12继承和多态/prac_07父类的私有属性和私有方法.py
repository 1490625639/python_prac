class Father:
    def __init__(self):
        # 普通的属性,共有属性
        self.name = "老王"
        # 带有双下划线的是私有属性
        self.__pwd = 2323
    def get_t(self):
        return self.__pwd
    # 在类的内部对外提供访问私有属性的接口 get/set
    def get_pwd(self):
        return self.__pwd

    def set_pwd(self, newpwd):
        self.__pwd = newpwd

    def func(self):
        self.__secret()

    def eat(self):
        # 在类内可以使用self.私有属性名, 访问私有属性
        print("%s吃东西,ta的密码是%s" % (self.name, self.__pwd))

    def __secret(self):
        # 带有双下划线的是私有方法
        print("%s的个人秘密私有方法 密码是%d" % (self.name, self.__pwd))


class Son(Father):
    def run(self):
        print("小王喜欢泡")


xiaowang = Son()
print(xiaowang.name)
# 在类外无法直接访问私有属性
# print(xiaowang.__pwd)
print(xiaowang.eat())
# 在类外边,子类对象无法直接访问父类的私有方法
# print(xiaowang.__secret())

# 虽然是私有属性,但是我们知道python是通过名字重组的方式进行了修改,导致看不到
# 通过dir(对象名)查看改后的函数,但是不推荐

# 在类的内部提供了访问私有属性和私有方法的接口 get 和set
print(dir(xiaowang))

print(xiaowang.get_pwd())
print(xiaowang.set_pwd(1111))
print(xiaowang.get_pwd())
print(xiaowang.func())
# print(xiaowang.get_t())