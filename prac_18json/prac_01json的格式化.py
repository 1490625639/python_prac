# -*- coding: UTF-8 -*-
"""
Project ：python_prac 
File    ：prac_01json的格式化.py
Author  ：张以白
Date    ：2023/7/27 2:09 
"""
import json

"""json格式化用到indent参数"""
shujv = "{\n     \"a\": \"Hello, World!123\",\n     \"address\": {\n          \"a\": \"Hello, World!\",\n          \"city\": \"New York\",\n          \"country\": \"USA\",\n          \"zipcode\": \"10001\"\n     },\n     \"age\": 30,\n     \"email\": \"johndoe@example.com\",\n     \"hobbies\": [\n          \"Reading\",\n          \"Traveling\",\n          \"Cooking\"\n     ],\n     \"is_student\": true,\n     \"name\": \"John Doe\",\n     \"option\": false,\n     \"url\": \"https://baidu.com\"\n}"


def json_for(data):
    # 将JSON字符串解析为Python对象
    json_data = json.loads(data)
    # load从文件中加载    loads是json字符串转成python结构
    # dump写入文件        dumps是python结构转成json字符串

    with open("./test.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=5)
        # json.dump()将Python对象写入文件


if __name__ == '__main__':
    json_for(data=shujv)
