class Sell:
    def __init__(self) -> None:
        Sell.sell_data = []
        for i in range(12):
            Sell.sell_data.append(None)

    def sell_goods(self, month, number, name):
        if Sell.sell_data[month - 1] is None:
            Sell.sell_data[month - 1] = []
        Sell.sell_data[month - 1].append((number, name))

    def show_data(self, month):
        if (
            not isinstance(month, int)
            or month < 0
            or month > 12
            or Sell.sell_data[month - 1] is None
        ):
            print("该月没有销售数据或者输入的月份有误！")
        else:
            print(f"{month}月份的商品销售明细如下：")
            for set in Sell.sell_data[month - 1]:
                print(f"商品编号：{set[0]}  商品名称：{set[1]}")

    def test(self):
        print(Sell.sell_data)


def question_set(obj: Sell):
    obj.sell_goods(2, "T0001", "笔记本电脑")
    obj.sell_goods(2, "T0002", "华为荣耀6X")
    obj.sell_goods(2, "T0003", "iPad")
    obj.sell_goods(2, "T0004", "华为荣耀V9")
    obj.sell_goods(2, "T0005", "MacBook")


if __name__ == "__main__":
    shop = Sell()
    question_set(shop)
    print("—" * 10 + "销售明细" + "—" * 10)
    while True:
        month = int(input("请输入要查询的月份（比如1、2、3等）："))
        shop.show_data(month)
        print()
