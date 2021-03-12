largest=None
smallest=None
count=0
while True:
    inp=input('Enter a number: ')
    if inp=='done':
        break
    try:
        num=int(inp)
    except:
        print('Invalid input')
        continue
    if largest is None and smallest is None:
        largest=num
        smallest=num
        #print(largest,smallest)
    if largest<num:
        largest=num
    if smallest>num:
        smallest=num
print('Maximum is',largest)
print('Minimum is',smallest)
