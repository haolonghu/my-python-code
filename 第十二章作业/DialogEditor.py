import tkinter as tk
import tkinter.scrolledtext as tst
from tkinter import filedialog
from tkinter import colorchooser
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.creatWidgets()
    def creatWidgets(self):
        self.textEdit=tst.ScrolledText(self,width=80,height=20)
        self.textEdit.grid(row=0,column=0,rowspan=6)
        self.btnOpen=tk.Button(self,text="打开",command=self.funcOpen)
        self.btnOpen.grid(row=1,column=1)
        self.btnSave=tk.Button(self,text="保存",command=self.funcSave)
        self.btnSave.grid(row=2,column=1)
        self.btnColor=tk.Button(self,text="颜色",command=self.funcColor)
        self.btnColor.grid(row=3,column=1)
        self.btnQuit=tk.Button(self,text="退出",command=self.funcQuit)
        self.btnQuit.grid(row=4,column=1)
    def funcOpen(self):
        self.textEdit.delete(1.0,tk.END)
        fname=tk.filedialog.askopenfilename(filetypes=[('python源文件','.py')])
        with open(fname,'r',encoding='UTF-8') as f1:
            str1=f1.read()
        self.textEdit.insert(0.0,str1)
    def funcSave(self):
        str1=self.textEdit.get(1.0,tk.END)
        fname=tk.filedialog.asksaveasfilename(filetypes=[('python源文件','.py')])
        with open(fname,'w',encoding='UTF-8') as f1:
            f1.write(str1)
    def funcColor(self):
        t,c=tk.colorchooser.askcolor(title='askcolor')
        self.textEdit.config(bg=c)
    def funcQuit(self):
        root.destroy()
root=tk.Tk()
root.title('简易文本编辑器')
app=Application(master=root)
app.mainloop()
