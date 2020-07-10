# 各种操作类
import random
from card import Card
from user import User
import time


class ATM(object):
    # 初始化
    def __init__(self, allUsersInfo):
        # 将所有用户信息传递过来，以便后续操作
        self.allUsersInfo = allUsersInfo  # 卡号 ：用户

    # 确认密码
    def checkPwd(self, realPwd):
        myList = [3, 2, 1, 0]
        for i in myList:
            # 如果密码输入错误超过三次
            if i == 0:
                return False
            rePass = input('请再次输入密码：')
            if realPwd == rePass:
                return True
            elif (i - 1) != 0:
                print('输入错误，你还有%d次输入的机会！' % (i - 1))

    # 随机生成开户卡号
    def randomId(self):
        while True:
            # 存储卡号
            str = ''

            # 随机生成6位卡号
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch

            # 判断卡号是否重复
            if not self.allUsersInfo.get(str):
                return str

    # 开卡操作
    def createUser(self):
        try:
            name = input('请输入姓名：')  # 用户姓名
            idCard = input('请输入身份证号码：')  # 用户身份证号
            phone = input('请输入电话号码：')  # 用户的电话号码
            preMoney = int(input('请输入预存金额：'))  # 用户的预存金额

            # 预存金额少于0则开户失败
            if preMoney < 0:
                print('预存金额有误，开户失败！')
                return -1

            # 设置密码
            onePwd = input('请输入密码：')  # 第一次密码
            twoPwd = self.checkPwd(onePwd)

            if not twoPwd:
                print('确认密码错误，开户失败！')
                return -1

            # 以上全部完成，则开户所需的信息准备齐全，开户成功
            # 系统生成开户卡号

            # 生成卡号
            cardStr = self.randomId()

            # 创建一个卡的实例，用于存储卡的信息
            card = Card(cardStr, onePwd, preMoney)

            # 创建一个用户实例，用于存储用户的信息
            user = User(name, idCard, phone, card)

            # 按 卡号 ： 用户信息 键值对的形式存入字典中
            self.allUsersInfo[cardStr] = user

            # 提示用户，已经开户成功
            time.sleep(1)
            print('开户成功，请牢记卡号({})...'.format(cardStr))

        except Exception as e:
            print('抱歉，系统出现故障，暂时无法操作！')
            return

    # 判断卡号是否存在
    def isExistence(self, cardStrInp):
        # 卡号不存在，直接退回到选项界面
        if self.allUsersInfo.get(cardStrInp):
            return True

        # 卡号不存在的情况下
        else:
            print('卡号不存在！')
            return False

    # 做查询等操作时，输入密码
    def secretOption(self, cardStrInp):
        myList = [3, 2, 1, 0]
        for i in myList:
            # 如果密码输入错误超过三次
            if i == 0:
                return False
            passInp = input('请输入密码：')
            if passInp == self.allUsersInfo[cardStrInp].cardInfo.cardPwd:
                return True
            elif (i - 1) != 0:
                print('输入错误，你还有%d次输入的机会！' % (i - 1))


    # 查询用户信息
    def searchUserInfo(self):
        cardStrInp = input('请输入卡号：')  # 用户想要查询的卡号

        # 判断卡号的状态
        isExist = self.isExistence(cardStrInp)

        # 卡号存在
        if isExist:
            # 是否被锁定
            if not self.allUsersInfo[cardStrInp].cardInfo.isLock:
                # 输入密码并判断
                # 密码正确则输出余额
                if self.secretOption(cardStrInp):
                    print('账号：%s   余额：%d' % (cardStrInp, self.allUsersInfo[cardStrInp].cardInfo.cardMoney))
                    return 0

                # 密码错误则锁定卡号
                else:
                    print('密码输入错误超过3次，卡号已被锁定，请先解锁！')
                    self.allUsersInfo[cardStrInp].cardInfo.isLock = True
                    return -1
            else:
                print('该卡号已被锁定，请先解锁！')
                return -1


    # 取钱
    def getMoney(self):
        cardStrInp = input('请输入卡号：')

        isExist = self.isExistence(cardStrInp)
        # print(isExist)

        # 如果卡号存在
        if isExist:
            # 如果没被锁定
            if not self.allUsersInfo[cardStrInp].cardInfo.isLock:

                # 如果密码正确
                if self.secretOption(cardStrInp):
                    getMoney = int(input('请输入取款金额：'))

                    # 如果取款金额超出余额
                    if getMoney > self.allUsersInfo[cardStrInp].cardInfo.cardMoney:
                        print('余额不足，取款失败！')
                        return -1

                    # 余额足够的情况，取款成功
                    else:
                        self.allUsersInfo[cardStrInp].cardInfo.cardMoney -= getMoney
                        print('取款成功，卡上余额：%d' % self.allUsersInfo[cardStrInp].cardInfo.cardMoney)
                        return 0
                else:
                    print('密码输入错误超过3次，卡号已被锁定，请先解锁！')
                    self.allUsersInfo[cardStrInp].cardInfo.isLock = True
                    return -1
            else:
                print('该卡号已被锁定，请先解锁！')
                return -1


    # 存钱
    def saveMoney(self):
        cardStrInp = input('请输入卡号：')

        isExist = self.isExistence(cardStrInp)

        if isExist:
            # 如果没被锁定
            if not self.allUsersInfo[cardStrInp].cardInfo.isLock:

                # 如果密码正确
                if self.secretOption(cardStrInp):
                    saveMoney = int(input('请输入存款金额：'))
                    if saveMoney <= 0:
                        print('无效的存款金额！')
                        return -1
                    else:
                        # 存款成功
                        self.allUsersInfo[cardStrInp].cardInfo.cardMoney += saveMoney
                        print('存款成功，卡内余额为%d！' % self.allUsersInfo[cardStrInp].cardInfo.cardMoney)
                else:
                    print('密码输入错误超过3次，卡号已被锁定，请先解锁！')
                    self.allUsersInfo[cardStrInp].cardInfo.isLock = True
                    return -1
            else:
                print('该卡号已被锁定，请先解锁！')
                return -1

    # 转账
    def transMoney(self):
        cardInp = input('请输入卡号：')

        isExist = self.isExistence(cardInp)

        # 卡号存在
        if isExist:
            # 没被锁定
            if not self.allUsersInfo[cardInp].cardInfo.isLock:
                # 密码正确
                if self.secretOption(cardInp):
                    transCardInp = input('请输入要转账的卡号：')
                    isExistTrans = self.isExistence(transCardInp)

                    # 要转账的卡号存在
                    if isExistTrans:
                        # 要转账的卡号没被锁定
                        if not self.allUsersInfo[transCardInp].cardInfo.isLock:
                            # 要转账的卡号不是自己的卡号
                            if transCardInp != cardInp:
                                transMoneyInp = int(input('请输入要转账的金额：'))
                                # 判断转账金额是否大于卡内余额
                                if transMoneyInp > self.allUsersInfo[cardInp].cardInfo.cardMoney:
                                    print('余额不足，转账失败！')
                                    return -1
                                else:
                                    self.allUsersInfo[cardInp].cardInfo.cardMoney -= transMoneyInp
                                    self.allUsersInfo[transCardInp].cardInfo.cardMoney += transMoneyInp
                                    print('转账成功，卡内余额为%d!' % self.allUsersInfo[cardInp].cardInfo.cardMoney)
                            else:
                                print('无法转入自己的账户！')
                                return -1
                        else:
                            print('对方卡号已被锁定，无法转账，请先解锁！')
                            return -1
                else:
                    print('密码输入错误超过3次，卡号已被锁定，请先解锁！')
                    self.allUsersInfo[cardInp].cardInfo.isLock = True
                    return -1
            else:
                print('该卡号已被锁定，请先解锁！')
                return -1


    # 改密
    def changePwd(self):
        cardStrInp = input('请输入卡号：')

        isExist = self.isExistence(cardStrInp)

        if isExist:
            # 如果没被锁定
            if not self.allUsersInfo[cardStrInp].cardInfo.isLock:

                # 如果密码正确
                if self.secretOption(cardStrInp):
                    # 输入修改后的密码
                    changePwd = input('请输入新密码：')

                    # 不允许新密码和旧密码相同
                    if changePwd != self.allUsersInfo[cardStrInp].cardInfo.cardPwd:
                        myList = [3, 2, 1, 0]
                        for i in myList:
                            # 如果密码输入错误超过三次
                            if i == 0:
                                print('确认密码错误次数超过3次，修改密码失败！')
                                return -1
                            passInp = input('请确认新密码：')

                            # 如果新密码确认成功，则修改密码
                            if passInp == changePwd:
                                print('密码修改成功！')
                                self.allUsersInfo[cardStrInp].cardInfo.cardPwd = changePwd
                                return 0
                            elif (i - 1) != 0:
                                print('输入错误，你还有%d次输入的机会！' % (i - 1))
                    # 新密码和旧密码相同，不允许修改，提示并退出
                    else:
                        print('新密码不允许和旧密码相同！')
                        return -1
                # 密码不正确
                else:
                    print('密码输入错误超过3次，卡号已被锁定，请先解锁！')
                    self.allUsersInfo[cardStrInp].cardInfo.isLock = True
                    return -1
            else:
                print('该卡号已被锁定，请先解锁！')
                return -1


    # 解锁
    def unlockUser(self):
        cardStrInp = input('请输入卡号：')

        isExist = self.isExistence(cardStrInp)

        # 存在
        if isExist:
            # 被锁定
            if self.allUsersInfo[cardStrInp].cardInfo.isLock:
                # 如果密码正确
                if self.secretOption(cardStrInp):
                    # 输入身份证号信息做确认
                    idCardInp = input('请输入身份证号：')

                    # 身份证号信息匹配
                    if idCardInp == self.allUsersInfo[cardStrInp].idCard:
                        # 解锁成功
                        print('解锁成功！')
                        self.allUsersInfo[cardStrInp].cardInfo.isLock = False
                        return 0
                    else:
                        print('身份证号信息不匹配，解锁失败！')
                        return -1
                # 密码不正确
                else:
                    print('密码输出错误，解锁失败！')
                    return -1
            else:
                print('该卡号未被锁定，无需解锁！')
                return -1
