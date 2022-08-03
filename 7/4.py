class Cinema:  # 跟实际影院逻辑不同，题目问题
    movies = ["环太平洋：雷霆再起", "头号玩家", "红海行动"]
    shows = ["9:30", "10:40", "12:00"]
    seats = ["10-01", "10-02", "10-03", "10-04"]


class Ticket(Cinema):
    def __init__(self) -> None:
        print("请选择正在上映的电影", end="：")
        for index, name in enumerate(Cinema.movies, 1):
            print(f"{index}、《{name}》", end=" ")
        self.movie = input("\n已选电影：")
        print("请选择电影播放场次", end="：")
        for index, name in enumerate(Cinema.shows, 1):
            print(f"{index}、{name}", end=" ")
        self.show = input("\n电影场次：")
        print("请选择座位剩余座位", end="：")
        for pos in Cinema.seats:
            print(pos, end=" ")
        self.seat = input("\n选择座位：")

    def info(self):
        print(
            f"""电影：《{self.movie}》
播出时间：{self.show}
座位：{self.seat}
"""
        )

print("开摆了，不想写输出格式了")
ticket = Ticket()
print("\n正在出票。。。\n")
ticket.info()
