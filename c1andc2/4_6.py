hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    print('Error: Wrong Input')
rate = input("Enter Rates:")
try:
    r = float(rate)
except:
    print('Error: Wrong Input')
def computepay(h,r):
    if h<=40:
        pay=h*r
        return pay
    else:
        over=h-40
        over_pay=(over*1.5*r)+(40*r)
        return over_pay
print('Pay',computepay(h,r) )
