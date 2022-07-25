print("—" * 6 + "10086查询功能" + "—" * 6)
info = """
键入1，查询当前余额
键入2，查询当前剩余流量
键入3，查询当前剩余通话
键入0，退出自助查询系统！"""
remaining_credit = 999  # 元
remaining_mobile_data = 5  # G
remaining_call_duration = 189  # 分钟
print(info)
while True:
    choose = int(input())
    if choose == 1:
        print(f"当前余额为：{remaining_credit} 元")
    elif choose == 2:
        print(f"当前剩余流量为：{remaining_mobile_data} G")
    elif choose == 3:
        print(f"当前剩余通话为：{remaining_call_duration} 分钟")
    elif choose == 0:
        print("退出自助查询系统！")
        break
