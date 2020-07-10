# 用户信息类
class User(object):
    def __init__(self, name, idCard, phone, cardInfo):
        # 用户姓名
        self.name = name
        # 用户身份证号
        self.idCard = idCard
        # 用户的手机号码
        self.phone = phone
        # 用户的卡的信息（卡号、密码、余额）
        self.cardInfo = cardInfo