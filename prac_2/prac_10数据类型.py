# 使用type()函数查看数据类型  在python console中查看

"""数据类型分类
数字类型
    整形  int 非整形 float
    布尔类型  true false
非数字类型
    str 字符串
    list 列表
    tuple 元组
    dict 字典
    可变数据类型：list（列表）、dict（字典）、set（集合，不常用）

    不可变数据类型：数值类型（int、float、bool）、string（字符串）、tuple（元组）
        总结：可变数据类型更改值后，内存地址不发生改变。不可变数据类型更改值后，内存地址发生改变。
"""
name="张胜男"
type(name)
# type函数会自动判断数据类型   根据等号右边类型自动推导
