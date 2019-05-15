from tkinter import *

class Movile():
    def on_start(self,event):
        self.x=event.x
        self.y=event.y
        print("Incio",self.rootx,self.rooty)

    def on_drag(self,event):
        self.rootx+=event.x-self.x
        self.rooty+=event.y-self.y
        self.widget.place(x=self.rootx,y=self.rooty)

    def on_drop(self,event):
        print("Final",self.rootx,self.rooty)
    
    def __init__(self,widget,rootx,rooty):
        self.widget=widget
        self.rootx=rootx
        self.rooty=rooty
        self.widget.bind("<ButtonPress-1>", self.on_start)
        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease-1>", self.on_drop)
        
    
 
window = Tk()
 
window.title("app")
 
window.geometry('350x200')

canvas1 = Canvas(window, width=200, height=100)
canvas1.configure(background="blue")
canvas1.place(x=0,y=0)

M1=Movile(canvas1,0,0)

canvas2 = Canvas(window, width=200, height=100)
canvas2.configure(background="red")
canvas2.place(x=100,y=100)

M2=Movile(canvas2,100,100)

 
window.mainloop()
