# 书上要实时天气预报，随便找了个api，就这样吧，反正要求是用字符串的format()方法
import requests, json

format = "{0}\t{1}\t{2}\t{3}"
netdata = requests.get(
    "https://free-api.heweather.net/s6/weather/now?location=长沙&key=db86a5196f304e52a4369818c5182e60"
)
weadata = json.loads(netdata.text)["HeWeather6"]
weadata = weadata[0] 
print(
    format.format(
        weadata["update"]["loc"],
        "天气预报：" + weadata["now"]["cond_txt"],
        weadata["now"]["tmp"] + "℃",
        weadata["now"]["wind_dir"] + weadata["now"]["wind_sc"] + "级",
    )
)
