import math
r=float(input("请输入球的半径："))
area=4*math.pi*r**2
volume=(4*math.pi*r**3)/3
print(str.format("球的表面积是:{0:2.2f},体积为:{1:2.2f}",area,volume))
input()