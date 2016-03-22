# -*- coding: utf-8 -*-  
import pickle
import datetime
import os

class sport:
    def __init__(self, sportName, sportTarget_count,sportTarget_count_mu, sportTarget_time, sportTarget_endline_mu):
        self.name = str(sportName)
        self.sportTarget_count = float(sportTarget_count)
        self.sportTarget_count_mu =sportTarget_count_mu
        self.sportTarget_endline_mu = sportTarget_endline_mu
        #self.sportTarget_endline_mu = 'days'
        self.sportTarget_time = datetime.timedelta(days=sportTarget_time)
        self.sportTarget_startline = datetime.datetime.now()
        self.sportTarget_endline = self.sportTarget_time + datetime.datetime.now()
        self.sport_count = 0
    def addCount(self,newCount):
        self.sport_count += float(newCount)
    def haveAlook(self):
        self.sportCompleted = self.sport_count/self.sportTarget_count
        self.sportCompletedinTime = (int((datetime.datetime.now()-self.sportTarget_startline).total_seconds()/86400))/float(int(self.sportTarget_time.total_seconds()/86400))
        #self.sportCompletedinTime = (int((datetime.timedelta(days=2).total_seconds()/86400)))/float(int(self.sportTarget_time.total_seconds()/86400))
        if self.sportCompleted < 1:
            if self.sportCompleted < self.sportCompletedinTime and self.sportCompletedinTime < 1:
            	result = str((self.sportCompletedinTime-self.sportCompleted) * 10)+self.sportTarget_count_mu
                print "今天还有",result,"没有完成"
                print "是时候动起来了，不要怂！"
            elif self.sportCompleted < self.sportCompletedinTime and self.sportCompletedinTime >= 1:
                print "时间到。你没有完成计划。"
                result = False
            elif self.sportCompleted >= self.sportCompletedinTime and self.sportCompletedinTime < 1:
                print "今日目标已完成。",self.sportCompleted,self.sportCompletedinTime
                result = True
        else:
            print "本计划已完成。瘦子小姐！"
            result = True
        return result

def exitApp():
    pickle.dump(sportlist,open("sportObj.pk", "w"))
    exit()
def addSport():
    print "开始添加运动计划"
    name = raw_input("计划命名(例如跑步，游泳，登山等):")
    count = float(raw_input("计划运动量(不带单位):"))
    count_mu = raw_input("运动单位(上边运动量的单位):")
    time = float(raw_input("计划持续时间(不带单位):"))
    time_mu = raw_input("时间单位(例如天，周，月):")
    if time_mu == "周":
        time *= 7
    elif time_mu == "月":
        time *= 30
    sportlist.append(sport(name,count,count_mu,time,"days"))
    pickle.dump(sportlist,open("sportObj.pk", "w"))
def editSport():
	print "修改运动计划"
	sportID = int(raw_input("运动计划编号:"))
	name = raw_input("计划命名(例如跑步，游泳，登山等):")
	count = float(raw_input("计划运动量(不带单位):"))
	count_mu = raw_input("运动单位(上边运动量的单位):")
	time = float(raw_input("计划持续时间(不带单位):"))
	time_mu = raw_input("时间单位(例如天，周，月):")
	sportlist[sportID].name = name
	sportlist[sportID].sportTarget_count = count
	sportlist[sportID].sportTarget_count_mu = count_mu
	if time_mu == "周":
		time *= 7
	elif time_mu == "月":
		time *= 30
	sportlist[sportID].sportTarget_time = time
	sportlist[sportID].sportTarget_endling_mu = time_mu
	pickle.dump(sportlist,open("sportObj.pk", "w"))
def addCount(num):
	num = int(num)
	newCount = float(raw_input("运动量增加数(单位为"+sportlist[int(num)].sportTarget_count_mu+"):"))
	sportlist[int(num)].addCount(newCount)
	pickle.dump(sportlist,open("sportObj.pk", "w"))
def sportReview():
        print "="*20
        for num,sportItem in enumerate(sportlist):
            print "\n运动计划（"+str(num)+"）",sportItem.name
            #print "目标运动量:", str(sportItem.sportTarget_count)+sportItem.sportTarget_count_mu,'\n',"截止日期:",sportItem.sportTarget_endline
            print "目标运动量:", str(sportItem.sportTarget_count)+sportItem.sportTarget_count_mu
            sportItem.haveAlook()
            print '\n'+'-'*10
        print "="*20

if __name__ == '__main__':
    if os.path.isfile('sportObj.pk'):
        sportlist = pickle.load(open("sportObj.pk","r"))
        print "载入计划"
    else:
        sportlist = []
        addSport()
    sportReview()
    while True:
        print """
        输入"1000"，退出程序。数据自动保存。
        输入"1001"，修改运动计划。
        输入"1011"，添加新的运动计划。
        输入"1111"，查看当前所有计划及进度。
        输入运动计划编号，添加该计划纪录。"""
        command = raw_input("编号:")
        if command == "1000":
            exitApp()
        elif command == "1011":
            addSport()
        elif command == "1111":
            sportReview()
        elif command == "1001":
        	editSport()
        else:
            addCount(int(command))
        print "="*40