# 定义字典
dicts = {"username":"bigcatzx",'password':123456}

# 打印字典中的所有key
print(dicts.keys())

# 打印字典中所有value
print(dicts.values())

# 向字典中增加键/值对
dicts["age"] = 22

# 循环打印字典key和value
for k, v in dicts.items():
    print("dicts keys is %r" %k)
    print("dicts value is %r" %v)

# 删除键是'password'的项
dicts.pop('password')
print(dicts.keys())

# 打印字典以列表方法返回
print(dicts.items())