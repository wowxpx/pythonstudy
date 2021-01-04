import requests
r = requests.get("https://httpbin.org/get")
print(r.text)
r = requests.get("https://httpbin.org/get",params={"key1":"value1","key2":"value2"})

print(r.text)
r = requests.post("https://httpbin.org/post",data={"key":"value"})
print(r.text)
r = requests.put("https://httpbin.org/put",data={"key": "value"})

print(r.text)
r = requests.delete("https://httpbin.org/delete")
print(r.text)
r = requests.head("https://httpbin.org/get")
print(r.text)
r = requests.options("https://httpbin.org/get")
print(r.text)