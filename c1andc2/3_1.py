hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rates:")
r = float(rate)
if h<=40:
    pay=h*r
    print(pay)
else:
    over=h-40
    over_pay=(over*1.5*r)+(40*r)
    print(over_pay)
