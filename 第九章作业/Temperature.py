class Temperature:
     def __init__(self,degree):
          self.degree=degree
     def ToFahrenheit(self):
          C=float(self.degree)
          F=(C*9/5)+32
          return F
     def ToCelsius(self):
          F=float(self.degree)
          C=(F-32)*5/9
          return C

c1=float(input("请输入摄氏温度："))
c=Temperature(c1)
fc=c.ToFahrenheit()
print("摄氏温度=%.1f,华氏温度=%.1f"%(c1,fc))
f1=float(input("请输入华氏温度："))
f=Temperature(f1)
cf=f.ToCelsius()
print("华氏温度=%.1f,摄氏温度=%.1f"%(f1,cf))
