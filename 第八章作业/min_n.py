def min_n(a,b,*c):
    min=a
    if(a>b):min=b
    for i in c:
        if(i<min):min=i
    return min
print("最小的数字是："+str(min_n(8,2)))
print("最小的数字是："+str(min_n(16,1,7,4,15)))
print("最小的数字是："+str(min_n(8,9,43,432,3,12,9,5,7,8)))
input()