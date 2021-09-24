import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank_name = "汉科软地球中国区老牛湾分行"
bank = {}
def bank_useradd(username, password, country, province, street, door, account):
    for i in bank:
        if account in bank[i]:
            return 2
    else:
        bank[username] = {
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "account": account,
            "bank_name": bank_name,
            "money": 0
        }
        if len(bank) == 100:
            return 3
        return 1
def useradd():
    username = input("请输入您的用户名")
    password = int(input("请输入您的密码"))
    print("下面请您输入您的地址")
    country = input("\t\t请输入您所在的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account = random.randint(10000000, 99999999)
    status = bank_useradd(username, password, country, province, street, door, account)
    if status == 1:
        print("恭喜你成功开户，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s

            '''
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    elif status == 2:
        print("该用户名已存在")
    elif status == 3:
        print("恭喜你成功开户，以下是您的信息")
        info = '''
                            ------------个人信息------------
                            用户名:%s
                            账号：%s
                            密码：*****
                            国籍：%s
                            省份：%s
                            街道：%s
                            门牌号：%s
                            余额：%s
                            开户行名称：%s

                    '''
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
        print("注册用户组已满")


def cq():
    account = int(input("请输入你的账号"))
    for i in bank:
        if bank[i]["account"] == account:
            m = int(input("请输入你的存款金额"))
            bank[i]["money"] = bank[i]["money"] + m
            print("存款成功")
            info = '''
                                        ------------个人信息------------
                                        账号：%s
                                        余额：%s
                                        开户行名称：%s

                                '''
            print(info % (account, bank[i]["money"], bank_name))
            break
    else:
        print("输入账户不正确")


def qq():
    account = int(input("请输入你的账号"))
    password = int(input("请输入你的密码"))
    for i in bank:
        if bank[i]["account"] == account:
            if bank[i]["password"] == password:
                qq = int(input("请输入你的取款金额"))
                if bank[i]["money"] - qq >= 0:
                    bank[i]["money"] = bank[i]["money"] - qq
                    print("取款成功")
                    info = '''
                     ------------个人信息------------
                      账号：%s
                      余额：%s
                      开户行名称：%s

                      '''
                    print(info % (account, bank[i]["money"], bank_name))
                    return
                else:
                    print("钱不够")
                    break

            else:
                print("密码不正确")
                break
    else:
        print("账号不存在")


def zz():
    account1 = int(input("请输入你要转出的账号"))
    zczh = int(input("请输入你要转入的账号"))
    for i in bank:
        if bank[i]["account"] == zczh:
            for j in bank:
                if bank[j]["account"] == account1:
                    password = int(input("请输转出账户密码"))
                    if bank[j]["password"] == password:
                        cp = int(input("请输入转出金额"))
                        if bank[j]["money"] - cp >= 0:
                            bank[j]["money"] = bank[j]["money"] - cp
                            bank[i]["money"] = bank[i]["money"] + cp
                            print("转出成功")
                            info = '''
                                                        ------------个人信息------------
                                                                账号：%s
                                                                余额：%s
                                                                开户行名称：%s

                                                                    '''
                            print(info % (account1, bank[j]["money"], bank_name))
                            return 0
                        else:
                            print("余额不足")
                            return 0
                    else:
                        print("密码不正确")
                        return 0
    else:
        print("账号不存在")

def cx():
    account = int(input("请输入你要查询的账号"))
    for i in bank:
        if bank[i]["account"] == account:
            password = int(input("请输入你要查询账户的密码"))
            if bank[i]["password"] == password:
                country = bank[i]["country"]
                province = bank[i]["province"]
                street = bank[i]["street"]
                door = bank[i]["door"]
                info = '''
                                            ------------个人信息------------

                                            账号：%s
                                            密码：*****
                                            国籍：%s
                                            省份：%s
                                            街道：%s
                                            门牌号：%s
                                            余额：%s
                                            开户行名称：%s

                                    '''
                print(info % (account, country, province, street, door, bank[i]["money"], bank_name))
                return 0
            else:
                print("密码不正确")
                return 0
    else:
        print("账号不存在")
def tc():
    print("拜拜了你嘞")
while True:
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        cq()
    elif begin == "3":
        qq()
    elif begin == "4":
        zz()
    elif begin == "5":
        cx()
    elif begin == "6":
        tc()
        break
    else:
        print("你瞎输入什么东西")
        break