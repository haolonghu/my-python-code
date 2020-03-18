import tkinter as tk
from tkinter import messagebox
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.creatWidget()
    def creatWidget(self):
        self.lblTitle=tk.Label(self,text="个人信息调查")
        self.lblName=tk.Label(self,text="姓名")
        self.lblSex=tk.Label(self,text="性别")
        self.lblHobby=tk.Label(self,text="爱好")
        self.lblTitle.grid(row=0,column=0,columnspan=4)
        self.lblName.grid(row=1,column=0)
        self.lblSex.grid(row=2,column=0)
        self.lblHobby.grid(row=3,column=0)
        #文本框
        self.entryName=tk.Entry(self)
        self.entryName.grid(row=1,column=1,columnspan=3)
        #单选按钮
        self.vSex=tk.StringVar()
        self.vSex.set('M')
        self.radioSexM=tk.Radiobutton(self,text="男",value='M',variable=self.vSex)
        self.radioSexF=tk.Radiobutton(self,text="女",value='F',variable=self.vSex)
        self.radioSexM.grid(row=2,column=1)
        self.radioSexF.grid(row=2,column=2)
        #复选框
        self.vHobbyMusic=tk.IntVar()
        self.vHobbySports=tk.IntVar()
        self.vHobbyTravel=tk.IntVar()
        self.vHobbyMovie=tk.IntVar()
        self.checkboxMusic=tk.Checkbutton(self,text="音乐",variable=self.vHobbyMusic)
        self.checkboxSports=tk.Checkbutton(self,text="运动",variable=self.vHobbySports)
        self.checkboxTravel=tk.Checkbutton(self,text="旅游",variable=self.vHobbyTravel)
        self.checkboxMovie=tk.Checkbutton(self,text="影视",variable=self.vHobbyMovie)
        self.checkboxMusic.grid(row=3,column=1)
        self.checkboxSports.grid(row=3,column=2)
        self.checkboxTravel.grid(row=3,column=3)
        self.checkboxMovie.grid(row=3,column=4)
        #按钮
        self.btnOk=tk.Button(self,text="提交",command=self.funcOk)
        self.btnOk.grid(row=4,column=1,sticky=tk.E)
        self.btnCancel=tk.Button(self,text="取消",command=root.destroy)
        self.btnCancel.grid(row=4,column=2,sticky=tk.W)

    def funcOk(self):
        strSex='男' if (self.vSex.get()=='M') else '女'
        strMusic=self.checkboxMusic['text'] if (self.vHobbyMusic.get()==1) else''
        strSports=self.checkboxSports['text'] if (self.vHobbySports.get()==1) else''
        strTravel=self.checkboxTravel['text'] if (self.vHobbyTravel.get()==1) else''
        strMovie=self.checkboxMovie['text'] if (self.vHobbyMovie.get()==1) else''
        str1=self.entryName.get()+'您好:\n'
        str1+="您的性别是："+strSex+'\n'
        str1+="您的爱好是："+strMusic+' '+strSports+' '+strTravel+' '+strMovie
        tk.messagebox.showinfo("个人信息",str1)

root=tk.Tk()
root.title('个人信息调查')
app=Application(master=root)
app.mainloop()
