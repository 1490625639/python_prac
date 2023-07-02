import faker
from  faker import  Faker
# faker数据唯一性检验

def faker_test(n):
    l=[]
    f=Faker(locale="zh_CN")
    for i in range(n):
        name=f.unique.name()
        l.append(name)

    return f"总数{len(l)},去重后{len(set(l))}"
if __name__ == '__main__':
    print(faker_test(1000))
