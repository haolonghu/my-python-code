import tkinter as tk
from tkinter import messagebox
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.creatWidgets()
    def creatWidgets(self):
        self.lblEmail=tk.Label(self,text="用户名")
        self.lblPass1=tk.Label(self,text="密码")
        self.lblPass2=tk.Label(self,text="确认密码")
        self.lblDesc=tk.Label(self,text="自我介绍")
        self.lblEmail.grid(row=0,column=0,sticky=tk.E)
        self.lblPass1.grid(row=1,column=0,sticky=tk.E)
        self.lblPass2.grid(row=2,column=0,sticky=tk.E)
        self.lblDesc.grid(row=3,column=0,sticky=tk.NE)
        self.entryEmail=tk.Entry(self)
        self.entryPass1=tk.Entry(self,show="*")
        self.entryPass2=tk.Entry(self,show="*")
        self.textDesc=tk.Text(self,width=20,height=5)
        self.entryEmail.grid(row=0,column=1,columnspan=2)
        self.entryPass1.grid(row=1,column=1,columnspan=2)
        self.entryPass2.grid(row=2,column=1,columnspan=2)
        self.textDesc.grid(row=3,column=1,columnspan=2)
        self.btnOK=tk.Button(self,text="注册",command=self.funcOK)
        self.btnOK.grid(row=4,column=1,sticky=tk.E)
        self.btnCancel=tk.Button(self,text="取消",command=root.destroy)
        self.btnCancel.grid(row=4,column=2,sticky=tk.W)
    def funcOK(self):
        pw1=self.entryPass1.get()
        pw2=self.entryPass2.get()
        if(pw1==pw2):
            str1='欢迎注册\n'
            str1+="您的账户为："+self.entryEmail.get()+'\n'
            str1+="您的特长为：\n"+self.textDesc.get(0.0,tk.END)
            tk.messagebox.showinfo("注册",str1)
        else:
            str2='两次密码不同，请重新输入！\n'
            tk.messagebox.showinfo("Error!",str2)
root=tk.Tk()
root.title("新用户注册")
app=Application(master=root)
app.mainloop()



