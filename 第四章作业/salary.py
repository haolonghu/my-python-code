salary=int(input("请输入有固定工资收入的党员的月工资: "))
if(salary<=400):f=salary*0.005
elif(salary<=600):f=salary*0.01
elif(salary<=800):f=salary*0.015
elif(salary<=1500):f=salary*0.02
else:f=salary*0.03
print(str.format("月工资={0},缴纳党费={1:.1f}",salary,f))
input()