from threading import Thread
import time
money = 10000
i=0
class chushi(Thread):
    def run(self) -> None:
        global i
        while True:
            if i<500:
                i = i + 1
                #print("厨师正在烹饪，已经做了", i , "个汉堡！")
            else:
                time.sleep(3)

class xiaofeizhe(Thread):
    username  = ""
    count = 0
    def run(self) -> None:
        money = 10000
        global i
        while True:
            if money > 0 and i>0:
                self.count = self.count + 1
                money = money - 5
                i=i-1
                print(self.username, "抢到1个汉堡，总共抢了", self.count, "个，还剩",money,"元")
            elif i==0:
                 print("汉堡暂已售完，请静心等待")
                 time.sleep(3)
            elif money <= 0:
                 print(self.username, "钱已花完，总共抢了", self.count, "个汉堡！！")
                 break
p = chushi()

p1 = xiaofeizhe()
p1.username="一"

p2 = xiaofeizhe()
p2.username="二"

p3 = xiaofeizhe()
p3.username="三"

p4 = xiaofeizhe()
p4.username="四"

p5 = xiaofeizhe()
p5.username="五"

p6 = xiaofeizhe()
p6.username="六"

p.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()