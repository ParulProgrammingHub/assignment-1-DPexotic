p = float(input("principle amount:"))
t = int(input("time:"))
r = int(input("interest rate:"))

def interest(p,t,r):
    si = p * (1 + ((r*t)/100))
    print("simple interest:",si)
interest(p,t,r)

