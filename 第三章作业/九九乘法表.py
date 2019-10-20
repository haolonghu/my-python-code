print("正常的九九乘法表：")
for i in range(1,10):
    s=""
    for j in range(1,10):
        s+=str.format("{0:1}*{1:1}={2:<2} ",i,j,i*j)
    print(s)
print("\n\n")
print("下三角的九九乘法表：")
for i in range(1,10):
    s=""
    for j in range(1,10):
        if(i<j):continue
        s+=str.format("{0:1}*{1:1}={2:<2} ",i,j,i*j)
    print(s)
print("\n\n")
print("上三角的九九乘法表：")
for i in range(1,10):
    s=""
    for j in range(1,10):
        if(i>j):
            s+=str.format("{0:7}","")
        else:
            s+=str.format("{0:1}*{1:1}={2:<2} ",i,j,i*j)
    print(s)
input()
