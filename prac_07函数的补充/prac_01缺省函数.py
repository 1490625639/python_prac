import  os
open("prac_02多值参数.py", "w", encoding="utf_8")
# 所谓缺省函数，就是指定义函数时 函数参数有一个默认值的函数调用函数时
# 如果不给定一个值，就会使用默认值
def lack_def(name,age=22,mood="nice"):
    print(name)
    print(age)
    print(mood)

lack_def(name='我爱罗')
# 向形参变量传参时，建议加上形参变量名，这是关键字参数
lack_def(age=23,name='xiao',mood='good')