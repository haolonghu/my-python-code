def search(key,a):
     low=0
     high=len(a)-1
     while low<=high:
          mid=(low+high)//2
          if a[mid]<key:
               low=mid+1
          elif a[mid]>key:
               high=mid-1
          else:
               return mid
     return -1
import sys
b=[int(i) for i in sys.argv[1:len(sys.argv)-1]]
keys=int(sys.argv[len(sys.argv)-1])
temp=search(keys,b)
if temp!=-1:
     print("I have found it in the %d place"%(temp+1))
else:
     print("I can not found!")
