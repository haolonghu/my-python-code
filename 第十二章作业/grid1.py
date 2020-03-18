from tkinter import *
root=Tk();root.title("登陆")
Label(root,text="用户名").grid(row=0,column=0)
Entry(root).grid(row=0,column=1,columnspan=2)
Label(root,text="密码").grid(row=1,column=0)
Entry(root,show="*").grid(row=1,column=1,columnspan=2)
Button(root,text="登陆").grid(row=3,column=1,sticky=E)
Button(root,text="取消").grid(row=3,column=2,sticky=W)
root.mainloop()
