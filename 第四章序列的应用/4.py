通话 = ("0分钟", "50分钟", "100分钟", "300分钟", "不限量")
流量 = ("0M", "500M", "1G", "5G")
短信 = ("0条", "50条", "100条")
套餐 = []

print("定制自己的手机套餐：")
print("A.请设置通话时长")
for index, item in enumerate(通话, 1):
    print(f"{index}." + item)
套餐.append(int(input("输入选择的通话时长编号：")) - 1)

print("B.请设置流量包")
for index, item in enumerate(流量, 1):
    print(f"{index}." + item)
套餐.append(int(input("输入选择的流量包编号：")) - 1)

print("C.请设置短信条数")
for index, item in enumerate(短信, 1):
    print(f"{index}." + item)
套餐.append(int(input("输入选择的短信条数编号：")) - 1)

print("您的手机套餐定制成功：", end="")
print(f"免费通话时长为{通话[套餐[0]]}/月，", end="")
print(f"流量为{流量[套餐[1]]}/月，", end="")
print(f"短信条数{短信[套餐[2]]}/月", end="")
