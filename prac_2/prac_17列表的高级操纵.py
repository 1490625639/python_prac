# 列表的长度统计       len(列表）
lit = [11, 22, 99, 55]
print(len(lit))
# 统计某数据在列表出现的次数
# 列表.count（数据）
print(lit.count(11))
 # 列表排序 列表. sort() 升序
lit.sort()
print(lit)
# 列表排序 降序 反转  列表.sort(reverse=true)
lit.sort(reverse=True)
print(lit)
# 列表逆序  列表.reverse()
ok=[1,2,3,4,5]
ok.reverse()
print(ok)
# 列表的拷贝 列表.copy()
no=ok.copy()
print(no)
print(id(ok))
print(id(no))
# 拷贝不能将地址拷贝过来