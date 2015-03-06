# --coding:utf-8--

from Tkinter import *

def increaseRadius(even):
	global radius
	if radius < 100:
		radius += 2
	canvas.create_oval(100-radius,100-radius,100+radius,100+radius,tags="oval")

def decreaseRadius(event):
	global radius
	if radius > 2:
		radius -= 2
	canvas.create_oval(100-radius,100-radius,100+radius,100+radius,tags="oval")
	
root = Tk()

canvas = Canvas(root,bg="white",width = 200,height = 200)
canvas.bind("<Up>",increaseRadius)
canvas.bind("<Down>",decreaseRadius)
canvas.focus_set()
radius = 50
canvas.create_oval(100-radius,100-radius,100+radius,100+radius,tags="oval")
canvas.pack()

root.mainloop()