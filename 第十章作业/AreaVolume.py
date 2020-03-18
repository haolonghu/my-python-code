def countr(r):
     r=float(r)
     PI=3.14
     m1=PI*r*r
     m2=(4/3)*PI*(r**3)
     return [m1,m2]

def main():
     r=float(input("请输入半径："))
     print("圆面积=%.2f"%countr(r)[0])
     print("球面积=%.2f"%countr(r)[1])

if __name__=='__main__':
     main()
