num=int(input("请输入n的值："))
#非递归计算
a=[1]
def fib1(n):
    if(n==2):a.append(1)
    if(n>2):
        a.append(1)
        for i in range(2,n):
            a.append(a[i-1]+a[i-2])
    return a
a=fib1(num)
temp1=0
print("\n非递归计算:")
for i in a:
    print("{0:>5}".format(i),end='')
    temp1=temp1+1
    if(temp1%10==0):print("\n")

#递归计算
def fib2(n):
    if(n<=0):return 0
    if(n==1 or n==2):return 1
    else:return fib2(n-1)+fib2(n-2)
print("\n递归计算:")
temp2=0
for i in range(1,num+1):
    print("{0:>5}".format(fib2(i)),end='')
    temp2=temp2+1
    if(temp2%10==0):print("\n")
input()



