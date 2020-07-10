import pickle

f = open('database.txt', 'wb')
pickle.dump({}, f)
f.close()

file = open('database.txt', 'rb')
allUsersInfo = pickle.load(file)  # 将所有用户信息存储到 allUsersInfo中去
file.close()  # 关闭文件

if allUsersInfo.get('123'):
    print(1)

# 卡号不存在的情况下
else:
    print('卡号不存在！')