import os
if os.path.exists("prac_9面向对象.py"):
    os.rename("prac_9面向对象.py","prac_9在初始化方法内部定义属性.py")
for i in range(10,12):
    open("prac_%d.py"%i,"w",encoding="utf-8")
# 在init方法内部使用 self.属性名=属性值就可以定义属性

class Cat:
    def __init__(self):
        print("初始化方法主要用来初始化数据")
        # 在类的内部添加属性
        self.name="saly"
        # print(self.name)
        print("初始化方法定义属性成功")
    def eat(self):
        print("%s吃老八奥里给"%self.name)
# 创建对象
jvcat=Cat()

#TODO jvcat.name="cafo" 可以看到 如果在类的外部对属性定义的话,优先执行外部定义的,因为init函数内部是默认的
# 在类外部访问属性   对象名.属性名
print(jvcat.name)
jvcat.eat()
"""结论:对象的属性添加到对象的内存空间中去
    self保存的当前对象的引用地址"""