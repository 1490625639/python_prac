# -*- coding: UTF-8 -*-
"""
Project ：python_prac 
File    ：prac_01日期输出.py
Author  ：张以白
Date    ：2023/8/21 2:25 
"""
from datetime import datetime, timedelta

# 获取当前日期
current_date = datetime(2023, 8, 21)

# 输出未来一年的日期
for _ in range(365):
    print(current_date.strftime('%Y-%m-%d'))
    current_date += timedelta(days=1)