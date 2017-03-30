# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
from models import *
import isodate
from django.http import HttpResponse
from dateutil import parser
from userConstants import *
import datetime
from django.db.models import Max
from django.utils.datastructures import MultiValueDictKeyError
from simplejson import dumps
import logging
logger = logging.getLogger('django')

def getChannelForVideo(lang, category):
    logger.info("Entered getChannelForVideo ")
    channelList = []
    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=category)
    channelObj = Video_Channel.objects.filter(Language=langObj, Category=categoryObj)

    for i in channelObj:
        videoDict = {}
        videoDict['Channel_Id'] = i.Channel_Id
        videoDict['Source'] = i.Source_id
        channelList.append(videoDict)
    logger.info("Exited getChannelForVideo ")
    return channelList

def getVideoData(lang, category, channelList):
    logger.info("Entered getVideoData ")
    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=category)
    youtube = build('youtube', 'v3', developerKey='AIzaSyC7La0xSTaoc1xyPDAEK6D-IkucULPCraA')

    videoList = []
    for channelDict in channelList:
        search_response = youtube.search().list(part="id",
                                                type='video',
                                                order='date',
                                                channelId=channelDict['Channel_Id'],
                                                maxResults=MAX_VIDEO_PER_CHANNEL).execute()
        videoIds = []
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videoIds.append(search_result['id']['videoId'])

        search_response = youtube.videos().list(
                                                id=",".join(videoIds),
                                                part="id,snippet,contentDetails"
                                                ).execute()
        cnt = 0
        for search_result in search_response.get("items", []):
            dur=isodate.parse_duration(search_result["contentDetails"]["duration"])
            videoDict = {}
            videoDict['language'] = langObj
            videoDict['category'] = categoryObj
            videoDict['Video_Id'] = search_result['id']
            videoDict['title'] = search_result["snippet"]["title"]
            videoDict['summary'] = search_result["snippet"]["localized"]['description']
            videoDict['thumbnail'] = search_result['snippet']['thumbnails']['high']['url']
            videoDict['published'] = search_result["snippet"]["publishedAt"]
            videoDict['source'] = channelDict['Source']
            videoDict['duration'] = str(dur)
            videoList.append(videoDict)
            cnt+=1

    logger.info("Exited getVideoData ")
    return videoList

def inserNewsVideo(videoList):
    logger.info("Entered inserNewsVideo ")
    newsVideoObj = News_Video.objects.all()

    for videoDict in videoList:
        found = 0
        for item in newsVideoObj:
            if item.VideoId == videoDict['Video_Id']:
                found = 1
        if found == 0:
            sourceObj = Video_Source.objects.get(id = videoDict['source'])
            dt = parser.parse(videoDict['published'])
            video = News_Video(Language = videoDict['language'],
                               Category = videoDict['category'],
                               VideoId = videoDict['Video_Id'],
                               Title = videoDict['title'],
                               Summary = videoDict['summary'],
                               Thumbnail = videoDict['thumbnail'],
                               Source = sourceObj,
                               Published_Date = dt,
                               Duration = videoDict['duration'])
            video.save()
    logger.info("Exited inserNewsVideo ")

def insertLangCategoryVideoTable(lang, category, videoObj, maxClusterId, isRep):
    logger.info("Entered insertLangCategoryVideoTable ")
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = English_Top_Stories_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = English_Entertainment_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = English_Sports_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = English_World_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = English_Business_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = English_Lifestyle_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()

    if lang.lower() == ENGLISH.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = English_Health_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = English_Fashion_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = English_Technology_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()


    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = English_Environment_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = English_Science_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = English_Food_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Marathi_Top_Stories_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Marathi_Entertainment_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = Marathi_Sports_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Hindi_Top_Stories_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Hindi_Entertainment_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Hindi_Business_Video(Cluster_Id = maxClusterId,
                                                        Video = videoObj,
                                                        VideoId = videoObj.VideoId,
                                                        Title = videoObj.Title,
                                                        Summary = videoObj.Summary,
                                                        Thumbnail = videoObj.Thumbnail,
                                                        Source = videoObj.Source,
                                                        Published_Date = videoObj.Published_Date,
                                                        Duration = videoObj.Duration,
                                                        Is_Rep = isRep)
            langCategoryObj.save()
    logger.info("Exited insertLangCategoryVideoTable ")
    
