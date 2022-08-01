# 第7章 面向对象程序设计 (OOP)

面向对象程序设计具有三大基本特征：封装、继承和多态

这里写的OOP不全，还得在实际运用中补充知识

## 类

```python
class ClassName:
    '''Help Document'''
    statement
```

python中类的命名规范是`ClassName`
- 首字母大写
- 后续单词首字母也大写

### `__init__`方法

类似构造函数，每次创建一个类的新实例就会执行它

```python
class Geese:
    '''大雁类'''
    def __init__(self): # self参数是一个指向实例本身的引用
        print("我是大雁类！")
wildGoose = Geese
```

### 类的成员

#### 实例方法

```python
class ClassName:
    def function_name(self,parameter): # 第一个参数必须是self
        pass

instance = ClassName()
instance.function_name(parameter) # 调用
```

#### 数据成员

```python
class ClassName:
    class_data = None # 公有类属性
    __private_class_data = None # 私有类属性
    def __init__(self):
        instance_data = None # 实例属性
        self.__private_class_data = None # 私有类内部调用

instance = ClassName()
print(instance.class_data) # 公有类属性的调用
print(instance._ClassName__private_class_data) # 私有类属性的调用
```

#### 属性

```python
class ClassName:
    @property # 装饰器
    def method_name(self):
        block
        return None
    @method_name.setter
    def method_name(self,value):
        block
        return value

instance = ClassName()
instance.method_name # 调用不用括号了
instance.method_name = "Value" # 使用setter方法
```

~~感觉是个坏文明，不清楚，先看看~~

#### 类的继承

```python
class DerivedClassName(BaseClassName1,Name2):
    block
```

派生类调用基类`__init__`方法，使用`super().__init()__`