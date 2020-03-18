n=int(input("please input the rows of Yang Hui Triangle: "))
print("\n")
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
for i in range(n):
    a[i][0]=a[i][i]=1
for i in range(2,n):
    for j in range(1,i):
        a[i][j]=a[i-1][j-1]+a[i-1][j]
for i in range(n):
    b=str()
    for j in range(i+1):
        b=b+str(a[i][j])+' '
    print(b.center(n*3),end='')    
    print('')
input()
