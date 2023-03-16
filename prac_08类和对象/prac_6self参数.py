"""结论：
        哪个对象调用，就保存哪个对象的引用地址
        self参数保存当前对象的引用地址

        """
import os
if os.path.exists("prac_6面向对象.py"):

    os.rename("prac_6面向对象.py","prac_6self参数.py")
class Cat:
    def eat(self):
        print("猫吃东西self方法",self)
    def drink(self,water):
        print("猫喝水方法")
        print("小猫喝%s",water)
orangecat=Cat()
orangecat.eat()
print(orangecat)

print("---"*20)

bosimao=Cat()
bosimao.eat()
print(bosimao)
# orangecat.drink()
