def merge(left,right):
     merged=[]
     i,j=0,0
     while i<len(left) and j< len(right):
          if left[i]<=right[j]:
               merged.append(left[i])
               i+=1
          else:
               merged.append(right[j])
               j+=1
     merged.extend(left[i:])
     merged.extend(right[j:])
     return merged

def mergeSort(a):
     if len(a)<=1:
          return a
     mid=len(a)//2
     left=mergeSort(a[:mid])
     right=mergeSort(a[mid:])
     return merge(left,right)
     
def main():
     import sys
     a=[int(i) for i in sys.argv[1:]]
     a1=mergeSort(a)
     print(a1)

if __name__=='__main__':main()
