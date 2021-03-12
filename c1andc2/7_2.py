fname = input("Enter file name: ")
fh = open(fname,'r')
count=0;
add=0
for i in fh:
    if not "X-DSPAM-Confidence:" in i:
        continue
    count=count+1
    find=i.find('0.')
    add=add+float(i[find:].rstrip())
avg=add/count
print('Average spam confidence:',avg)
