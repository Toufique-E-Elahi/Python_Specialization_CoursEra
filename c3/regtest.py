import re
fnm=input('File Name: ')
fh=open(fnm,'r')
list=[]
for i in fh:
    num=re.findall('[0-9]+',i)

    if len(num)>=1:
        for x in range(len(num)):
            y=int(num[x])
            list.append(y)
    else:continue
print(sum(list))
