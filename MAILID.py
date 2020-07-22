import re
x='^[a-z]+[\._]?[a-z]+[@]\w+[.]\w{2,3}$'
vname=input("mailid")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid")
else:
    print("invalid mailid")