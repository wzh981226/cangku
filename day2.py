import random
ran=random.randint(0,2)
a=500#初始资金：500
i=0
while True:
    print("你的余额为：", a)
    num=int(input("请输入一个数字"))
    if num == ran:
        print ("yes")
        a=a+10
        print (a)
        ran = random.randint(0, 2)
    elif i==2:
        break
    else:
        a=a-100
        print ("no")
        i=i+1







