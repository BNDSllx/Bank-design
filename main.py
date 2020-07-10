# 主函数
from view import View
import pickle
from atm import ATM
import time

def main():
    # 定义管理员对象
    admin = View()

    # 管理员登录界面
    admin.printAdminView()

    # 如果管理员账号、密码输入错误则退出
    if admin.adminOption():
       return -1

    # 读取存储在文件中的所有用户的信息
    file = open('database.txt', 'rb')
    allUsersInfo = pickle.load(file)  # 将所有用户信息存储到 allUsersInfo中去
    file.close()  # 关闭文件

    # 打印所有用户信息，以便验证
    print('*' * 10)
    print('usersInfo:', allUsersInfo)

    # 创建atm实例，并将所有用户信息传递过去，进行初始化
    atm = ATM(allUsersInfo)

    # 循环进行操作选项
    while True:
        # 调用功能显示方法，显示功能选项
        admin.printSysFunctionView()

        # 提示用户输入功能选项进行操作
        option= input('请输入操作选项（数字）:')

        # 对用户的操作选项进行判断
        if option == "1":  # 开户操作
            atm.createUser()

        elif option == "2":  # 查询余额操作
            atm.searchUserInfo()

        elif option == "3":  # 取钱操作
            atm.getMoney()

        elif option == "4":  # 存钱操作
            atm.saveMoney()

        elif option == "5":  # 转账操作
            atm.transMoney()

        elif option == "6":  # 改密码操作
            atm.changePwd()

        elif option == "7":  # 解锁操作
            atm.unlockUser()

        # 以下操作暂时未写
        # elif option == "q":  # 退出操作
        #     # atm.quitSys()
        #     print('退出')

        # elif option == "9":  # 补卡操作
        #     print("补卡")
        #
        # elif option == "0":  # 销户操作
        #     print("销户")

        elif option == "8":  # 退出系统
            return 0

        # 如果用户输入的不是上述操作
        else:
            print('无效的操作选项！')
            return -1

        # 将新信息写入文件
        # 将当前系统中的用户信息保存到文件中
        f = open('database.txt', "wb")
        pickle.dump(allUsersInfo, f)
        f.close()






if __name__ == '__main__':
    main()