"""

新式类:以object为基类的类,一般是python3.x版本以上,推荐 如果没有指定父类,会默认使用object作为该类的基类

经典类:不以object为基类的类,一般是在python2.x版本以上, 不推荐   如果没有指定父类,则不会以object作为基类

dir类名    新式类会出很多object类里边的魔法属性和魔法方法,新式类默认继承object类


            旧 类没有object类的东西,默认不继承

        推荐定义类时,加上继承object类
        例:  class Animal(object):
                pass"""