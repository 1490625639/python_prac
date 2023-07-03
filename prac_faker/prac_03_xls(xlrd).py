from faker import Faker
import xlrd
from xlutils.copy import copy
import xlwt
# 测试代码1231
# 使用xlrd库将数据写入到xls文件中

fake = Faker(locale='zh_CN')  # 创建一个使用中文数据的Faker对象

# 打开指定的Excel文件
rb = xlrd.open_workbook('existing_file.xls', formatting_info=True)

# 复制现有工作簿
wb = copy(rb)

# 获取要操作的工作表
ws = wb.get_sheet(0)  # 假设要操作的工作表索引为0

# 生成并写入随机数据 (起始行有列表下标)
for row in range(3, 11):  #range(1, 11): 假设需要生成10行数据，从第2行开始写入
    name = fake.unique.name() #中文成员姓名
    english_name = Faker(locale="en_US").unique.name() # 英文签名
    number = fake.unique.pyint()# 编号 这里用随机Int数字实现
    phone_number = fake.unique.phone_number()# 手机号
    email = fake.unique.email()

    print(f"{name}{english_name}{number}{phone_number}{email}")
#               行,列,数据
    ws.write(row, 0, name)
    ws.write(row, 1, english_name)
    ws.write(row, 2, number)
    ws.write(row, 4, phone_number)
    ws.write(row, 5, email)
    ws.write(row,6,"维森集团有限公司")
    ws.write(row,7,"系统管理员；印章管理员；流程管理员；模板管理员")
    ws.write(row,9,"qiyuesuo#2020")

# 保存修改后的Excel文件
wb.save('existing_file.xls')