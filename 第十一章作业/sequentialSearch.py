def search(alist,item):
     pos=0
     found=False
     while pos<len(alist) and not found:
          if(alist[pos])==item:
               found=True
          else:
               pos=pos+1
     return found
#test
import sys
a=[int(i) for i in sys.argv[1:]]
b=int(input("please input the number you wanna search:"))
print(search(a,b))
