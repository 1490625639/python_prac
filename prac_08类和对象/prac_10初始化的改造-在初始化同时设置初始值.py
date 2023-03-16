"""import os
if os.path.exists("prac_9面向对象.py"):
    os.rename("prac_9面向对象.py","prac_9在初始化方法内部定义属性.py")
for i in range(10,12):
    open("prac_%d.py"%i,"w",encoding="utf-8")"""
# 在init方法内部使用 self.属性名=属性值就可以定义属性



"""本篇问题:类里面的初始值固定,但是实际上经常初始值需要改变,在todoz中有过思考,\
但是如果放在类外边定义,那么又回到了容易错乱的本质问题上
本次就是解决初始值需要不断改变的问题"""



"""class Cat:
    def __init__(self):
        print("初始化方法主要用来初始化数据")
        # 在类的内部添加属性
        self.name="saly"

        print("初始化方法定义属性成功")
    def eat(self):
        print("%s吃老八奥里给"%self.name)
# 创建对象
jvcat=Cat()
"""









# 在初始化同时设置初始值
# 一：在init方法中添加形参变量，def init(self,形参变量，*args)
# 二：在init方法中把形参保存为属性 self。属性名=形参
# 三：使用类模板创建对象时 一定要传参 对象=类名（参数）
#
#在init 中传入多个参数，一开始的 默认值，用多个参数进行替换
# self .name=参数name self.age=age ，达到了，多个属性在类内部被定义，
# 用self 调用eat 方法。
# 外部的对象在创建需要写入参数
#





class Dog:
    def __init__(self,new_name,oldage):
        self.name=new_name
        self.age=oldage

    def eat(self,food):
        print("%s岁的%s吃%s"%(self.age,self.name,food))
hh=Dog("史努比",12)
hh.eat("奥里给")













#TODO jvcat.name="cafo" 可以看到 如果在类的外部对属性定义的话,优先执行外部定义的,因为init函数内部是默认的
# 在类外部访问属性   对象名.属性名
"""print(jvcat.name)
jvcat.eat()"""
"""结论:对象的属性添加到对象的内存空间中去
    self保存的当前对象的引用地址"""