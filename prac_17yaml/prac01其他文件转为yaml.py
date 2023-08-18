import yaml
import json

# 思路是 字符串参数化写入字典，字典通过yaml.dump写入yaml文件   yaml.dump 的作用:将 Python 数据结构（如字典、列表等）转换为 YAML 格式的字符串
def sort_test(name_data,country_data,age_data,url_data):

    data = {
    "address": {
        "name": name_data,# 1 字符串参数化写入字典
        "city": "New York",
        "country": country_data,
        "zipcode": "10001"
    },
    "age": age_data,
    "email": "johndoe@example.com",
    "hobbies": [
        "Reading",
    ],
    "is_student": True,
    "url": url_data,
    "name": "John Doe"


}
    print(type(data))

    yaml_file_path = "./input.yaml"
    with open(yaml_file_path, 'w') as yaml_file:
        # 2 字典转写入yaml文件
        yaml.safe_dump(data, yaml_file, default_flow_style=False,sort_keys=False)
        print("成功！")

if __name__ == '__main__':
    sort_test(name_data="songxia", country_data="HK", age_data="20", url_data="test.com")





"""yaml转字典
import yaml

f = open('input.yaml', 'r')
ystr = f.read()

aa = yaml.load(ystr, Loader=yaml.FullLoader)
print(aa)
print(type(aa))"""
