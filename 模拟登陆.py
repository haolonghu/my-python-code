from getpass import getpass
from hashlib import md5
username=input("用户名：")
pass1=str(getpass("密码："))
hl =md5()
passwd=pass1+"Huhaolong!.;\iidk)9"
hl.update(passwd.encode(encoding='utf-8'))
if username=="hhl" and hl.hexdigest()=="84e069801fef1a7ba65b98e6563f3cd9":
    print("登陆成功！")
else:
    print("用户名或密码错误!")
input()