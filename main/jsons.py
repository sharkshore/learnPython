import json

data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}

#json对象转化为字符串
jsonstr=json.dumps(data)

print(jsonstr)

dd=json.loads(jsonstr)
print(dd)
