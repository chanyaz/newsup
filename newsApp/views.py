# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Utils import *
from youtube import *
from userConstants import *
from django.template.context import RequestContext
from simplejson import dumps
from models import *
import logging
from django.utils.datastructures import MultiValueDictKeyError
from loadNews import *
from django.core.exceptions import ObjectDoesNotExist
import urllib # Python URL functions
import csv

from xlrd import open_workbook

logger = logging.getLogger('django')

def insertLanguageCategory(request):
    #insertWithoutClustering(HINDI,FARIDABAD,DELTA_HOURS_TWENTY_FOUR)
    #clusterOnLanguageCategory(ENGLISH,TOP_STORIES,DELTA_HOURS_TWELVE)

    '''clusterOnLanguageCategory(HINDI,TOP_STORIES,DELTA_HOURS_TWELVE)
    clusterOnLanguageCategory(HINDI,WORLD,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,OPINION,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,HEALTH,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,LIFESTYLE,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,ENTERTAINMENT,DELTA_HOURS_TWENTY_FOUR)
    clusterOnLanguageCategory(HINDI,TECHNOLOGY,DELTA_HOURS_TWENTY_FOUR)
    clusterOnLanguageCategory(HINDI,AUTO,DELTA_HOURS_TWENTY_FOUR)
    clusterOnLanguageCategory(HINDI,POLITICS,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,ENVIRONMENT,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,TRAVEL,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,SCIENCE,DELTA_HOURS_TWENTY_FOUR)
    clusterOnLanguageCategory(HINDI,BUSINESS,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,FOOD,DELTA_HOURS_TWENTY_FOUR)
    clusterOnLanguageCategory(HINDI,FASHION,DELTA_HOURS_TWENTY_FOUR)
    insertWithoutClustering(HINDI,CRIME,DELTA_HOURS_TWENTY_FOUR)'''


    createURLFile()


    return HttpResponse("Hello world")

import urllib # Python URL functions
import csv

from xlrd import open_workbook

def createURLFile():
    f = open_workbook('E:/ImportIOurls15Mar.xlsx','r')
    for line in f.sheets():
        for row in range(line.nrows):
            lang = (line.cell(row,0).value)
            cat = (line.cell(row,1).value)
            prevURL = (line.cell(row,2).value)
            source = (line.cell(row,3).value)
            finalURL = (line.cell(row,7).value)
            #print row
            #print '===================================='
            #sourceObj = News_Source.objects.get(Name=source)
            #langObj = Language.objects.get(Name=lang)
            #categoryObj = News_Category.objects.get(Name=cat)
            try:
                feedObj = News_Feed.objects.get(URL = prevURL,
                                                )
                '''for feed in feedObj:
                    feed.URL = finalURL
                    feed.save()'''
                feedObj.URL = finalURL
                feedObj.save()
            except:
                print row



def TopN(request):
    logger.info("Entered TopN ")
    deleteLangCategoryTable(MARATHI, TOPN)
    createTopN(MARATHI)
    deleteLangCategoryTable(ENGLISH, TOPN)
    createTopN(ENGLISH)
    deleteLangCategoryTable(HINDI, TOPN)
    createTopN(HINDI)
    logger.info("Exited TopN ")
    return HttpResponse("Hello world")

