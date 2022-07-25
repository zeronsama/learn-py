from random import randint

standard_number = randint(1, 10)
guess_number = int(input("请输入1~10之间的任意一个数：\n"))
while True:
    if guess_number == standard_number:
        break
    elif guess_number < standard_number:
        guess_number = int(input("太小，请重新输入：\n"))
    elif guess_number > standard_number:
        guess_number = int(input("太大，请重新输入：\n"))
    else:
        pass
print("恭喜你，你赢了，猜中的数字是：", guess_number)
