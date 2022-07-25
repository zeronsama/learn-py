print("-" * 13 + "跳一跳" + "-" * 13)
print("\n欢迎回来，请开始游戏……")
print("请输入（中心、音乐块、微信支付块）：")
score = 0
while True:
    string = input("请输入：")
    if string == "中心":
        score += 2
    elif string == "音乐块":
        score += 30
    elif string == "微信支付块":
        score += 10
    else:
        pass
    print("您的分数为：", score)