def deleteLangCategoryVideoTable(lang, category):
    logger.info("Entered deleteLangCategoryVideoTable ")
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = English_Top_Stories_Video.objects.all().delete()

        elif category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = English_Entertainment_Video.objects.all().delete()

        elif category.lower() == SPORTS.lower():
            langCategoryObj = English_Sports_Video.objects.all().delete()

        elif category.lower() == WORLD.lower():
            langCategoryObj = English_World_Video.objects.all().delete()

        elif category.lower() == BUSINESS.lower():
            langCategoryObj = English_Business_Video.objects.all().delete()

        elif category.lower() == LIFESTYLE.lower():
            langCategoryObj = English_Lifestyle_Video.objects.all().delete()

        elif category.lower() == HEALTH.lower():
            langCategoryObj = English_Health_Video.objects.all().delete()

        elif category.lower() == FASHION.lower():
            langCategoryObj = English_Fashion_Video.objects.all().delete()

        elif category.lower() == TECHNOLOGY.lower():
            langCategoryObj = English_Technology_Video.objects.all().delete()

        elif category.lower() == ENVIRONMENT.lower():
            langCategoryObj = English_Environment_Video.objects.all().delete()

        elif category.lower() == SCIENCE.lower():
            langCategoryObj = English_Science_Video.objects.all().delete()

        elif category.lower() == FOOD.lower():
            langCategoryObj = English_Food_Video.objects.all().delete()

    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Marathi_Top_Stories_Video.objects.all().delete()

        elif category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Marathi_Entertainment_Video.objects.all().delete()

    if lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Hindi_Top_Stories_Video.objects.all().delete()

        elif category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Hindi_Entertainment_Video.objects.all().delete()

        elif category.lower() == BUSINESS.lower():
            langCategoryObj = Hindi_Business_Video.objects.all().delete()
    logger.info("Exited deleteLangCategoryVideoTable ")
    
def getMaxClusterIdVideo(lang, category):
    logger.info("Entered getMaxClusterIdVideo ")
    if lang == ENGLISH:
        if category.lower() == TOP_STORIES.lower():
            maxDict = English_Top_Stories_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == ENTERTAINMENT.lower():
            maxDict = English_Entertainment_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == SPORTS.lower():
            maxDict = English_Sports_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == WORLD.lower():
            maxDict = English_World_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == BUSINESS.lower():
            maxDict = English_Business_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == LIFESTYLE.lower():
            maxDict = English_Lifestyle_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == HEALTH.lower():
            maxDict = English_Health_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == FASHION.lower():
            maxDict = English_Fashion_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == TECHNOLOGY.lower():
            maxDict = English_Technology_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == ENVIRONMENT.lower():
            maxDict = English_Environment_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == SCIENCE.lower():
            maxDict = English_Science_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == FOOD.lower():
            maxDict = English_Food_Video.objects.all().aggregate(Max('Cluster_Id'))

    elif lang == MARATHI:

        if category.lower() == TOP_STORIES.lower():
            maxDict = Marathi_Top_Stories_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == ENTERTAINMENT.lower():
            maxDict = Marathi_Entertainment_Video.objects.all().aggregate(Max('Cluster_Id'))
    elif lang == HINDI:

        if category.lower() == TOP_STORIES.lower():
            maxDict = Hindi_Top_Stories_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == ENTERTAINMENT.lower():
            maxDict = Hindi_Entertainment_Video.objects.all().aggregate(Max('Cluster_Id'))

        elif category.lower() == BUSINESS.lower():
            maxDict = Hindi_Business_Video.objects.all().aggregate(Max('Cluster_Id'))

    logger.info("Exited getMaxClusterIdVideo ")
    return maxDict


