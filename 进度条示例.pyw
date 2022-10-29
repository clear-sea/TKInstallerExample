import os
import  tkinter
from time import sleep
from tkinter import ttk
root=tkinter.Tk()
#设置主窗口标题
root.title('进度条')
#设置主窗口的高宽
root['height']=200
root['width']=400
def Pro_Bar(root):
    #标签
    label=tkinter.Label(root,text='加密进度:',font=('黑体', 12))
    label.place(x=10,y=60)
    #进度条
    progressbar=ttk.Progressbar(root)
    progressbar.place(x=80,y=60)
    #设置进度条最大值为100
    progressbar['maximum']=100
    #设置进度条长度
    progressbar['length']=280
    def Value_Bar():
        for i in range(100):
            progressbar['value']=i+1
            sleep(0.1)
            root.update()
    #控制进度条启动按钮
    btn=tkinter.Button(root,text='启动',font=('黑体', 14),cursor='hand2',command=Value_Bar)
    btn.place(x=180,y=130)

if __name__=='__main__':
    Pro_Bar(root)
    root.mainloop()

