def constellation(cmonth,cdate):
    sdate=[20,19,21,20,21,22,23,23,23,24,23,22]
    conts =['摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座']
    print(f"{cmonth}月{cdate}日星座为：",end="")
    if int(cdate)<sdate[int(cmonth)-1]:
        print(conts[int(cmonth)-1])
    else:
        print(conts[int(cmonth)])


month = int(input("请输入月份（例如：5）："))
date = int(input("请输入日期（例如：17）："))
constellation(cdate=date,cmonth=month)