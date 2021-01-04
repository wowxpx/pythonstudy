import re
phone = "2004-959-559"
num = re.sub(r'#.*$',"",phone)
print("电话号码是：",num)
num = re.sub(r'\D',"",phone)
print("电话号码是：",num)
def double(matched):
    value = int(matched.group("value"))
    return str(value*2)
s = "A23G4HFD567"
print(re.sub("(?P<value>\d+)",double,s))