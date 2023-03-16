# 函数的返回值本质上也是引用的传递
def fanhui():
    num1=10
    num2=20
    ret=num1+num2
    print(f"num1的值为{num1},num2的值为{num2}")
    print(num1,id(num1),num2,id(num2))
    print(f"最终结果为{ret} 地址为{id(ret)}")
    return ret
lastret=fanhui()
print(f"看看返回值调用后结果{lastret,id(lastret)}")
# 结论：函数的返回值，本质上也是引用的传递
