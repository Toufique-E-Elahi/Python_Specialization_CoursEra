fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
except:
    print("Error: Wrong file input")
    quit()
list_mail=list()
for i in fh:
    if not i.startswith('From '):
        continue
    mail=i.rstrip().split()
    list_mail.append(mail[1])
#print(list_mail)
count=dict()
for list in list_mail:
    count[list]=count.get(list,0)+1
bigCount=None
bigMail=None
for count_mail,count_num in count.items():
    if bigCount is None or count_num>bigCount:
        bigMail=count_mail
        bigCount=count_num
    else:
        continue
print(bigMail,bigCount)
