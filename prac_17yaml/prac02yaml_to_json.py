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
        datas = yaml.load(f, Loader=yaml.FullLoader)
    #jsonDatas = json.dumps(datas, indent=5)
    # 将字典的内容转换为json格式的字符串.实际不可用，因为转成字符串后有""
    with open("./new.json", "w", encoding="utf-8") as newfile:
        json.dump(datas, newfile, indent=5)

if __name__ == "__main__":
    yamlPath = './input.yaml'
    yaml_to_json(yamlPath)


