open("prac_04多值参数的组包和拆包.py", "w", encoding="utf-8")


# 多指参数累加和
def sumnum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


ret = sumnum(12, 234, 12, 2)

print(ret)
