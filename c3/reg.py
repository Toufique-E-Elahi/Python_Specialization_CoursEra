import re
fnm=input('File Name: ')
fh=open(fnm,'r')
#List_Comprehension
print(sum([int(x) for x in re.findall('[0-9]+',fh.read())]))
