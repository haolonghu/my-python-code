a=[]
x=float(input("请输入一个实数，输入-1终止："))
while x!=-1:
	a.append(x)
	x=float(input("请输入一个实数，输入-1终止："))
print("计数：",len(a))
print("求和：",sum(a))
print("平均值：",sum(a)/len(a))