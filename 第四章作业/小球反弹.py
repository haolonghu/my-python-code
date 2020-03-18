h=100.0
s=h/2
for i in range(1,10):
    h=h+2*s
    if(i==8):temp=s/2
    s=s/2
print(str.format("小球在第10次反弹时，共经过{0:.2f}米\n第十次反弹{1:.2f}米",h,temp)) 
input()