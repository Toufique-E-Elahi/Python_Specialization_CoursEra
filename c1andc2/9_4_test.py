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
    #count[list]=count.get(list,0)+1
    #Long way of previous comment
    if list in count:
        count[list]=count[list]+1
    else:
        count[list]=1
bigCount=None
bigMail=None
for count_mail in count:
    if bigCount is None or count[count_mail]>bigCount:
        bigMail=count_mail
        bigCount=count[count_mail]
    else:
        continue
print(bigMail,bigCount)
