import math
a=float(input("请输入a："))
b=float(input("请输入b："))
c=float(input("请输入c："))
if(a==0 and b==0):print("此方程无解！")
elif(a==0 and b!=0):
    x=float(-c/b)
    print("此方程的解为：%.1f"%x)
else:
    d=b*b-4*a*c
    if(d==0):
        x1=x2=float(-b/2*a)
        print("此方程有两个相等实根：%.1f"%x1)
    elif(d>0):
        x1=float(-b/(2*a)+math.sqrt(d)/(2*a))
        x2=float(-b/(2*a)-math.sqrt(d)/(2*a))
        print(str.format("此方程有两个不等实根：{0:.1f} 和 {1:.1f}",x1,x2))
    else:
        realPart=-b/(2*a)
        imagPart=math.sqrt(abs(d))/(2*a)
        print(str.format("此方程有两个不等实根：{0:.1f}+{1:.1f}i 和 {0:.1f}-{1:.1f}i",realPart,imagPart))
    
input()