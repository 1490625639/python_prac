# 在python中,类也是一个特殊的对象

class Person:
    def __init__(self):
        print("wef")
print(Person)
print(id(Person))

# 结论:类名,就是一个变量名,保存当前类对象的引用地址

# python中f一切皆对象,类模板也是一个对象,叫做类对象