import faker
from  faker import Faker
"""案例"""
#f=Faker(locale="zh_CN")
#print(f.pyint())

english_name = Faker(locale="en_US").unique.name() # 英文签名
print(english_name)
