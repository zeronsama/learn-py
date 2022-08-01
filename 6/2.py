def combo(name: str) -> str:
    if name == "考神套餐":
        return "13元"
    elif name == "单人套餐":
        return "9.9元"
    elif name == "情侣套餐":
        return "20元"
    else:
        pass


set = ["考神套餐", "单人套餐", "情侣套餐"]
print("米粉店套餐如下:", end="")
for index, item in enumerate(set, start=1):
    print(f"{index}.{item}", end=" ")
print()
for item in set:
    print(f"{item}{combo(item)}")
