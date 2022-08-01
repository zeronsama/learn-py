class SmartPhone:
    """
    智能手机类，默认语言是英文
    """

    def __init__(self, language=None):
        if language is None:
            SmartPhone.language = "英文"
            print("智能手机的默认语言是", SmartPhone.language)
        else:
            SmartPhone.language = language
            print("将智能手机的默认语言设置为", SmartPhone.language)


phone1 = SmartPhone()
phone2 = SmartPhone("中文")
