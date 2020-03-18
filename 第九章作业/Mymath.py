import math
class Mymath:
     def __init__(self,r):
          #r=float(r)
          self.r=r
     def mymath(self):
          z1=2*math.pi*self.r
          m1=2*math.pi*(self.r**2)
          z2=(4/3)*math.pi*(self.r**3)
          m2=4*math.pi*(self.r**2)
          print("圆的周长=%.2f\n圆的面积=%.2f"%(z1,m1))
          print("球的表面积=%.2f\n球的体积=%.2f\n"%(m2,z2))
#test
r=float(input("请输入半径："))
a=Mymath(r)
a.mymath()
