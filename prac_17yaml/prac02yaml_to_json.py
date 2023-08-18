# -*- coding: UTF-8 -*-
"""
Project ：python_prac
File    ：prac02yaml_to_json.py
Author  ：张以白
Date    ：2023/7/27 1:47
"""
import yaml
import json

# yaml文件内容转换成json格式
import yaml
import json

def yaml_to_json(yamlPath):
    with open(yamlPath, encoding="utf-8") as f:
        # 1 将YAML数据转换为Python字典或列表等数据结构。
        datas = yaml.load(f, Loader=yaml.FullLoader)
        print(f"数据：{datas}\n类型：{type(datas)}")
    # 2.将字典的内容转换为json格式
    with open("./new.json", "w", encoding="utf-8") as newfile:
        json.dump(datas, newfile, indent=5)

if __name__ == "__main__":
    yamlPath = './input.yaml'
    yaml_to_json(yamlPath)


