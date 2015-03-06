# -- coding:utf-8--
from Tkinter import *
def changeRelief():
	reliefList = ['flat','raised','sunken','groove','ridge']
	global reliefIndex
	label.config(relief=reliefList[reliefIndex%len(reliefList)])
	reliefIndex += 1
	
def changeColor(event):
	colorList = ['red','blue','yellow']
	global colorIndex
	label.config(fg=colorList[colorIndex%len(colorList)])
	colorIndex += 1

reliefIndex = 0
colorIndex = 0
	
root = Tk()

label = Label(root,text = "Welcome to python")
button1 = Button(root,text = "relief",command=changeRelief)
button2 = Button(root,text = "color")
button2.bind("<Button-1>",changeColor)

label.pack()
button1.pack(side=LEFT,anchor=CENTER,expand=YES)
button2.pack(side=LEFT,anchor=CENTER,expand=YES)


root.mainloop()

"""
GUI控件添加方法：
1、导入模块
2、创建主窗口
3、创建控件对象，由Tkinter的该控件相关方法来实现
4、pack()(布局器)是用来管理和显示组件的，它的参数
5、主窗口调用mainloop()进入主事件循环
"""