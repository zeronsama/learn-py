# 没看懂想让我干嘛

while True:
    print("查询能量请输入能量来源！退出程序请输入0")
    print("能量来源如下：")
    print("生活缴费、行走捐、共享单车、线下支付、网络购票")
    string = input()
    if string == "生活缴费":
        print("100g")
    elif string == "行走捐":
        print("200g")
    elif string == "共享单车":
        print("300g")
    elif string == "线下支付":
        print("400g")
    elif string == "网络购票":
        print("500g")
    elif string == "0":
        break
    else:
        continue
