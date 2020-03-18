j=0
Sn=0
n=int(input("请输入要计算到哪一位（即n为多少）："))
for i in range(1,abs(n)+1,2):
    if(j%2==0):i=i
    else:i=-i
    j=j+1
    Sn=i+Sn
print("Sn=%d"%Sn)
input()