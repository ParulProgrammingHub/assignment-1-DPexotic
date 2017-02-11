n = int(input("enter days"))
years = n/360
months = (n % 360)/30
days = (n%360)%30
print("years:",years,"months:",months,"days:",days)
