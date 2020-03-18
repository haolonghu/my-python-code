import random
a=set();b=set()
temp=random.randrange(0,11)
while len(a)!=temp:
     m=random.randrange(0,11)
     a.add(m)
while len(b)!=10-temp:
     m=random.randrange(0,11)
     b.add(m)
print("集合的内容，长度，最大值和最小值分别为：")
print(a,len(a),max(a),min(a))
print(b,len(b),max(b),min(b))
print("A和B的并集，交集和差集分别为：")
print(a|b,a&b,a-b)