def insertVideoLanguageCategory(request):

    getVideoForLanguageCategory(HINDI,TOP_STORIES,DELTA_HOURS_TWELVE)
    getVideoForLanguageCategory(HINDI,ENTERTAINMENT,DELTA_HOURS_TWELVE)
    getVideoForLanguageCategory(HINDI,BUSINESS,DELTA_HOURS_TWELVE)
    '''getVideoForLanguageCategory(ENGLISH,ENTERTAINMENT,DELTA_HOURS_THREE_SIXTY)
    getVideoForLanguageCategory(ENGLISH,SPORTS,DELTA_HOURS_THREE_SIXTY)
    getVideoForLanguageCategory(MARATHI,TOP_STORIES,DELTA_HOURS_TWELVE)
    getVideoForLanguageCategory(MARATHI,ENTERTAINMENT,DELTA_HOURS_THREE_SIXTY)

    getVideoForLanguageCategory(ENGLISH,WORLD,DELTA_HOURS_TWENTY_FOUR)
    getVideoForLanguageCategory(ENGLISH,BUSINESS,DELTA_HOURS_TWENTY_FOUR)
    getVideoForLanguageCategory(ENGLISH,LIFESTYLE,DELTA_HOURS_THREE_SIXTY)
    getVideoForLanguageCategory(ENGLISH,HEALTH,DELTA_HOURS_THREE_SIXTY)
    getVideoForLanguageCategory(ENGLISH,FASHION,DELTA_HOURS_THREE_SIXTY)
    getVideoForLanguageCategory(ENGLISH,TECHNOLOGY,DELTA_HOURS_THREE_SIXTY)
    getVideoForLanguageCategory(ENGLISH,ENVIRONMENT,DELTA_HOURS_THREE_SIXTY)
    getVideoForLanguageCategory(ENGLISH,SCIENCE,DELTA_HOURS_THREE_SIXTY)
    getVideoForLanguageCategory(ENGLISH,FOOD,DELTA_HOURS_THREE_SIXTY)'''

    #getVideoForLanguageCategory(MARATHI,SPORTS)
    return HttpResponse("Hello world insertVideoLanguageCategory is done")

def sourceNews(request):
    if request.method == "GET":
        try:
            lang=request.GET['language']
        except MultiValueDictKeyError:
            lang=ENGLISH
        try:
            category=request.GET['category']
        except MultiValueDictKeyError:
            category=TOP_STORIES
        sourceId=int(request.GET['sourceid'])
        newsDictList=loadNewsForSourceNews(lang, category,sourceId)
        return HttpResponse(dumps(newsDictList,ensure_ascii=True), content_type="application/json")


def socialIndicator(request):
    #socialIndicators(ENGLISH,TOP_STORIES)
    #socialIndicators(HINDI,TOP_STORIES)
    createURLFile1()
    return HttpResponse("Hello world ")


def createURLFile1():
    url1="https://api.import.io/store/connector/"
    url2 = '/_query?input=webpage/url:'
    url3 = '&&_apikey='
    f = open_workbook('E:/NewsApp/AllImportFeeds2.xls','r')
    for line in f.sheets():
        for row in range(line.nrows):
            lang = (line.cell(row,0).value)
            cat = (line.cell(row,1).value)
            urlprev = (line.cell(row,2).value)
            source = (line.cell(row,3).value)
            connector = (line.cell(row,4).value)
            apikey = (line.cell(row,5).value)
            webpageURL = (line.cell(row,7).value)
            #webpage = urlprev.split('webpage/url:')[1].split('&&_apikey')[0]
            webpage = urllib.quote_plus(webpageURL)
            #webpage = urllib.quote_plus(urlprev)
            print 'lang: ',lang
            print 'cat: ',cat
            print 'urlprev: ',urlprev
            print 'source: ',source
            print 'connector: ' ,connector
            print 'apikey : ',apikey
            print 'webpage: ',webpage
            finalURL = url1+connector+url2+webpage+url3+apikey
            print 'finalURL: ',finalURL
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=cat)
            sourceObj = News_Source.objects.get(Name=source)
            feedObj = News_Feed.objects.get(Language = langObj,
                                            Category = categoryObj,
                                            Source = sourceObj,
                                            URL = urlprev)
            #feedObj.URL = finalURL
            feedObj.URL = webpageURL
            feedObj.Type = 'RSS 2.0'
            feedObj.save()
            '''feedObj = News_Feed(Language = langObj,
                                Category = categoryObj,
                                Source = sourceObj,
                                URL = finalURL)
            feedObj.save()'''


#These methods are API METHODS. The app user will directly call them ---------------------------

def loadNewsForHome(request):
  if request.method == "GET":
       lang=request.GET['language']
       categoryString=request.GET['category']
       categoryList=categoryString.split(",")
       newsDictList=loadNewsForHomeScreen(lang,categoryList)
       userDict={'newsDictList':newsDictList}
       return HttpResponse(dumps(userDict,ensure_ascii=True), content_type="application/json")

def loadNewsForCategory1(request):

   lang="English"
   category="Economy"
   maxClusterId=0
   similarNewsDict={}
   newsDictList=loadNewsForCategoryScreen(lang, category, maxClusterId)
   # also get similar news articles
   for articles in newsDictList:

        clusterId=articles['Cluster_Id']
        similarNewsDict[clusterId]=getSimilarNewsArticles(lang, category, clusterId)

   userDict={'newsDictList':newsDictList,
             'similarNewsDict':similarNewsDict}
   return render_to_response('category.html', userDict,context_instance=RequestContext(request))

