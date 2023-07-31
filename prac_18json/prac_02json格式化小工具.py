# -*- coding: UTF-8 -*-
"""
Project ：python_prac 
File    ：prac_02json格式化小工具.py
Author  ：张以白
Date    ：2023/7/27 2:30
使用tkinter+json实现格式化json的一个小工具
"""
import tkinter
from tkinter import *
import json
import math
from tkinter import ttk


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def json_format(self):
        try:
            self.data = self.entry1.get()
            # # 将JSON字符串解析为Python对象
            json_data = json.loads(self.data)  #
            # # load从文件中加载    loads是json字符串转成python结构
            # # dump写入文件        dumps是python结构转成json字符串

            with open("./test.json", "w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=5)
                print(json_data)
            #     # json.dump()将Python对象写入文件
            # 创建提示标签
            self.tip_label = Label(self, text="已经生成！存放test.json中")
            self.tip_label.pack()
        except:

            self.tip_label = Label(self, text="json格式有误！")
            self.tip_label.pack()

    #
    def creatWidget(self):
        self.label1 = Label(self, text="请输入json数据")
        self.label1.pack()
        v1 = StringVar()
        self.entry1 = Entry(self, textvariable=v1, width=40)
        v1.set("请输入你想格式化的json数据")
        self.entry1.pack()

        self.btn1 = Button(self, text="开始转换")
        # self.btn1.bind("<Button-1>",lambda event: self.turnover())
        self.btn1.bind("<Button-1>", lambda event: [self.json_format()])
        self.btn1.pack()

    def nextwedgit(self):
        print("调用后的按钮信息")
        self.label2 = Label(self, text="格式化后数据", width=10, height=1)
        self.label2.pack(side="left")

        # 创建一个Frame，用于在文本框和按钮之间创建空间
        spacer_frame = Frame(self)
        spacer_frame.pack(side="left")  # 使用padx来增加水平间距

        # 文本编辑区
        self.textpad = Text(self)
        self.textpad.pack()


if __name__ == '__main__':
    # json_format(data=shujv)
    root = Tk()
    # 设置窗口大小
    window_width = 500
    window_height = 400

    # 获取屏幕的宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算窗口在屏幕上的坐标
    x = math.floor((screen_width - window_width) / 2)
    y = math.floor((screen_height - window_height) / 2)

    # 设置窗口位置
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title("json格式化工具")
    # 设置窗口背景色彩
    root.configure(bg="#F2F2F2")  # 设置背景颜色为浅灰色

    app = Application(master=root)

    # 运行主循环
    root.mainloop()
