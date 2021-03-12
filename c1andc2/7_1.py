fname = input("Enter file name: ")
fh = open(fname,'r')
for i in fh:
    print(i.upper().rstrip())
