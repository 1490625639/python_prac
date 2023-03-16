class Gun:
    def __init__(self,type):
        "初始化方法"
        self.type=type
        # 子弹数量
        self.bullet_count=0
    def add_bullet_count(self,count):
        self.bullet_count+=count


    def shoot(self):
        #判断是否有子弹，没有子弹不能设计
        if self.bullet_count==0:
            print("你还没有子弹，先添加子弹吧")
            return
        self.bullet_count-=1
        print("%sbiubiubiu,剩余子弹数量为%d"%(self.type ,self.bullet_count))
# 使用枪支类模板创建对象
# ak=Gun("ak47")
# ak.bullet_count=2
# print(ak.shoot())
class Soldier:
    def __init__(self,name,gun=None):
        self.name=name
        self.gun=gun
        # 新兵默认没有枪

    def add(self, newnum):
        # if self.gun == None:
            #身份运算符
        if self.gun is None:
            # 用来比较两个对象的内存地址是否一致---是否是对同一个对象的引用用 is 或者 is not
            print("%s没有枪 不能射击" % self.name)
            return
        self.gun.add_bullet_count(newnum)

    def fire(self):
        if self.gun==None:
            print("%s没有枪 不能射击"%self.name)
            return
        # self.gun.add_bullet_count(2)
        # self.gun.shoot()
# 使用士兵类创建对象
ak47=Gun("步枪")
sanduo=Soldier("许三多",ak47)
sanduo.add(23)
sanduo.gun.shoot()

sanduo.gun.shoot()
sanduo.gun.shoot()