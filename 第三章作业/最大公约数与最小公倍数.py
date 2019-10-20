import random
temp1=m=random.randint(0,100000)
temp2=n=random.randint(0,100000)
print(str.format("整数1={0}，整数2={1}",m,n))
if(m<n):n,m=m,n
r=m%n
while(r!=0):
    m=n
    n=r
    r=m%n
max=int(temp1*temp2/n)
print(str.format("最大公约数={0}，最小公倍数={1}",n,max))
input()
