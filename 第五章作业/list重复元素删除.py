import numpy as np
l=[]
n=input("请输入列表内的元素，输入‘-1’结束:")
while n!='-1':
    l.append(n)
    n=input("请输入列表内的元素，输入‘-1’结束:")
a = np.unique(l)
print("原list为：",l)
print("删除重复元素后list为：",a)
input()
