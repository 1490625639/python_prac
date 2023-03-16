score = int(input('请输入成绩'))
if score < 30:
    print('成绩为差劲')
elif score < 60:
    print('成绩不及格')
elif 60 < score < 80:
    print('成绩及格了')
else:
    print('成绩优秀')
# 使用alt 加shift加enter 因为第一个已经小于三十分了 所以第二个没有必要加上 大于三十 肯定大于