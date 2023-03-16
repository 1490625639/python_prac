class Person(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("%s喜欢吃东西"%self.name)
ok=Person("xixi")
print(id(ok.eat()))