import sys
n=int(sys.argv[1])
power=1
i=0
f=open("out.log","w")
sys.stdout=f
while i<=n:
	print(str(i),' ',str(i*2),' ',str(power))
	power=2*power
	i=i+1
print("done!")
	