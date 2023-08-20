# -*- coding: UTF-8 -*-
"""
Project ：python_prac 
File    ：prac_02markdown表格输出.py
Author  ：张以白
Date    ：2023/8/21 2:31 
"""
from datetime import datetime, timedelta

# 获取当前日期
current_date = datetime(2023, 8, 21)

# 生成Markdown表格
markdown_table = "|   时间    |   任务   | 进度 |\n|:---------:|:--------:|:----:|\n"

for _ in range(365):
    markdown_table += f"| {current_date.strftime('%Y-%m-%d')}|                 |      |\n"
    current_date += timedelta(days=1)

# 将生成的Markdown表格输出到文件或打印出来
print(markdown_table)