def loadSimilarNews(request):
    if request.method == "GET":
       lang=request.GET['language']
       category=request.GET['category']
       clusterId=request.GET['clusterid']
       userDict=getSimilarNewsArticles(lang, category, clusterId)
       return HttpResponse(dumps(userDict,ensure_ascii=True), content_type="application/json")

def loadNewsForCategory(request):
    if request.method == "GET":
        try:
            lang=request.GET['language']
        except MultiValueDictKeyError:
            lang=ENGLISH
        try:
            category=request.GET['category']
        except MultiValueDictKeyError:
            category=TOP_STORIES
        try:
            maxClusterId=int(request.GET['maxclusterid'])
        except MultiValueDictKeyError:
            maxClusterId=0
        similarNewsDict={}
        newsDictList=loadNewsForCategoryScreen(lang, category, maxClusterId)
        #return render_to_response('category.html', newsDictList,context_instance=RequestContext(request))
        return HttpResponse(dumps(newsDictList,ensure_ascii=True), content_type="application/json")

def loadTopN(request):
    #logger.info("Entered loadTopN ")
    if request.method == "GET":
        try:
            lang=request.GET['language']
        except MultiValueDictKeyError:
            lang=ENGLISH
        userDict = getSimilarTopN(lang)
        return HttpResponse(dumps(userDict,ensure_ascii=True), content_type="application/json")

def loadTopNVideo(request):
    #logger.info("Entered loadTopN ")
    if request.method == "GET":
        try:
            lang=request.GET['language']
        except MultiValueDictKeyError:
            lang=ENGLISH
        userDict = getSimilarTopNVideo(lang)
        #logger.info("Exited loadTopN ")
        return HttpResponse(dumps(userDict,ensure_ascii=True), content_type="application/json")

def loadVideoForCategory(request):
    if request.method == "GET":
        try:
            lang=request.GET['language']
        except MultiValueDictKeyError:
            lang=ENGLISH
        try:
            category=request.GET['category']
        except MultiValueDictKeyError:
            category=TOP_STORIES
        try:
            maxClusterId=int(request.GET['maxclusterid'])
        except MultiValueDictKeyError:
            maxClusterId=0
        if not maxClusterId:
        # this means that the request is for the first time
            maxClusterId=0
        limit=CATEGORY_VIDEO_LIMIT
        newsDictList=getVideoForCategoryScreen(lang, category, limit, maxClusterId)
        return HttpResponse(dumps(newsDictList,ensure_ascii=True), content_type="application/json")

def isVideoAvailable(request):
    if request.method == "GET":
        lang=request.GET['language']
        category=request.GET['category']
    found = 0
    for dict in videoLangCatList:
        if found == 0:
            if dict['lang'].lower() == lang.lower():
                if dict['category'].lower() == category.lower():
                    found = 1
    isVideoPresent ={}
    isVideoPresent['isPresent'] = found
    return HttpResponse(dumps(isVideoPresent,ensure_ascii=True), content_type="application/json")

def loadNewsForCategoryNew(request):
    if request.method == "GET":
        try:
            lang=request.GET['language']
        except MultiValueDictKeyError:
            lang=ENGLISH
        try:
            category=request.GET['category']
        except MultiValueDictKeyError:
            category=TOP_STORIES
        try:
            maxClusterId=int(request.GET['maxclusterid'])
        except MultiValueDictKeyError:
            maxClusterId=0
        similarNewsDict={}
        newsDictList=loadNewsForCategoryScreenNew(lang, category, maxClusterId)
        #return render_to_response('category.html', newsDictList,context_instance=RequestContext(request))
        return HttpResponse(dumps(newsDictList,ensure_ascii=True), content_type="application/json")

def loadSimilarNewsNew(request):
    if request.method == "GET":
       lang=request.GET['language']
       category=request.GET['category']
       clusterId=request.GET['clusterid']
       userDict=getSimilarNewsArticlesNew(lang, category, clusterId)
       return HttpResponse(dumps(userDict,ensure_ascii=True), content_type="application/json")