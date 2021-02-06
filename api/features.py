# -*- coding = utf-8 -*-
# @Time : 2021-02-06 16:46
# @Author : 沉默
# @File : features.py
# @Software: PyCharm
import tkinter as tk
from tkinter import messagebox
# from PIL import Image, ImageTk
import os
import shutil

# fileRoot = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))# 获取上一级文件路径
companyName = "微同生命"#公司名称

def init(val):
    global fileRoot
    fileRoot = val

def handleLeft():
    # 点击专业版
    # 判断文件是否存在
    print(fileRoot)
    filePath = fileRoot + '/weiton/';  # 仅限当前文件创建文件
    res = False
    for fileName in os.listdir(filePath):
        if fileName == '专业版.text':
            res = True
            break
    # 点击专业版按钮 文件也是专业版
    if res:
        # 如果是专业版就执行专业版下的exe文件
        software = filePath + 'index.text';
        os.system(software)
    else:
        # 如果不是修改文件名执行另外一个文件夹下的exe文件
        path = fileRoot + '/weiton/';
        if os.path.exists(path):
            os.rename(fileRoot + '/weiton/', fileRoot + '/testpro/')
            os.rename(fileRoot + '/testai/', fileRoot + '/weiton/')
            software = filePath + 'index.text';
            os.system(software)
        else:
            messagebox.showwarning('{name}'.format(name=companyName), '文件不存在')



#softwareName 打开的软件名
#softwareFile 软件上一次层的文件夹名
def handleProcess(val):
    softwareName = val.split('-----')[0]
    softwareFile = val.split('-----')[1]
    # 1.文件判断是否改为weiton
    # 判断文件是否存在

    filePath = fileRoot + '/weiton/';  # 仅限当前文件创建文件

    res = False
    for fileName in os.listdir(filePath):
        if fileName == '修复版.text':
            res = True
            break
    # 点击修复版按钮 文件也是修复版
    if res:
        # 如果是专业版就执行修复版下的exe文件
        software = filePath + 'index.text';
        os.system(software)
    else:
        # 如果不是修改文件名执行另外一个文件夹下的exe文件
        path = fileRoot + '/weiton/';
        if os.path.exists(path):
            os.rename(fileRoot + '/weiton/', fileRoot + '/testai/')
            os.rename(fileRoot + '/testpro/', fileRoot + '/weiton/')
            software = filePath + 'index.text';
            os.system(software)
        else:
            messagebox.showwarning('{name}'.format(name=companyName), '文件不存在')

    # 2.杀掉软件
    name = softwareName.split('.')

    res = ("{name}".format(name=name[0]) in os.popen(f'tasklist /FI "IMAGENAME eq "'+softwareName).read())
    ##判断进程是否被杀死 False是杀死了
    process = True

    if res:
        # 防止进程没有被杀死
        process = handleKill(process,softwareName)
    else:
        process = False
        print('{name}'.format(name=companyName),'该软件未打开')
        # messagebox.showwarning('{name}'.format(name=companyName), '该软件未打开')

    # 进程已杀死
    if not process:
        # 判断文件是否存在

        filePath = fileRoot + '/weiton/{name}/'.format(name=softwareFile);  # 仅限当前文件创建文件 test1动态文件 test2动态文件
        filePath = filePath.replace('\\', '/')

        file = 'index.text';#覆盖的文件   特别注意  特别注意  特别注意  特别注意  特别注意
        newFile = "F:/image/20200203/index.text"#被覆盖的文件路径
        fileFinally = handleCoverFile(filePath, file,newFile)
        ##判断文件是否覆盖和备份成功
        if fileFinally:
            #3.打开对应软件
            appPath = "E:/Sublime Text 3/sublime_text.exe";
            openFinally = openApp(appPath)
            if not openFinally:
                messagebox.showwarning('{name}'.format(name=companyName), '打开程序失败')
        else:
            messagebox.showwarning('{name}'.format(name=companyName), '覆盖文件失败')

        print('成功')

#防止进程没有被杀死
def handleKill(process,softName):
    if process:
        process = os.system('TASKKILL /F /IM {name}'.format(name=softName))
        return process
    else:
        handleKill(process,softName)

#备份文件和覆盖文件
def handleCoverFile(filePath,file,newFile):
    # ##判断文件是否存在 存在就覆盖文件
    if os.path.exists(filePath):
        # os.mkdir(filePath)
        oldFile = filePath + file  # 配方文件路径
        copyRes = shutil.copy(oldFile, newFile)
        if not copyRes:
            return False
        else:
            return True
    else:
        return False

#打开软件
def openApp(appPath):
    ##判断文件是否存在
    if os.path.exists(appPath):
        return os.startfile(appPath) == None
    else:
        return False