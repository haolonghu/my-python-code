j=0
for i in range(2000,3000+1):
    if((i%4==0 and i%100!=0 or i%400==0)):
        print(i ,end="  ")
        j=j+1
    if(j%18==0):print()
input()