def getVideoForLanguageCategory(lang,category,deltaHours):
    logger.info("Entered getVideoForLanguageCategory ")

    channelList = getChannelForVideo(lang, category)
    videoList = getVideoData(lang, category, channelList)
    inserNewsVideo(videoList)

    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=category)
    deltaDate = datetime.datetime.now() - datetime.timedelta(hours = deltaHours)


    videoObjAll = News_Video.objects.filter(Language=langObj,
                                             Category=categoryObj,
                                             Published_Date__gt=deltaDate).order_by('Published_Date')
    maxDict = getMaxClusterIdVideo(lang,category)
    if maxDict['Cluster_Id__max'] :
        maxClusterId = maxDict['Cluster_Id__max'] + 1
    else :
        maxClusterId = 1

    deleteLangCategoryVideoTable(lang, category)

    for videoObj in videoObjAll :
        insertLangCategoryVideoTable(lang, category, videoObj, maxClusterId, 1)
        maxClusterId +=1

    logger.info("Exited getVideoForLanguageCategory ")


def getVideoForCategoryScreen(lang, category, limit, maxClusterId):
    if lang.lower()==ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            if maxClusterId:
                categoryDict = English_Top_Stories_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Top_Stories_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == ENTERTAINMENT.lower():
            if maxClusterId:
                categoryDict = English_Entertainment_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Entertainment_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == SPORTS.lower():
            if maxClusterId:
                categoryDict = English_Sports_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Sports_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == WORLD.lower():
            if maxClusterId:
                categoryDict = English_World_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_World_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == BUSINESS.lower():
            if maxClusterId:
                categoryDict = English_Business_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Business_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == LIFESTYLE.lower():
            if maxClusterId:
                categoryDict = English_Lifestyle_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Lifestyle_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == HEALTH.lower():
            if maxClusterId:
                categoryDict = English_Health_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Health_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == FASHION.lower():
            if maxClusterId:
                categoryDict = English_Fashion_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Fashion_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == TECHNOLOGY.lower():
            if maxClusterId:
                categoryDict = English_Technology_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Technology_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == ENVIRONMENT.lower():
            if maxClusterId:
                categoryDict = English_Environment_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Environment_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == SCIENCE.lower():
            if maxClusterId:
                categoryDict = English_Science_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Science_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == FOOD.lower():
            if maxClusterId:
                categoryDict = English_Food_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = English_Food_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    elif lang.lower()==MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            if maxClusterId:
                categoryDict = Marathi_Top_Stories_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = Marathi_Top_Stories_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == ENTERTAINMENT.lower():
            if maxClusterId:
                categoryDict = Marathi_Entertainment_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = Marathi_Entertainment_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    elif lang.lower()==HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            if maxClusterId:
                categoryDict = Hindi_Top_Stories_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = Hindi_Top_Stories_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == ENTERTAINMENT.lower():
            if maxClusterId:
                categoryDict = Hindi_Entertainment_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = Hindi_Entertainment_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
        if category.lower() == BUSINESS.lower():
            if maxClusterId:
                categoryDict = Hindi_Business_Video.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
            else:
                categoryDict = Hindi_Business_Video.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    return parseDateTimeToStringVideo(categoryDict)

def parseDateTimeToStringVideo(dictList):
    thumbStr='Thumbnail'
    isRepStr='Is_Rep'
    titleStr='Title'
    VideoIdStr='VideoId'
    summStr='Summary'
    clusterStr='Cluster_Id'
    sourceStr='Source_id'
    videoStr='Video_id'
    idStr='id'
    pubDateStr='Published_Date'
    durStr = 'Duration'
    currDateStr = 'Current_Date'
    newsDictList=[]
    for rec in dictList:
        sourceObj = Video_Source.objects.get(id=rec.Source_id)
        newsDict={}
        newsDict[thumbStr]=rec.Thumbnail
        if rec.Is_Rep:
            newsDict[isRepStr]=1
        else:
            newsDict[isRepStr]=0
        newsDict[titleStr]=rec.Title
        newsDict[VideoIdStr]=rec.VideoId
        newsDict[summStr]=rec.Summary
        newsDict[clusterStr]=rec.Cluster_Id
        newsDict[sourceStr]=sourceObj.Name
        newsDict[videoStr]=rec.Video_id
        newsDict[idStr]=rec.id
        newsDict[durStr]=rec.Duration
        newsDict[pubDateStr]=rec.Published_Date.strftime('%Y-%m-%d %H:%M')
        newsDictList.append(newsDict)
    return newsDictList