# 作用:可以做到测试代码,只会在测试的时候运行,被导入的时候不会运行
def table():
    for i in range  (1,10):
        for j in range  (1,10):
            print("%d*%d=%d\t"%(i,j,i*j),end="")
        print("")

if __name__ == '__main__':
    # 冷知识:if __name__ == '__main__': 可以通过main打出来
    table()
    print(__name__)
# 当前文件自己运行__name__会出来main
"""但是把这个包导入到别的地方去时,__name__出来的是模块名model
所以可以加一个判断,如果是我自己用,就可以运行函数,但是别人不会用"""