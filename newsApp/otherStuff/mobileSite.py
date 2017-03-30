# -*- coding: utf-8 -*-
from userConstants import *
def convertMobileSite(URL):
    if URL[7:14]=='online3':
        mobileURL = 'http://m.' + URL[15:]
        mobileURL = unicode(mobileURL,"utf-8")
    elif URL[7:10]=='www':
        mobileURL = 'http://m.' + URL[11:]
    elif Source_id == 30:
        mobileURL = 'm.maharashtratimes.com' + URL[38:]
    else:
        mobileURL = 'http://m.' + URL[7:]

    return mobileURL

def checkForMobileURL(URL,Source_id):
    for mobileURLId in sourceIdForMobileURL:
        if mobileURLId == Source_id:
            URL = convertMobileSite(URL)
            return URL
    for noTranscodeId in noTranscode:
        if noTranscodeId == Source_id:
            return URL
    URL = 'googleweblight.com/?lite_url=' + URL
    if Source_id == 39:
        URL = unicode(URL,"utf-8")

    return URL

#URL = 'http://maharashtratimes.indiatimes.com/nation/when-i-will-meet-pm-i-will-only-tell-him-one-thing-that-we-dont-need-money-or-land-just-stop-hampering-our-work/articleshow/50286102.cms'
URL = 'http://online3.esakal.com/NewsDetails.aspx?NewsId=4729320117822425501&SectionId=28&SectionName=ताज्या बातम्या&NewsDate=20151221&Provider=- सकाळ वृत्तसेवा&NewsTitle=उद्योगांना कर्जमाफी,शेतकऱ्यांना का नाही?- उद्धव'
Source_id = 108
URL = checkForMobileURL(URL,Source_id)
print URL