import re
result1 = re.findall(r'\d+',"baidu 123 google 456")
result2 = re.findall(r"\d+","baidu8800b123google456")

print(result1)
print(result2)