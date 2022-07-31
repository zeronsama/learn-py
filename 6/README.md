# 第6章 函数

## 快速上手

```python
# 定义
def 函数名(参数1,参数2,参数3=默认值)
    """这里可以写函数的注释
    介绍一下功能什么的
    """
    return [Value] # 返回值
    pass

# 调用
# 位置参数
函数名(对应参数1,对应参数2) # 参数3使用默认值
# 关键字参数
函数名(参数2=XXX,参数1=XXX) # 可以不对应位置
```

python中函数的命名规范是`function_name`
- 全小写字母
- 单词间下划线当空格

## 进阶

- 默认参数必须指向**不可变对象**

    ```python
    def wrong_demo(obj=[]) #列表是可变对象
        pass #多次调用会出错

    def right_demo(obj=None)
        if obj==None:
            obj = []
    ```
    
- 可变参数的两种形式

    - `*parameter`

        接受多个参数，形成**元组**

    - `**parameter`

        接收`参数=赋值`的形式，形成**字典**

- 变量的作用域

    函数体内部使用全局变量，加上`global`修饰

## 匿名函数(lambad表达式)

```python
result = lambda arg1,argx... :expression
```

等价使用：
```python
def circle_area(r):
    return 3.14*r*r

circle_area = lambda r:3.14*r*r
```

一个案例：
[原代码](/4/3.py)
```python
TVshow = [
    ("Gu,hotm", 1.4),
    ("Tpdoth", 1.343),
    ("Mfwdm", 0.92),
    ("NCsbil", 0.862),
    ("It", 0.553),
    ("S", 0.411),
    ("EodA", 0.164),
    ("Tpsotnft", 0.259),
    ("Dd", 0.394),
    ("Ml", 0.562),
]
TVshow.sort(key=lambda list:list[1], reverse=True)
print("电视剧的收视率排行榜：")
for tuple in TVshow:
    print(f"《{tuple[0]}》  收视率：{tuple[1]}%")
```