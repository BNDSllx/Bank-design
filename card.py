# 卡类
class Card(object):
    def __init__(self, cardStr, cardPwd, cardMoney):
        self.cardStr = cardStr  # 卡号
        self.cardPwd = cardPwd  # 卡密
        self.cardMoney = cardMoney  # 卡中余额

        self.isLock = False  # 卡号是否被锁