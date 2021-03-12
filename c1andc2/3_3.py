try:
    inp= float(input("Enter Score between 0.0 to 1.0: "))

except:
    print('Error: Please type numerical value')
    quit()
if (inp>1.0) or (inp<0.0):
    print("Error: Wrong Data")
elif inp>=0.9:
    print('A')
elif inp>=0.8:
    print('B')
elif inp>=0.7:
    print('C')
elif inp>=0.6:
    print('D')
elif inp<0.6:
    print('D')
