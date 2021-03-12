fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
except:
    print("Error: Wrong file input")
    quit()
count=0
for i in fh:
    if not i.startswith('From '):
        continue
    count=count+1
    mail=i.rstrip().split()
    print(mail[1])

print("There were", count, "lines in the file with From as the first word")
