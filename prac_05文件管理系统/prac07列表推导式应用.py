# 利用列表推导式创建列表
import  random
def test1():
    print([x for x in  range(0,12)])
test1()

def test2():
    """创建一百个随机数用一行代码
    for后用了_没有用x,表示占位符,此处表示random.randit(0,100) 计数用
    """
    list=[ random.randint(0,100)  for _ in range(0,101)]
    print(list)
    # 后面表示次数 ,前面表示随机数

    # 列表推导式给列表增加值
    newlist=[x+100 for x in list]
    print(newlist)

    # 利用列表表达式将序列中的偶数拼接成列表
    str=[x for x in newlist if x%2==0]
    print(str)
test2()
#
# def test3():
#
