import tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        optionList=range(10,61,4)
        self.vFont=tk.StringVar()
        self.vFont.set(14)
        self.optionMenuFont=tk.OptionMenu(self,self.vFont,*optionList)
        self.optionMenuFont.pack(side=tk.LEFT)
        self.buttonFont=tk.Button(self,text="改变字体",command=self.changefont)
        self.buttonFont.pack(side=tk.LEFT)
        self.lblTitle=tk.Label(self,text="hello",font=('Helvetica',14,'bold'))
        self.lblTitle.pack(side=tk.LEFT)
    def changefont(self):
        fontNew=('Helvetica',self.vFont.get(),'bold')
        self.lblTitle.config(font=fontNew)
root=tk.Tk()
root.title('设置字体大小')
root['width']=400
root['height']=50
app=Application(master=root)
app.mainloop()
