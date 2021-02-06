# -*- coding = utf-8 -*-
# @Time : 2021-02-04 17:49
# @Author : 沉默
# @File : index.py
# @Software: PyCharm

import api.features as features
import tkinter as tk
import os
import sys

def main():
    # 路径初始化
    rootPath = os.path.split(os.path.realpath(__file__))[0]
    features.init(rootPath)

    root = tk.Tk();
    root.resizable(width=True,height=True)
    w,h = root.maxsize()
    root.geometry(str(w)+"x"+str(h)+"+0+0")#设置宽高
    # root.geometry("500x500+0+0")#设置宽高
    wBth = str(int(w/2))
    # rootFile = os.path.dirname(__file__);
    img_gif = tk.PhotoImage(file="./img/test1.png")
    left = tk.Button(root,text="左", width=wBth,height=str(h),font=("微软雅黑",100),image=img_gif,fg="black",bg="#557097",command=features.handleLeft)
    left.place(x=0, y=0)

    img_right = tk.PhotoImage(file="./img/test1.png")
    right = tk.Label(root,text="修复版", width=wBth,height=200,font=("微软雅黑",56),image=img_right,fg="black",bg="green")
    right.place(x=wBth, y=0)


    # 判断文件是否存在
    fileRoot = rootPath;  # 获取当前文件的路径  pyinstaller打包后才能识别的路径
    print(fileRoot)
    filePath = fileRoot + '/testpro/';  # 仅限当前文件创建文件
    #判断文件修复版的文件是否存在 file
    if not os.path.exists(filePath):
        filePath = fileRoot + '/weiton/';  # testpro不存在就是改名为weiton

    y = 200
    img_num = 0
    num = 1
    # img_png = tk.PhotoImage(file="./img/testpro.gif")
    img_png = []
    softwareName = 'sublime_text.exe'##打开的文件名
    for fileName in os.listdir(filePath):
        if fileName.split('.')[0] != '修复版':
            imgFile = filePath + fileName
            imgFile1 = imgFile.replace('\\','/')
            #test1.png按钮的图片
            img_png.append(tk.PhotoImage(file=imgFile1+"/test1.png"))
            ##command=lambda arg=(filePath + fileName):handleProcess(arg))  lambda防止生成按钮执行函数  arg把参数放入函数中
            tk.Button(root, text="1", width=wBth, height=200, font=("微软雅黑", 56), fg="black", image=img_png[img_num],bg="red",
                      command=lambda arg=(softwareName+'-----'+fileName):features.handleProcess(arg)).place(x=wBth, y=str(y * num))
            num = int(num) + 1
            img_num = int(img_num) + 1

    #去掉边框
    root.overrideredirect(False)

    #消息循环
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e+'1111')

