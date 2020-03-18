import tkinter as tk
import tkinter.scrolledtext as tst 
from tkinter import messagebox
from tkinter import filedialog
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.creatWidgets()
        self.creatMenu()
        root['menu']=self.menubar
        root.bind('<Button-3>',self.f_popup)
    def creatWidgets(self):
        self.textEdit=tst.ScrolledText(self,width=80,height=20)
        self.textEdit.grid(row=0,column=0,rowspan=6)
    def creatMenu(self):
        #创建子菜单
        self.menubar=tk.Menu(root)
        self.menufile=tk.Menu(self.menubar)
        self.menuedit=tk.Menu(self.menubar,tearoff=0)
        self.menuhelp=tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.menufile)
        self.menubar.add_cascade(label='Edit',menu=self.menuedit)
        self.menubar.add_cascade(label='Help',menu=self.menuhelp)
        #添加菜单项
        self.menufile.add_command(label='New',command=self.f_new)
        self.menufile.add_command(label='Open',command=self.f_open)
        self.menufile.add_command(label='Save',accelerator='^A',command=self.f_save)
        self.menufile.add_separator
        self.menufile.add_command(label='Exit',command=root.destroy)
        self.menuedit.add_command(label='Cut',command=self.f_cut)
        self.menuedit.add_command(label='Copy',command=self.f_copy)
        self.menuedit.add_command(label='Paste',command=self.f_paste)
        self.menuhelp.add_command(label='About',command=self.f_about)
    def f_new(self):
        self.textEdit.delete(1.0,tk.END)
    def f_open(self):
        self.textEdit.delete(1.0, tk.END)
        fname = tk.filedialog.askopenfilename(filetypes=[('Python源文件', '.py')])
        with open(fname, 'r', encoding='utf-8') as f1:
            str1 = f1.read()
        self.textEdit.insert(0.0, str1)
    def f_save(self):
        str1 = self.textEdit.get(1.0, tk.END)
        fname = tk.filedialog.asksaveasfilename(filetypes=[('Python源文件','.py')])
        with open(fname, 'w', encoding='utf-8') as f1:
            f1.write(str1)
    def f_about(self):
        tk.messagebox.showinfo('关于','版本V 1.0.1')
    def f_cut(self):
        try:
            str1 = self.textEdit.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.textEdit.clipboard_clear()
            self.textEdit.clipboard_append(str1)
            self.textEdit.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except:
            pass
    def f_copy(self):
        try:
            str1 = self.textEdit.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.textEdit.clipboard_clear()
            self.textEdit.clipboard_append(str1)
        except:
            pass
    def f_paste(self):
        str1 = self.textEdit.selection_get(selection='CLIPBOARD')
        try:
            self.textEdit.replace(tk.SEL_FIRST, tk.SEL_LAST, str1)
        except:
            self.textEdit.insert(tk.INSERT, str1)
    def f_popup(self, event):
        self.menuedit.post(event.x_root, event.y_root)
root=tk.Tk()
root.title('简易文本编辑器')
app=Application(master=root)
app.mainloop()
    
