maths = (input("enter marks:")
physics = (input("enter marks:")
chem = (input("enter marks:")
com = (input("enter marks:")
ps = (input("enter marks:")
mean = (maths + physics + chem + com + ps)/5
per = mean *100
print ("mean ="%mean)
if(per>35):
    print("pass")
else:
    print ("fail")
