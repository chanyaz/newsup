# -*- coding: utf-8 -*-
import urllib
import csv
import json
from xlrd import open_workbook

f = open_workbook('E:/Facebook_Names/FbNewGroups.xls','r')
for line in f.sheets():
    values = []
    for row in range(line.nrows):
        try:
            col_value = []
            value  = (line.cell(row,1).value)
            valueRow  = (line.cell(row,0).value)
            fid = str(int(value))
            print fid
            query = "select name from user where uid in (SELECT uid FROM group_member WHERE gid =" + fid + "order by uid desc LIMIT 10000)"
            YOUR_ACCESS_TOKEN = 'CAACEdEose0cBAKuQlwWmrC1svUGOKmTO8r6GDGA4W14KfGjfQg8yJenCE3PVEeLZAcpgEtEOZCoWNXZBDnV3fIHhqJCHwBeBA9CIc9oOZAd7FIzFhYK6m14a6WDYYrvaB4fBSZB1rAYZAHgyOLFOTLdvvsuWps0eXCf9beKXZCzScQNqGWSC5ITCfaREQQIqL7lrGZAG2DnHgAZDZD'
            params = urllib.urlencode({'q': query, 'access_token': YOUR_ACCESS_TOKEN})
            print params
            url = "https://graph.facebook.com/fql?" + params
            data = urllib.urlopen(url).read()
            j = json.loads(data)
            cnt = 0
            finalcnt = 0
            list = []
            finalList= []
            for dict in j['data']:
                try:
                    finalName = '@'+dict['name'].encode('utf-8')
                    print finalName
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
            fid = fid.rstrip('\n')
            outputFileName = 'E:/Facebook_Names/FbNewGroups/'+ valueRow +'_'+ str(int(value)) + '.csv'
            finalList = zip(*finalList)
            with open(outputFileName, 'wb') as fp:
                a = csv.writer(fp)
                try:
                    a.writerows(finalList)
                except UnicodeEncodeError:
                    print 'fuck'
        except:
            print 'fuck you'