p = float(input("principle amount:"))
t = int(input("time:"))
r = int(input("interest percentage:"))

def ci(p,t,r):
    x = (1 +(r/100))**t
    i = (r * x - t)
    return i
print("compound interest:",ci(p,t,r))
