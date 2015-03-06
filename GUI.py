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
GUI�ؼ���ӷ�����
1������ģ��
2������������
3�������ؼ�������Tkinter�ĸÿؼ���ط�����ʵ��
4��pack()(������)�������������ʾ����ģ����Ĳ���
5�������ڵ���mainloop()�������¼�ѭ��
"""