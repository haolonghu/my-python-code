import datetime
name=str(input("请输入您的名字："))
b=int(input("请输入您的出生年份："))
c=datetime.date.today().year-b
print("您好!{0}。您今年{1}岁".format(name,c))
input()