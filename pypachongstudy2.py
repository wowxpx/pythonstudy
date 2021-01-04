import re
ret = re.search("www","www.aaa.com www.bbb.com")
print(type(ret))
print(ret.group())
print(ret.span())
print(re.search("cn","www.aaa.com www.bbb.com"))

line = "Cats are smarter than dogs";
searchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)
if searchObj:
    print("searchObj.group():",searchObj.group())
    print("searchObj.group(1):",searchObj.group(1))
    print("searchObj.group(2):",searchObj.group(2))
else:
    print("Nothing found!!")