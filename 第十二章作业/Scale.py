import tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.creatWidgets()
    def creatWidgets(self):
        self.scaleFont=tk.Scale(self,from_=10,to=60,length=400,orient=tk.HORIZONTAL,command=self.changefont)
        self.scaleFont.set(20)
        self.scaleFont.pack()
        self.lblTitle=tk.Label(self,text="Hello",font=('Helvetica',20,'bold'))
        self.lblTitle.pack()
    def changefont(self,value):
        fontNew=('Helvetica',self.scaleFont.get(),'bold')
        self.lblTitle.config(font=fontNew)
root=tk.Tk()
root.title('设置字体大小')
root['width']=400
root['height']=50
app=Application(master=root)
app.mainloop()
