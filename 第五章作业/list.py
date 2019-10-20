s=[9,7,8,3,2,1,55,6]
sum=0
print("元素个数为：",len(s))
print("最大值为：",max(s))
print("最小值为：",min(s))
for i in range(len(s)):
    sum=sum+s[i]
print("元素之和为：",sum)
print("平均值为：",sum/len(s))
input()