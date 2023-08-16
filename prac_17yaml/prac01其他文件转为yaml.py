import yaml
import json

# 思路是 字符串参数化写入字典，字典通过yaml.dump写入yaml文件
a_data="woqu"
url_data = "huhu.com"

json_data = {
    "address": {
        "a": a_data,# 1 字符串参数化写入字典
        "city": "New York",
        "country": "USA",
        "zipcode": "10001"
    },
    "age": 30,
    "email": "johndoe@example.com",
    "hobbies": [
        "Reading",
    ],
    "is_student": True,
    "name": "John Doe",
    "option": False,
    "url": url_data

}
print(type(json_data))

yaml_file_path = "./input.yaml"
with open(yaml_file_path, 'w') as yaml_file:
    # 2 字典转写入yaml文件   yaml.dump 的作用是将 Python 数据结构（如字典、列表等）转换为 YAML 格式的字符串
    yaml.safe_dump(json_data, yaml_file, default_flow_style=False)






"""yaml转字典
import yaml

f = open('input.yaml', 'r')
ystr = f.read()

aa = yaml.load(ystr, Loader=yaml.FullLoader)
print(aa)
print(type(aa))"""
