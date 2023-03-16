import os
if os.path.exists("prac_7面向对象.py"):
    os.rename("prac_7面向对象.py","prac_7在类的外边添加属性.py")
"""
        给对象添加属性有两种
            在类的外部添加属性             不推荐使用(可能造成属性找不到错误),因为对象属性的封装应该封装在类的内部
                对象名、属性名=属性值
                    添加完属性后访问方式有两种:内部 self.属性名     调用:self.方法名(参数)
                                            外部 对象名.属性名  调用: 对象名.方法名(参数)
            在类的内部添加属性       
"""
class Cat:

    def eat(self):
        # 在类的内部访问属性用self
        print("%s猫吃东西方法"%self.name)
        # 在类的内部访问方法也是用self
        self.drink("可乐")

    def drink(self,water):
        # print("猫喝水方法")
        print("小猫喝%s",water)
# 通过类模板创建对象
orangecat=Cat()
# 在类外部给对象添加属性
orangecat.name="saly"
# 在类的外部访问属性
print(orangecat.name)
"""这里直接调用方法就行,print(套用print)会出 none"""
orangecat.eat()


"""lazcat=Cat()
lazcat.name="懒橘猫"
lazcat.eat()"""
# 谁调用self 就保存哪个的引用地址



