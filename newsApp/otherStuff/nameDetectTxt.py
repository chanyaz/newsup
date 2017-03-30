# -*- coding: utf-8 -*-
import urllib
import csv
import json
from xlrd import open_workbook


f=open('E:/Facebook_Names/apte.txt','r')
for line in f:
    groupName = line.split('%')[0]
    groupId = line.split('%')[1]
    values = []
    query = "select name from user where uid in (SELECT uid FROM group_member WHERE gid =" + groupId + "order by uid desc LIMIT 10000)"
    YOUR_ACCESS_TOKEN = 'CAACEdEose0cBAGV9DbXH3sZCbYPuV2PURgBAXzoASUItuOYSe83UzooHpEPEOUZAT1tM8S1Jxyv9lq9l88Oo2BZBkLkdfMQppdGzGFTgVisMvpga9URFMEZAP9DV1H9sRGAruFZBSUnmhTDMKsGLcPlwd7UvK3PDeG7CukBsZBIBihAPOHwgdzUn5SUhZASaplNI5bL7WsKXwZDZD'
    params = urllib.urlencode({'q': query, 'access_token': YOUR_ACCESS_TOKEN})
    print params
    try :
        url = "https://graph.facebook.com/fql?" + params
        data = urllib.urlopen(url).read()
        print data
        j = json.loads(data)
        cnt = 0
        finalcnt = 0
        list = []
        finalList= []
        print j
        for dict in j['data']:
            try:

                finalName = '@'+dict['name'].encode('utf-8')
                list.insert(cnt,finalName)
                cnt+=1
                if cnt == 50:
                    cnt = 0
                    list = tuple(list)
                    finalList.insert(finalcnt,list)
                    finalcnt +=1
                    list=[]
            except:
                pass
        groupId = groupId.rstrip('\n')
        outputFileName = 'E:/Facebook_Names/verma/New folder/'+ groupName +'_'+ str(groupId) + '.csv'
        finalList = zip(*finalList)
        with open(outputFileName, 'wb') as fp:
            a = csv.writer(fp)
            try:
                a.writerows(finalList)
            except UnicodeEncodeError:
                print 'fuck'
    except :
        print 'fuck you'
f.close()

