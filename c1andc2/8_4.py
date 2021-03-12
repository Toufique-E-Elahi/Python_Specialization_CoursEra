fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
except:
    print("Error: Wrong file input")
    quit()
list=list()
for i in fh:
    line=i.rstrip()
    words=line.split()
    for word in words:
        if word in list:
            continue
        list.append(word)
    #print(words)
    #list.append(words)
list.sort()
print(list)
