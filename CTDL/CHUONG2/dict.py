x = {"name": "John", "age": 30}
print(x["name"])                # Kết quả: "John"
print(len(x))                   # Kết quả: 2
del x["age"]
print(x)                        # Kết quả: {"name": "John"}
print(x.keys())                 # Kết quả: dict_keys(["name"])
print(x.values())               # Kết quả: dict_values(["John"])
print(x.items())                # Kết quả: dict_items([("name", "John")])
