class Credit:
    def __init__(self, number, password=None) -> None:
        Credit.number = number
        if password is None:
            Credit.password = 123456
            print(f"信用卡{Credit.number}的默认密码为{Credit.password}")
        else:
            Credit.password = password
            print("重置信用卡%d的密码为%d" % (Credit.number, Credit.password))


card1 = Credit(4013735633800642)
card2 = Credit(4013735633800642, 168779)
