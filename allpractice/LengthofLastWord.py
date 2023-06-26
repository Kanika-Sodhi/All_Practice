import re

name = "  Hello   python  "

nname = re.sub(' +', " ", name)
cleanname = nname.strip()
splitword = cleanname.split(' ')
print(len(splitword[1]))
# lstlen = len(splitword)-1
# print(len(splitword[lstlen]))
