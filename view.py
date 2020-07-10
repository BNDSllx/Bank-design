# 视图类
import time


class View(object):
    admin = '1'
    pwd = '1'

    # 管理员登录界面
    def printAdminView(self):
        print("*****************************************************************")
        print("*                                                               *")
        print("*                                                               *")
        print("*                       欢迎登陆李律学的银行                        *")
        print("*                                                               *")
        print("*                                                               *")
        print("*****************************************************************")

    # 用户操作主界面
    def printSysFunctionView(self):
        print("*****************************************************************")
        print("*        开户(1)                            查询(2)             *")
        print("*        取款(3)                            存款(4)             *")
        print("*        转账(5)                            改密(6)             *")
        print("*        解锁(7)                            退出(8)             *")
        # print("*        补卡(9)                            销户(0)             *")
        # print("*                         退出(t)                               *")
        print("*****************************************************************")

    # 管理员登录选项
    def adminOption(self):
        inputAdmin = input('请输入管理员账号：')

        if inputAdmin != self.admin:
            print('账号错误！')
            return -1

        inputPwd = input('请输入管理员密码：')

        if inputPwd != self.pwd:
            print('密码错误！')
            return -1

        # 管理员账号和密码全部正确
        print('操作成功，请稍后...')
        time.sleep(2)
        return 0

# view = View()
# view.printAdminView()
# view.adminOption()
# view.printSysFunctionView()