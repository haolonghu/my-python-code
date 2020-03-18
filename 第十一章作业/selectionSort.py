def selectionSort(a):
     for i in range(0,len(a)):
          m=i
          for j in range(i+1,len(a)):
               if(a[j]<a[m]):
                    m=j
          a[i],a[m]=a[m],a[i]
def main():
     import sys
     a=[int(i) for i in sys.argv[1:]]
     selectionSort(a)
     print(a)

if __name__=='__main__':main()
     
