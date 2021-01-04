import re
ret = re.match("www","www.example.com")
print(type(ret))
print(ret.group())
print(ret.span())
print(re.match("com","www.example.com"))
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M | re.I)
if matchObj:
    print("matchObj.group():",matchObj.group())
    print("matchObj.group(1):",matchObj.group(1))
    print("matchObj.group(2):",matchObj.group(2))
else:
    print("No match!!")