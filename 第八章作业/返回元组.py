s1=[9,7,8,3,2,1,55,6]
s2=["apple","pear","melon","kiwi"]
s3="TheQuickBrownFox"
def f(s):
    if s is list:
        s.sort()
        max1=max(s)
        min1=min(s)
        len1=len(s)
        return max1,min1,len1
    else:
        t=list(s)
        t.sort()
        max1=max(t)
        min1=min(t)
        len1=len(t)
        return max1,min1,len1
m=f(s1)
print("List= "+str(s1))
print("最大值=%s，最小值=%s，元素个数=%s\n"%(m[0],m[1],m[2]))
m=f(s2)
print("List= "+str(s2))
print("最大值=%s，最小值=%s，元素个数=%s\n"%(m[0],m[1],m[2]))
m=f(s3)
print("List= "+str(s3))
print("最大值=%s，最小值=%s，元素个数=%s\n"%(m[0],m[1],m[2]))
input()