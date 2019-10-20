import math
def getValue(b,r,n):
    v=b*(1+r)**n
    return v
b=float(input("请输入本金："))
r=float(input("请输入年利率："))
n=float(input("请输入年数："))
v=getValue(b,r,n)
print(str.format("最终的收益为：{0:2.2f}",v))
input()