import math
principal = float(input("请输入本金："))
rate = float(input("请输入年利率："))
year = float(input("请输入年份："))
amount = principal*(1+rate/100)**year
print(str.format("本金利率为: {0:2.2f}", amount))
input()
