# -*- coding: utf-8 -*-

import urllib # Python URL functions
import csv

from xlrd import open_workbook


def createURLFile():

    url1="https://api.import.io/store/connector/"
    url2 = '/_query?input=webpage/url:'
    url3 = '&&_apikey='
    finalList=[]
    f = open_workbook('E:/NewsApp/AllImportFeeds2.xls','r')
    for line in f.sheets():
        for row in range(line.nrows):
            list=[]
            lang = (line.cell(row,0).value)
            cat = (line.cell(row,1).value)
            urlPrev = (line.cell(row,2).value)
            source = (line.cell(row,3).value)
            connector = (line.cell(row,4).value)
            apikey = (line.cell(row,5).value)
            name = (line.cell(row,6).value)
            webpage = urlPrev.split('webpage/url:')[1].split('&&_apikey')[0]
            print webpage
            webpageSafe = urllib.quote_plus(webpage)
            finalURL = url1+connector+url2+webpage+url3+apikey
            list.append(lang)
            list.append(cat)
            list.append(urlPrev)
            list.append(source)
            list.append(connector)
            list.append(apikey)
            list.append(name)
            list.append(finalURL)
            list = tuple(list)
            finalList.append((list))
    outputFileName = 'E:/NewsApp/ImportIOurls15Mar.csv'
    with open(outputFileName, 'wb') as fp:
        a = csv.writer(fp)
        a.writerows(finalList)
def createURLPrint(urldict):

    url1="https://api.import.io/store/connector/"
    url2 = '/_query?input=webpage/url:'
    apiKey = '&&_apikey=bc89297672ad4c7a935fa54367c30a660206333997c9fa80e2a37b5c149a95b45ba5bec6a9ea47ecafeb019fb2644b8c22eb18a8c9b2b391512f2f3b416879b9995d8b93d0e1a5a8de9f9a3c032e6b0c'

    for key in urldict:
        webpageSafe = urllib.quote_plus(urldict[key])
        finalURL = url1+key+url2+webpageSafe+apiKey
        print finalURL

urldict = {'6e338c32-d286-41b7-825c-3e8c4929bcfc':'http://delhincr.amarujala.com/channels/faridabad-news-ncr',
           '29dbde0a-bd60-4f48-a181-a91538929aa4':'http://www.jagran.com/local/haryana_faridabad-news-hindi.html',
           '98360cfc-dac9-403e-9832-cc9e4883b032':'http://www.haribhoomi.com/news/delhi/faridabad/',
           }

createURLFile()



