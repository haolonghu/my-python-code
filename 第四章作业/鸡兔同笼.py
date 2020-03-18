h=int(input("请输入鸡和兔子的总数："))
while True:
    f=int(input("请输入鸡和兔子的总脚数(必须是偶数）："))
    if(f%2==0):break
r1=f/2-h
c1=h-r1
temp=0
for r2 in range(h+1):
    if(r2*4+(h-r2)*2==f):temp=1;break
if(temp==1):
    c2=h-r2
    print(str.format("方法一：鸡：{0}只,兔：{1}只",int(c1),int(r1)))
    print(str.format("方法二：鸡：{0}只,兔：{1}只",c2,r2))
else:
    print("方法一：无解，请重新运行测试！")
    print("方法二：无解，请重新运行测试！")
input()