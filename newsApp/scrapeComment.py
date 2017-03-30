import urllib2
from bs4 import BeautifulSoup
import re
import requests


def scrapeComments(url,sourceId):
    html = urllib2.urlopen(url, None, 10)
    soup = BeautifulSoup(html)
    str1 = 'http://vuukle.com/api.asmx/getCommentCountListByHost?id='
    str2 = '&host='
    str3 = '&list='


    if sourceId == 1:

        i = soup.find_all("a", {"class":"comment"})
        for item in i:
            finalStr = str(item)
            urlid = int(finalStr[32:39])
            finalDict = {
                        'website': 'indianexpress.com',
                        'api' : '2e5a47ef-15f6-4eec-a685-65a6d0ed00d0',
                        'id': urlid,
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'

    elif sourceId == 27:
        website = 'loksatta.com'
        x= soup(text=re.compile('create_vuukle_platform'))

        for item in x:
            y = item.lstrip()
            z = y.split("'")

            finalDict = {
                        'website': website,
                        'api' : str(z[1]),
                        'id': int(z[3]),
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'
    elif sourceId == 107:
        website = 'bhaskar.com'
        x= soup(text=re.compile('create_vuukle_platform'))
        for item in x:
            y = item.lstrip()
            z = y.split("'")

            finalDict = {
                        'website': website,
                        'api' : str(z[3]),
                        'id': int(z[5]),
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'
    elif sourceId == 35:
        website = 'indiatvnews.com'
        x= soup(text=re.compile('UNIQUE_ARTICLE_ID '))
        for item in x:
            y = item.lstrip()
            z = y.split('"')

            finalDict = {
                        'website': website,
                        'api' : str(z[9]),
                        'id': str(z[1]),
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'
    elif sourceId == 131:
        website = 'amarujala.com'
        x= soup(text=re.compile('create_vuukle_platform'))

        for item in x:
            y = item.lstrip()
            z = y.split('"')

            finalDict = {
                        'website': website,
                        'api' : str(z[1]),
                        'id': str(z[3]),
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'

    elif sourceId == 135:
        website = 'livehindustan.com'
        x= soup(text=re.compile('create_vuukle_platform'))

        for item in x:
            y = item.lstrip()
            z = y.split("'")

            finalDict = {
                        'website': website,
                        'api' : str(z[1]),
                        'id': str(z[3]),
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'
    elif sourceId == 134:
        website = 'aajtak.intoday.in'
        x= soup(text=re.compile('UNIQUE_ARTICLE_ID'))

        for item in x:
            y = item.lstrip()
            z = y.split('"')

            finalDict = {
                        'website': website,
                        'api' : 'dc34b5cc-453d-468a-96ae-075a66cd9eb7',
                        'id': str(z[1]),
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'
    elif sourceId == 150:
        website = 'abpnews.abplive.in'
        x= soup(text=re.compile('create_vuukle_platform'))

        for item in x:
            y = item.lstrip()
            z = y.split('"')

            finalDict = {
                        'website': website,
                        'api' : '454859d8-ee0d-4f40-a92e-808c968122ea',
                        'id': str(z[1]),
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'
    elif sourceId == 32:
        website = 'abpmajha.abplive.in'
        x= soup(text=re.compile('create_vuukle_platform'))

        for item in x:
            y = item.lstrip()
            z = y.split('"')

            finalDict = {
                        'website': website,
                        'api' : '454859d8-ee0d-4f40-a92e-808c968122ea',
                        'id': str(z[1]),
                        }
            urlString =  str1 + finalDict['api'] + str2 + finalDict['website'] + str3 + finalDict['id']
            return urlString,'yuucle'
    elif sourceId == 3:
        string1 = 'http://disqus.com/embed/comments/?base=default&version=7ff52449a33b7f7845efccc7ceb593f0'
        string2 =  '&f=firstpost'
        string3 =  '&t_i='
        #x= soup(text=re.compile('data-disqus-identifier'))
        x = soup.findAll("a", {"class":"cmntsNum"})
        for item in x:
            string4 = string1 + string2 + string3 +  item['data-disqus-identifier'] + '&t_u=' + url
            return string4,'discus'
    elif sourceId == 40:
        string1 = 'http://disqus.com/embed/comments/?base=default&version=7ff52449a33b7f7845efccc7ceb593f0'
        string2 =  '&f=zeenews'
        string3 =  '&t_i='
        #x= soup(text=re.compile('data-disqus-identifier'))
        #print soup
        x = soup.findAll("a", {"class":"disqus-comment-count"})
        for item in x:
            string4 = string1 + string2 + string3 +  item['data-disqus-identifier'] + '&t_u=' + url
            return string4,'discus'
    elif sourceId == 114:
        string1 = 'http://www.hindustantimes.com/fragment/PortalConfig/www.hindustantimes.com/jpt/custom/disqusapi.jpt?thread='
        string4 = string1 +  url
        return string4,'yuucle'
    elif sourceId == 2:
        x = soup.findAll("iframe", {"id":"article-comment-frame"})
        for item in x:
            y = item['data-original']
        string1 = 'http://www.business-standard.com'
        finalUrl = string1 + y
        print finalUrl
        return finalUrl,'iframe'

def scrape4comments(url,sourceid):
    try:
        urlString,identifier = scrapeComments(url,sourceid)

        if identifier =='yuucle':
            r= requests.get(urlString)
            wjson = r.json()
            return wjson
        elif identifier =='discus':
            html = urllib2.urlopen(urlString, None, 10)
            soup = BeautifulSoup(html)
            x= soup(text=re.compile('"total"'))
            z = x[0].split('"total"')[1].split(":")[1].split(",")[0]
            return z
        elif identifier == 'iframe':
            html = urllib2.urlopen(urlString, None, 10)
            soup = BeautifulSoup(html)
            x = soup.findAll("span", {"class":"comment-num"})
            for item in x :
                return item.h2.string



    except:
        return 0

