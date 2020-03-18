def quickSort(a,low,high):
     i=low
     j=high
     if i>=j:
          return a
     key=a[i]
     while i<j:
          while i<j and a[j]>key:
               j=j-1
          a[i]=a[j]
          while i<j and a[i]<=key:
               i=i+1
          a[j]=a[i]
     a[i]=key
     quickSort(a,low,i-1)
     quickSort(a,j+1,high)
def main():
     import sys
     a=[int(i) for i in sys.argv[1:]]
     quickSort(a,0,len(a)-1)
     print(a)
if __name__=='__main__':main()
