import random, decimal

print("-" * 10 + "模拟微信抢红包" + "-" * 10)
leftnum = decimal.Decimal(input("请输入要装入红包的总金额（元）："))
num = int(input("请输入红包的个数（个）："))
for i in range(1, num + 1):
    if i < num:
        thisone=random.uniform(0.01,float(leftnum - decimal.Decimal(num - i) * decimal.Decimal("0.01")))
        realthisone = decimal.Decimal(str(thisone)).quantize(decimal.Decimal("0.00"))
        leftnum -= realthisone
    else:
        realthisone = leftnum
    print(f"第{i}个红包：{realthisone}元")
