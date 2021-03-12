fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
except:
    print("Error: Wrong file input")
    quit()
list_hr=list()
for i in fh:
    if not i.startswith('From '):
        continue
    mail=i.rstrip().split()
    hr=mail[5].split(':')
    list_hr.append(hr[0])
#print(list_hr)
count=dict()
for list in list_hr:
    count[list]=count.get(list,0)+1
#print(sorted(count.items()))

for mail_hr,count_num in sorted(count.items()):
    print(mail_hr,count_num)
