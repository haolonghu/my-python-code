class Temp:
     @staticmethod
     def c2f(tc):
          tc=float(tc)
          tf=(tc*9/5)+32
          return tf
     @staticmethod
     def f2c(tf):
          tf=float(tf)
          tc=(tf-32)*5/9
          return tc
#test
print("1.从摄氏度到华氏度")
print("2.从华氏度到摄氏度")
print("3.退出")
choice=int(input("请选择："))
while (choice!=3):
     if choice==1:
          tc=float(input("请输入摄氏温度："))
          tf=Temp.c2f(tc)
          print("华氏温度为%.2f度"%tf)
          choice=int(input("请选择："))
     elif choice==2:
          tf=float(input("请输入华氏温度："))
          tc=Temp.f2c(tf)
          print("摄氏温度为%.2f度"%tc)
          choice=int(input("请选择："))
     else:
          print("选项不存在！")
          choice=int(input("请选择："))


