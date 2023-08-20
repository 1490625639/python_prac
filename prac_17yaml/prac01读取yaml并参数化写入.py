import yaml
import json

"""
思路: 1.yaml转字典
      2.字符串参数化写入字典
      3.字典通过yaml.dump写入yaml文件   yaml.dump 的作用:将 Python 数据结构（如字典、列表等）转换为 YAML 格式的字符串
"""


def sort_test(name_data, country_data, age_data, url_data):
    yaml_file_path = "./input.yaml"
    # 1.yaml写成字典
    f = open(yaml_file_path, 'r')
    data = yaml.load(f.read(), Loader=yaml.FullLoader)
    print(f"读取的数据为:{data}")

    # 2.参数化写入字典
    data["address"]["name"] = name_data
    data["address"]["country"] = country_data
    data["age_data"] = age_data
    data["url"] = url_data
    # print(type(data))
    # print(data["address"]["name"])

    # 3.字典转写入yaml文件
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file, default_flow_style=False, sort_keys=False)
        print(f"写入后的数据为{data}")


if __name__ == '__main__':
    sort_test(name_data="ceshi", country_data="US", age_data=23, url_data="test.com")
