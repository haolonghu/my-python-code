n=-1
sumfor=sumwhile=1
while(n<0):
    temp=n=int(input("请输入非负整数n："))
for i in range(1,n+1):
    sumfor*=i
while(n>0):
    sumwhile*=n
    n=n-1
print(str.format("for循环：{0}!={1}",temp,sumfor))
print(str.format("while循环：{0}!={1}",temp,sumwhile))
input()