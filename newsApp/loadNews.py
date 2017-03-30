from models import *
from userConstants import *
import datetime

#These methods are API METHODS. The app user will directly call them ---------------------------



def loadNewsForHomeScreen(lang,categoryList):
# Calling Screen: HOME
#I/P: 1. langList - List of users language prefferences
# 2. categoryList- List of users category prefferences
#O/P: Top news from all those categories as provided in the list by language
    masterCategoryDict={}
    languageDict={}
    limit=HOME_ARTICLE_LIMIT
    maxClusterId=0
    if lang.lower()==ENGLISH.lower():
            languageDictList=[]
            for category in categoryList:

                masterCategoryDict[category]=getEnglishNewsFromCategory(category,limit,maxClusterId)
            languageDictList.append(masterCategoryDict)
            languageDict[lang]=languageDictList

    elif lang.lower()==MARATHI.lower():
            languageDictList=[]
            for category in categoryList:
                masterCategoryDict[category]=getMarathiNewsFromCategory(category,limit,maxClusterId)
            languageDictList.append(masterCategoryDict)
            languageDict[lang]=languageDictList
    return languageDict


def loadNewsForCategoryScreen(lang,category,maxClusterId):
# Calling Screen: CATEGORY
#I/P: 1. lang - users language
# 2. category -  users category
# 3. maxClusterId -  Highest value of the cluster Id
#O/P: Top news from that category
    limit=CATEGORY_ARTICLE_LIMIT

    if not maxClusterId:
        # this means that the request is for the first time
        maxClusterId=0

    if lang.lower()==ENGLISH.lower():
        categoryDict=getEnglishNewsFromCategory(category,limit,maxClusterId)

    elif lang.lower()==MARATHI.lower():
        categoryDict=getMarathiNewsFromCategory(category, limit, maxClusterId)

    return categoryDict

def loadNewsForCategoryScreenNew(lang,category,maxClusterId):
    limit=CATEGORY_ARTICLE_LIMIT

    if not maxClusterId:
        # this means that the request is for the first time
        maxClusterId=0

    if lang.lower()==ENGLISH.lower():
        categoryDict=getEnglishNewsFromCategoryNew(category,limit,maxClusterId)

    elif lang.lower()==MARATHI.lower():
        categoryDict=getMarathiNewsFromCategoryNew(category, limit, maxClusterId)
    elif lang.lower()==HINDI.lower():
        categoryDict=getHindiNewsFromCategoryNew(category, limit, maxClusterId)

    return categoryDict

def loadNewsForSourceNews(lang,category,sourceId):
    limit=CATEGORY_SOURCE_LIMIT

    if lang.lower()==ENGLISH.lower():
        categoryDict=getEnglishNewsForSource(category,limit,sourceId)

    elif lang.lower()==MARATHI.lower():
        categoryDict=getMarathiNewsForSource(category, limit,sourceId)
    elif lang.lower()==HINDI.lower():
        categoryDict=getHindiNewsForSource(category, limit,sourceId)

    return categoryDict

# This method will be called from the HOME SCREEN. It will load news by category.
def getEnglishNewsFromCategory(category,limit,maxClusterId):

    if category.lower() == ECONOMY.lower():
        categoryDict = English_Economy.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == SPORTS.lower():
        categoryDict = English_Sports.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = English_Top_Stories.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = English_World.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == OPINION.lower():
        if maxClusterId:
         categoryDict = English_Opinion.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = English_Opinion.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == HEALTH.lower():
        categoryDict = English_Health.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = English_Lifestyle.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = English_Entertainment.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = English_Technology.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = English_Politics.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == ENVIRONMENT.lower():
        categoryDict = English_Environment.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = English_Travel.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = English_Science.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = English_Business.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == STOCKS.lower():
        categoryDict = English_Stocks.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == FOOD.lower():
        categoryDict = English_Food.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = English_Fashion.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == MUMBAI.lower():
        if maxClusterId:
         categoryDict = English_Mumbai.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = English_Mumbai.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PUNE.lower():
        if maxClusterId:
         categoryDict = English_Pune.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = English_Pune.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    return parseDateTimeToString(categoryDict)

def getEnglishNewsFromCategoryNew(category,limit,maxClusterId):

    if category.lower() == ECONOMY.lower():
        categoryDict = English_Economy.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == SPORTS.lower():
        categoryDict = English_Sports.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = English_Top_Stories.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = English_World.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == OPINION.lower():
        if maxClusterId:
         categoryDict = English_Opinion.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = English_Opinion.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == HEALTH.lower():
        categoryDict = English_Health.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = English_Lifestyle.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = English_Entertainment.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = English_Technology.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = English_Politics.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == ENVIRONMENT.lower():
        categoryDict = English_Environment.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = English_Travel.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = English_Science.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = English_Business.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == STOCKS.lower():
        categoryDict = English_Stocks.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == FOOD.lower():
        categoryDict = English_Food.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = English_Fashion.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == MUMBAI.lower():
        if maxClusterId:
         categoryDict = English_Mumbai.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = English_Mumbai.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PUNE.lower():
        if maxClusterId:
         categoryDict = English_Pune.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = English_Pune.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    return parseDateTimeToStringSourceName(categoryDict)

def getEnglishNewsForSource(category,limit,sourceId):
    sourceObj = News_Source.objects.get(id=sourceId)
    if category.lower() == ECONOMY.lower():
        categoryDict = English_Economy.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == SPORTS.lower():
        categoryDict = English_Sports.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = English_Top_Stories.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = English_World.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == OPINION.lower():
        categoryDict = English_Opinion.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == HEALTH.lower():
        categoryDict = English_Health.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = English_Lifestyle.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = English_Entertainment.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = English_Technology.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = English_Politics.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == ENVIRONMENT.lower():
        categoryDict = English_Environment.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = English_Travel.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = English_Science.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = English_Business.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == STOCKS.lower():
        categoryDict = English_Stocks.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == FOOD.lower():
        categoryDict = English_Food.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = English_Fashion.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == MUMBAI.lower():
        categoryDict = English_Mumbai.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == PUNE.lower():
        categoryDict = English_Pune.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    return parseDateTimeToStringSourceName(categoryDict)



# This method will be called from the HOME SCREEN. It will load news by category.
def getMarathiNewsFromCategory(category,limit,maxClusterId):
    if category.lower() == SPORTS.lower():
        categoryDict = Marathi_Sports.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = Marathi_Top_Stories.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == MAHARASHTRA.lower():
        categoryDict = Marathi_Maharashtra.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = Marathi_World.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == OPINION.lower():
        if maxClusterId:
         categoryDict = Marathi_Opinion.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Opinion.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
   
    if category.lower() == HEALTH.lower():
        categoryDict = Marathi_Health.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = Marathi_Lifestyle.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        if maxClusterId:
         categoryDict = Marathi_Entertainment.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Entertainment.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = Marathi_Technology.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = Marathi_Politics.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = Marathi_Travel.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = Marathi_Science.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = Marathi_Business.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = Marathi_Fashion.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == MUMBAI.lower():
        if maxClusterId:
         categoryDict = Marathi_Mumbai.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Mumbai.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PUNE.lower():
        if maxClusterId:
         categoryDict = Marathi_Pune.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Pune.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == NAGPUR.lower():
        if maxClusterId:
         categoryDict = Marathi_Nagpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Nagpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == NASIK.lower():
        if maxClusterId:
         categoryDict = Marathi_Nasik.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Nasik.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == AURANGABAD.lower():
        if maxClusterId:
         categoryDict = Marathi_Aurangabad.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Aurangabad.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == SOLAPUR.lower():
        if maxClusterId:
         categoryDict = Marathi_Solapur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Solapur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == KOLHAPUR.lower():
        if maxClusterId:
         categoryDict = Marathi_Kolhapur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Kolhapur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == SATARA.lower():
        if maxClusterId:
         categoryDict = Marathi_Satara.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Satara.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == SANGLI.lower():
        if maxClusterId:
         categoryDict = Marathi_Sangli.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Sangli.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == AKOLA.lower():
        if maxClusterId:
         categoryDict = Marathi_Akola.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Akola.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == AHMEDNAGAR.lower():
        if maxClusterId:
         categoryDict = Marathi_Ahmednagar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Ahmednagar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == JALGAON.lower():
        if maxClusterId:
         categoryDict = Marathi_Jalgaon.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Jalgaon.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == GOA.lower():
        if maxClusterId:
         categoryDict = Marathi_Goa.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Goa.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == CHANDRAPUR.lower():
        if maxClusterId:
         categoryDict = Marathi_Chandrapur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Chandrapur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == WARDHA.lower():
        if maxClusterId:
         categoryDict = Marathi_Wardha.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Wardha.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    return parseDateTimeToString(categoryDict)

def getMarathiNewsFromCategoryNew(category,limit,maxClusterId):
    if category.lower() == SPORTS.lower():
        categoryDict = Marathi_Sports.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = Marathi_Top_Stories.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == MAHARASHTRA.lower():
        if maxClusterId:
         categoryDict = Marathi_Maharashtra.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Maharashtra.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = Marathi_World.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == OPINION.lower():
        if maxClusterId:
         categoryDict = Marathi_Opinion.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Opinion.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == HEALTH.lower():
        if maxClusterId:
         categoryDict = Marathi_Health.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Health.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == LIFESTYLE.lower():
        if maxClusterId:
         categoryDict = Marathi_Lifestyle.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Lifestyle.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        if maxClusterId:
         categoryDict = Marathi_Entertainment.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Entertainment.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = Marathi_Technology.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = Marathi_Politics.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = Marathi_Travel.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = Marathi_Science.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == BUSINESS.lower():
        if maxClusterId:
         categoryDict = Marathi_Business.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Business.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = Marathi_Fashion.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == MUMBAI.lower():
        if maxClusterId:
         categoryDict = Marathi_Mumbai.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Mumbai.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PUNE.lower():
        if maxClusterId:
         categoryDict = Marathi_Pune.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Pune.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == NAGPUR.lower():
        if maxClusterId:
         categoryDict = Marathi_Nagpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Nagpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == NASIK.lower():
        if maxClusterId:
         categoryDict = Marathi_Nasik.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Nasik.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == AURANGABAD.lower():
        if maxClusterId:
         categoryDict = Marathi_Aurangabad.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Aurangabad.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == SOLAPUR.lower():
        if maxClusterId:
         categoryDict = Marathi_Solapur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Solapur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == KOLHAPUR.lower():
        if maxClusterId:
         categoryDict = Marathi_Kolhapur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Kolhapur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == SATARA.lower():
        if maxClusterId:
         categoryDict = Marathi_Satara.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Satara.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == SANGLI.lower():
        if maxClusterId:
         categoryDict = Marathi_Sangli.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Sangli.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == AKOLA.lower():
        if maxClusterId:
         categoryDict = Marathi_Akola.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Akola.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == AHMEDNAGAR.lower():
        if maxClusterId:
         categoryDict = Marathi_Ahmednagar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Ahmednagar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == JALGAON.lower():
        if maxClusterId:
         categoryDict = Marathi_Jalgaon.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Jalgaon.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == GOA.lower():
        if maxClusterId:
         categoryDict = Marathi_Goa.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Goa.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == CHANDRAPUR.lower():
        if maxClusterId:
         categoryDict = Marathi_Chandrapur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Chandrapur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == WARDHA.lower():
        if maxClusterId:
         categoryDict = Marathi_Wardha.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Marathi_Wardha.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    return parseDateTimeToStringSourceName(categoryDict)

def getMarathiNewsForSource(category,limit,sourceId):
    sourceObj = News_Source.objects.get(id=sourceId)
    if category.lower() == SPORTS.lower():
        categoryDict = Marathi_Sports.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = Marathi_Top_Stories.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == MAHARASHTRA.lower():
        categoryDict = Marathi_Maharashtra.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = Marathi_World.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == OPINION.lower():
        categoryDict = Marathi_Opinion.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == HEALTH.lower():
        categoryDict = Marathi_Health.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = Marathi_Lifestyle.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = Marathi_Entertainment.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = Marathi_Technology.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = Marathi_Politics.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = Marathi_Travel.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = Marathi_Science.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = Marathi_Business.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = Marathi_Fashion.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == MUMBAI.lower():
        categoryDict = Marathi_Mumbai.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == PUNE.lower():
        categoryDict = Marathi_Pune.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == NAGPUR.lower():
        categoryDict = Marathi_Nagpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == NASIK.lower():
        categoryDict = Marathi_Nasik.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == AURANGABAD.lower():
        categoryDict = Marathi_Aurangabad.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == SOLAPUR.lower():
        categoryDict = Marathi_Solapur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == KOLHAPUR.lower():
        categoryDict = Marathi_Kolhapur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == SATARA.lower():
        categoryDict = Marathi_Satara.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == SANGLI.lower():
        categoryDict = Marathi_Sangli.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == AKOLA.lower():
        categoryDict = Marathi_Akola.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == AHMEDNAGAR.lower():
        categoryDict = Marathi_Ahmednagar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == JALGAON.lower():
       categoryDict = Marathi_Jalgaon.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == GOA.lower():
       categoryDict = Marathi_Goa.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == CHANDRAPUR.lower():
       categoryDict = Marathi_Chandrapur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]

    if category.lower() == WARDHA.lower():
       categoryDict = Marathi_Wardha.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]


    return parseDateTimeToStringSourceName(categoryDict)





def getSimilarNewsArticles(lang,category,clusterId):

    limit=SIMILAR_ARTICLE_LIMIT

    if lang.lower()==ENGLISH.lower():
        categoryDict=getSimilarEnglishNewsArticles(category,limit,clusterId)

    elif lang.lower()==MARATHI.lower():
        categoryDict=getSimilarMarathiNewsArticles(category,limit,clusterId)

    return categoryDict

 # This method will be called from the HOME/CATEGORY SCREEN. It will return similar news article details.

def getSimilarNewsArticlesNew(lang,category,clusterId):

    limit=SIMILAR_ARTICLE_LIMIT

    if lang.lower()==ENGLISH.lower():
        categoryDict=getSimilarEnglishNewsArticlesNew(category,limit,clusterId)

    elif lang.lower()==MARATHI.lower():
        categoryDict=getSimilarMarathiNewsArticlesNew(category,limit,clusterId)

    elif lang.lower()==HINDI.lower():
        categoryDict=getSimilarHindiNewsArticlesNew(category,limit,clusterId)



    return categoryDict

 # This method will be called from the HOME/CATEGORY SCREEN. It will return similar news article details.

def getSimilarEnglishNewsArticles(category,limit,clusterId):
    if category.lower() == ECONOMY.lower():
        categoryDict = English_Economy.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SPORTS.lower():
        categoryDict = English_Sports.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = English_Top_Stories.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = English_World.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == OPINION.lower():
        categoryDict = English_Opinion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == HEALTH.lower():
        categoryDict = English_Health.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = English_Lifestyle.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = English_Entertainment.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = English_Technology.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = English_Politics.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == ENVIRONMENT.lower():
        categoryDict = English_Environment.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = English_Travel.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = English_Science.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = English_Business.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == STOCKS.lower():
        categoryDict = English_Stocks.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == FOOD.lower():
        categoryDict = English_Food.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = English_Fashion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == MUMBAI.lower():
        categoryDict = English_Mumbai.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == PUNE.lower():
        categoryDict = English_Pune.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    return parseDateTimeToString(categoryDict)

def getSimilarEnglishNewsArticlesNew(category,limit,clusterId):
    if category.lower() == ECONOMY.lower():
        categoryDict = English_Economy.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SPORTS.lower():
        categoryDict = English_Sports.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = English_Top_Stories.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = English_World.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == OPINION.lower():
        categoryDict = English_Opinion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == HEALTH.lower():
        categoryDict = English_Health.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = English_Lifestyle.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = English_Entertainment.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = English_Technology.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = English_Politics.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == ENVIRONMENT.lower():
        categoryDict = English_Environment.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = English_Travel.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = English_Science.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = English_Business.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == STOCKS.lower():
        categoryDict = English_Stocks.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == FOOD.lower():
        categoryDict = English_Food.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = English_Fashion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == MUMBAI.lower():
        categoryDict = English_Mumbai.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == PUNE.lower():
        categoryDict = English_Pune.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    return parseDateTimeToStringSourceName(categoryDict)



def getSimilarMarathiNewsArticles(category,limit,clusterId):
# This method will be called from the HOME/CATEGORY SCREEN. It will return similar news article details.
    if category.lower() == SPORTS.lower():
        categoryDict = Marathi_Sports.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = Marathi_Top_Stories.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = Marathi_World.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == OPINION.lower():
        categoryDict = Marathi_Opinion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == HEALTH.lower():
        categoryDict = Marathi_Health.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = Marathi_Lifestyle.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = Marathi_Entertainment.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = Marathi_Technology.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = Marathi_Politics.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = Marathi_Travel.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = Marathi_Science.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = Marathi_Business.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = Marathi_Fashion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == MUMBAI.lower():
        categoryDict = Marathi_Mumbai.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == PUNE.lower():
        categoryDict = Marathi_Pune.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == NAGPUR.lower():
        categoryDict = Marathi_Nagpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == NASIK.lower():
        categoryDict = Marathi_Nasik.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == AURANGABAD.lower():
        categoryDict = Marathi_Aurangabad.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SOLAPUR.lower():
        categoryDict = Marathi_Solapur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == KOLHAPUR.lower():
        categoryDict = Marathi_Kolhapur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SATARA.lower():
        categoryDict = Marathi_Satara.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SANGLI.lower():
        categoryDict = Marathi_Sangli.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == AKOLA.lower():
        categoryDict = Marathi_Akola.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == AHMEDNAGAR.lower():
        categoryDict = Marathi_Ahmednagar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == JALGAON.lower():
        categoryDict = Marathi_Jalgaon.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == GOA.lower():
        categoryDict = Marathi_Goa.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == CHANDRAPUR.lower():
        categoryDict = Marathi_Chandrapur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == WARDHA.lower():
        categoryDict = Marathi_Wardha.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == MAHARASHTRA.lower():
        categoryDict = Marathi_Maharashtra.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]


    return parseDateTimeToString(categoryDict)

def getSimilarMarathiNewsArticlesNew(category,limit,clusterId):

    if category.lower() == SPORTS.lower():
        categoryDict = Marathi_Sports.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = Marathi_Top_Stories.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = Marathi_World.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == OPINION.lower():
        categoryDict = Marathi_Opinion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == HEALTH.lower():
        categoryDict = Marathi_Health.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == LIFESTYLE.lower():
        categoryDict = Marathi_Lifestyle.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = Marathi_Entertainment.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        categoryDict = Marathi_Technology.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == POLITICS.lower():
        categoryDict = Marathi_Politics.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == TRAVEL.lower():
        categoryDict = Marathi_Travel.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SCIENCE.lower():
        categoryDict = Marathi_Science.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == BUSINESS.lower():
        categoryDict = Marathi_Business.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = Marathi_Fashion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == MUMBAI.lower():
        categoryDict = Marathi_Mumbai.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == PUNE.lower():
        categoryDict = Marathi_Pune.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == NAGPUR.lower():
        categoryDict = Marathi_Nagpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == NASIK.lower():
        categoryDict = Marathi_Nasik.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == AURANGABAD.lower():
        categoryDict = Marathi_Aurangabad.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SOLAPUR.lower():
        categoryDict = Marathi_Solapur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == KOLHAPUR.lower():
        categoryDict = Marathi_Kolhapur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SATARA.lower():
        categoryDict = Marathi_Satara.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == SANGLI.lower():
        categoryDict = Marathi_Sangli.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == AKOLA.lower():
        categoryDict = Marathi_Akola.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == AHMEDNAGAR.lower():
        categoryDict = Marathi_Ahmednagar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == JALGAON.lower():
        categoryDict = Marathi_Jalgaon.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == GOA.lower():
        categoryDict = Marathi_Goa.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == CHANDRAPUR.lower():
        categoryDict = Marathi_Chandrapur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == WARDHA.lower():
        categoryDict = Marathi_Wardha.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]

    if category.lower() == MAHARASHTRA.lower():
        categoryDict = Marathi_Maharashtra.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]


    return parseDateTimeToStringSourceName(categoryDict)


def getSimilarHindiNewsArticlesNew(category,limit,clusterId):
    if category.lower() == UTTARPRADESH.lower():
        categoryDict = Hindi_UttarPradesh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == UTTARAKHAND.lower():
        categoryDict = Hindi_Uttarakhand.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == HIMACHALPRADESH.lower():
        categoryDict = Hindi_HimachalPradesh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == DELHI.lower():
        categoryDict = Hindi_Delhi.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JAMMUKASHMIR.lower():
        categoryDict = Hindi_JammuKashmir.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == PUNJAB.lower():
        categoryDict = Hindi_Punjab.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MADHYAPRADESH.lower():
        categoryDict = Hindi_MadhyaPradesh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JHARKHAND.lower():
        categoryDict = Hindi_Jharkhand.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BIHAR.lower():
        categoryDict = Hindi_Bihar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == HARYANA.lower():
        categoryDict = Hindi_Haryana.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == CHATTISGARH.lower():
        categoryDict = Hindi_Chattisgarh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == RAJASTHAN.lower():
        categoryDict = Hindi_Rajasthan.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == WESTBENGAL.lower():
        categoryDict = Hindi_WestBengal.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ORISSA.lower():
        categoryDict = Hindi_Orissa.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == GUJRAT.lower():
        categoryDict = Hindi_Gujrat.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MAHARASHTRA.lower():
        categoryDict = Hindi_Maharashtra.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == LUCKNOW.lower():
        categoryDict = Hindi_Lucknow.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ALLAHABAD.lower():
        categoryDict = Hindi_Allahabad.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == PRATAPGARH.lower():
        categoryDict = Hindi_Pratapgarh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == KANPUR.lower():
        categoryDict = Hindi_Kanpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MERATH.lower():
        categoryDict = Hindi_Merath.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == AGRA.lower():
        categoryDict = Hindi_Agra.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == NOIDA.lower():
        categoryDict = Hindi_Noida.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == GAZIABAD.lower():
        categoryDict = Hindi_Gaziabad.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BAGPAT.lower():
        categoryDict = Hindi_Bagpat.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SAHARNPUR.lower():
        categoryDict = Hindi_Saharnpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BULANDSHAHAR.lower():
        categoryDict = Hindi_Bulandshahar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == VARANASI.lower():
        categoryDict = Hindi_Varanasi.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == GORAKHPUR.lower():
        categoryDict = Hindi_Gorakhpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JHANSI.lower():
        categoryDict = Hindi_Jhansi.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MUZAFFARNAGAR.lower():
        categoryDict = Hindi_Muzaffarnagar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SITAPUR.lower():
        categoryDict = Hindi_Sitapur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JAUNPUR.lower():
        categoryDict = Hindi_Jaunpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == AZAMGARH.lower():
        categoryDict = Hindi_Azamgarh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MORADABAD.lower():
        categoryDict = Hindi_Moradabad.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BAREILLY.lower():
        categoryDict = Hindi_Bareilly.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BALIA.lower():
        categoryDict = Hindi_Balia.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ALIGARH.lower():
        categoryDict = Hindi_Aligarh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MATHURA.lower():
        categoryDict = Hindi_Mathura.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BHOPAL.lower():
        categoryDict = Hindi_Bhopal.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == INDORE.lower():
        categoryDict = Hindi_Indore.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == GWALIOR.lower():
        categoryDict = Hindi_Gwalior.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JABALPUR.lower():
        categoryDict = Hindi_Jabalpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == UJJAIN.lower():
        categoryDict = Hindi_Ujjain.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == RATLAM.lower():
        categoryDict = Hindi_Ratlam.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SAGAR.lower():
        categoryDict = Hindi_Sagar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == DEWAS.lower():
        categoryDict = Hindi_Dewas.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SATNA.lower():
        categoryDict = Hindi_Satna.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == REWA.lower():
        categoryDict = Hindi_Rewa.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == PATNA.lower():
        categoryDict = Hindi_Patna.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BHAGALPUR.lower():
        categoryDict = Hindi_Bhagalpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MUJAFFARPUR.lower():
        categoryDict = Hindi_Mujaffarpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == GAYA.lower():
        categoryDict = Hindi_Gaya.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == DARBHANGA.lower():
        categoryDict = Hindi_Darbhanga.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == POORNIYA.lower():
        categoryDict = Hindi_Poorniya.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SEWAN.lower():
        categoryDict = Hindi_Sewan.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BEGUSARAI.lower():
        categoryDict = Hindi_Begusarai.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == KATIHAR.lower():
        categoryDict = Hindi_Katihar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JAIPUR.lower():
        categoryDict = Hindi_Jaipur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == UDAIPUR.lower():
        categoryDict = Hindi_Udaipur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JODHPUR.lower():
        categoryDict = Hindi_Jodhpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == AJMER.lower():
        categoryDict = Hindi_Ajmer.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BIKANER.lower():
        categoryDict = Hindi_Bikaner.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ALWAR.lower():
        categoryDict = Hindi_Alwar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SIKAR.lower():
        categoryDict = Hindi_Sikar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == KOTA.lower():
        categoryDict = Hindi_Kota.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BHILWARA.lower():
        categoryDict = Hindi_Bhilwara.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BHARATPUR.lower():
        categoryDict = Hindi_Bharatpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == CHHATIS.lower():
        categoryDict = Hindi_Chhatis.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == RAIPUR.lower():
        categoryDict = Hindi_Raipur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BHILAI.lower():
        categoryDict = Hindi_Bhilai.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == RAJNANDGAO.lower():
        categoryDict = Hindi_Rajnandgao.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == RAIGARH.lower():
        categoryDict = Hindi_Raigarh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JAGDALPUR.lower():
        categoryDict = Hindi_Jagdalpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == KORVA.lower():
        categoryDict = Hindi_Korva.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == RANCHI.lower():
        categoryDict = Hindi_Ranchi.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == DHANBAD.lower():
        categoryDict = Hindi_Dhanbad.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JAMSHEDPUR.lower():
        categoryDict = Hindi_Jamshedpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == GIRIDIHI.lower():
        categoryDict = Hindi_Giridihi.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == HAZARIBAGH.lower():
        categoryDict = Hindi_Hazaribagh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BOKARO.lower():
        categoryDict = Hindi_Bokaro.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == DEHRADUN.lower():
        categoryDict = Hindi_Dehradun.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == NAINITAAL.lower():
        categoryDict = Hindi_Nainitaal.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == HARIDWAAR.lower():
        categoryDict = Hindi_Haridwaar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ALMORAH.lower():
        categoryDict = Hindi_Almorah.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == UDDHAMSINGHNAGAR.lower():
        categoryDict = Hindi_UddhamSinghNagar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SIMLA.lower():
        categoryDict = Hindi_Simla.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MANDI.lower():
        categoryDict = Hindi_Mandi.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BILASPUR.lower():
        categoryDict = Hindi_Bilaspur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == AMRITSAR.lower():
        categoryDict = Hindi_Amritsar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JALANDHAR.lower():
        categoryDict = Hindi_Jalandhar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == LUDHIANA.lower():
        categoryDict = Hindi_Ludhiana.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ROPARH.lower():
        categoryDict = Hindi_Roparh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == CHANDIGARH.lower():
        categoryDict = Hindi_Chandigarh.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ROHTAK.lower():
        categoryDict = Hindi_Rohtak.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == PANCHKULA.lower():
        categoryDict = Hindi_Panchkula.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == AMBALA.lower():
        categoryDict = Hindi_Ambala.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == PANIPAT.lower():
        categoryDict = Hindi_Panipat.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == GURGAON.lower():
        categoryDict = Hindi_Gurgaon.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == HISSAR.lower():
        categoryDict = Hindi_Hissar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JAMMU.lower():
        categoryDict = Hindi_Jammu.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SRINAGAR.lower():
        categoryDict = Hindi_Srinagar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == POONCH.lower():
        categoryDict = Hindi_Poonch.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == KOLKATA.lower():
        categoryDict = Hindi_Kolkata.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == JALPAIGURHI.lower():
        categoryDict = Hindi_Jalpaigurhi.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == DARJEELING.lower():
        categoryDict = Hindi_Darjeeling.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ASANSOL.lower():
        categoryDict = Hindi_Asansol.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SILIGURHI.lower():
        categoryDict = Hindi_Siligurhi.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BHUVANESHWAR.lower():
        categoryDict = Hindi_Bhuvaneshwar.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == PURI.lower():
        categoryDict = Hindi_Puri.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == CUTTACK.lower():
        categoryDict = Hindi_Cuttack.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == AHMEDABAD.lower():
        categoryDict = Hindi_Ahmedabad.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SURAT.lower():
        categoryDict = Hindi_Surat.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == VADODARA.lower():
        categoryDict = Hindi_Vadodara.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == MUMBAI.lower():
        categoryDict = Hindi_Mumbai.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == NAGPUR.lower():
        categoryDict = Hindi_Nagpur.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == PUNE.lower():
        categoryDict = Hindi_Pune.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SPORTS.lower():
        categoryDict = Hindi_Sports.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == TOP_STORIES.lower():
        categoryDict = Hindi_Top_Stories.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == WORLD.lower():
        categoryDict = Hindi_World.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == OPINION.lower():
        categoryDict = Hindi_Opinion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == HEALTH.lower():
        categoryDict = Hindi_Health.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == LIFESTYLE.lower():
        categoryDict = Hindi_Lifestyle.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = Hindi_Entertainment.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == TECHNOLOGY.lower():
        categoryDict = Hindi_Technology.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == POLITICS.lower():
        categoryDict = Hindi_Politics.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == ENVIRONMENT.lower():
        categoryDict = Hindi_Environment.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == TRAVEL.lower():
        categoryDict = Hindi_Travel.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == SCIENCE.lower():
        categoryDict = Hindi_Science.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == BUSINESS.lower():
        categoryDict = Hindi_Business.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == STOCKS.lower():
        categoryDict = Hindi_Stocks.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == FOOD.lower():
        categoryDict = Hindi_Food.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == WEEKEND.lower():
        categoryDict = Hindi_Weekend.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    if category.lower() == FASHION.lower():
        categoryDict = Hindi_Fashion.objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]
    return parseDateTimeToStringSourceName(categoryDict)

def getHindiNewsFromCategoryNew(category,limit,maxClusterId):
    if category.lower() == SPORTS.lower():
        categoryDict = Hindi_Sports.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == CRIME.lower():
        if maxClusterId:
         categoryDict = Hindi_Crime.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Crime.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == AUTO.lower():
        if maxClusterId:
         categoryDict = Hindi_Auto.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Auto.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == TOP_STORIES.lower():
        categoryDict = Hindi_Top_Stories.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == MAHARASHTRA.lower():
        if maxClusterId:
         categoryDict = Hindi_Maharashtra.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Maharashtra.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == WORLD.lower():
        categoryDict = Hindi_World.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]

    if category.lower() == OPINION.lower():
        if maxClusterId:
         categoryDict = Hindi_Opinion.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Opinion.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == HEALTH.lower():
        if maxClusterId:
         categoryDict = Hindi_Health.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Health.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == LIFESTYLE.lower():
        if maxClusterId:
         categoryDict = Hindi_Lifestyle.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Lifestyle.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == ENTERTAINMENT.lower():
        if maxClusterId:
         categoryDict = Hindi_Entertainment.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Entertainment.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == TECHNOLOGY.lower():
        if maxClusterId:
         categoryDict = Hindi_Technology.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Technology.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == POLITICS.lower():
        if maxClusterId:
         categoryDict = Hindi_Politics.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Politics.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == TRAVEL.lower():
        if maxClusterId:
         categoryDict = Hindi_Travel.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Travel.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == SCIENCE.lower():
        if maxClusterId:
         categoryDict = Hindi_Science.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Science.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == BUSINESS.lower():
        if maxClusterId:
         categoryDict = Hindi_Business.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
         categoryDict = Hindi_Business.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]

    if category.lower() == FASHION.lower():
        categoryDict = Hindi_Fashion.objects.filter(Is_Rep = 1,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]


    if category.lower() == UTTARPRADESH.lower():
        if maxClusterId:
            categoryDict = Hindi_UttarPradesh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_UttarPradesh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == UTTARAKHAND.lower():
        if maxClusterId:
            categoryDict = Hindi_Uttarakhand.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Uttarakhand.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == HIMACHALPRADESH.lower():
        if maxClusterId:
            categoryDict = Hindi_HimachalPradesh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_HimachalPradesh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == DELHI.lower():
        if maxClusterId:
            categoryDict = Hindi_Delhi.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Delhi.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JAMMUKASHMIR.lower():
        if maxClusterId:
            categoryDict = Hindi_JammuKashmir.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_JammuKashmir.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PUNJAB.lower():
        if maxClusterId:
            categoryDict = Hindi_Punjab.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Punjab.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MADHYAPRADESH.lower():
        if maxClusterId:
            categoryDict = Hindi_MadhyaPradesh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_MadhyaPradesh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JHARKHAND.lower():
        if maxClusterId:
            categoryDict = Hindi_Jharkhand.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jharkhand.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BIHAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Bihar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bihar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == HARYANA.lower():
        if maxClusterId:
            categoryDict = Hindi_Haryana.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Haryana.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == CHATTISGARH.lower():
        if maxClusterId:
            categoryDict = Hindi_Chattisgarh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Chattisgarh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == RAJASTHAN.lower():
        if maxClusterId:
            categoryDict = Hindi_Rajasthan.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Rajasthan.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == WESTBENGAL.lower():
        if maxClusterId:
            categoryDict = Hindi_WestBengal.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_WestBengal.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == ORISSA.lower():
        if maxClusterId:
            categoryDict = Hindi_Orissa.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Orissa.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == GUJRAT.lower():
        if maxClusterId:
            categoryDict = Hindi_Gujrat.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Gujrat.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MAHARASHTRA.lower():
        if maxClusterId:
            categoryDict = Hindi_Maharashtra.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Maharashtra.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == LUCKNOW.lower():
        if maxClusterId:
            categoryDict = Hindi_Lucknow.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Lucknow.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == ALLAHABAD.lower():
        if maxClusterId:
            categoryDict = Hindi_Allahabad.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Allahabad.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PRATAPGARH.lower():
        if maxClusterId:
            categoryDict = Hindi_Pratapgarh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Pratapgarh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == KANPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Kanpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Kanpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MERATH.lower():
        if maxClusterId:
            categoryDict = Hindi_Merath.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Merath.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == AGRA.lower():
        if maxClusterId:
            categoryDict = Hindi_Agra.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Agra.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == NOIDA.lower():
        if maxClusterId:
            categoryDict = Hindi_Noida.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Noida.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == GAZIABAD.lower():
        if maxClusterId:
            categoryDict = Hindi_Gaziabad.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Gaziabad.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BAGPAT.lower():
        if maxClusterId:
            categoryDict = Hindi_Bagpat.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bagpat.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SAHARNPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Saharnpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Saharnpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BULANDSHAHAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Bulandshahar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bulandshahar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == VARANASI.lower():
        if maxClusterId:
            categoryDict = Hindi_Varanasi.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Varanasi.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == GORAKHPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Gorakhpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Gorakhpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JHANSI.lower():
        if maxClusterId:
            categoryDict = Hindi_Jhansi.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jhansi.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MUZAFFARNAGAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Muzaffarnagar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Muzaffarnagar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SITAPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Sitapur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Sitapur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JAUNPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Jaunpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jaunpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == AZAMGARH.lower():
        if maxClusterId:
            categoryDict = Hindi_Azamgarh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Azamgarh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MORADABAD.lower():
        if maxClusterId:
            categoryDict = Hindi_Moradabad.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Moradabad.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BAREILLY.lower():
        if maxClusterId:
            categoryDict = Hindi_Bareilly.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bareilly.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BALIA.lower():
        if maxClusterId:
            categoryDict = Hindi_Balia.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Balia.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == ALIGARH.lower():
        if maxClusterId:
            categoryDict = Hindi_Aligarh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Aligarh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MATHURA.lower():
        if maxClusterId:
            categoryDict = Hindi_Mathura.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Mathura.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BHOPAL.lower():
        if maxClusterId:
            categoryDict = Hindi_Bhopal.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bhopal.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == INDORE.lower():
        if maxClusterId:
            categoryDict = Hindi_Indore.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Indore.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == GWALIOR.lower():
        if maxClusterId:
            categoryDict = Hindi_Gwalior.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Gwalior.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JABALPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Jabalpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jabalpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == UJJAIN.lower():
        if maxClusterId:
            categoryDict = Hindi_Ujjain.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Ujjain.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == RATLAM.lower():
        if maxClusterId:
            categoryDict = Hindi_Ratlam.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Ratlam.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SAGAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Sagar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Sagar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == DEWAS.lower():
        if maxClusterId:
            categoryDict = Hindi_Dewas.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Dewas.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SATNA.lower():
        if maxClusterId:
            categoryDict = Hindi_Satna.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Satna.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == REWA.lower():
        if maxClusterId:
            categoryDict = Hindi_Rewa.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Rewa.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PATNA.lower():
        if maxClusterId:
            categoryDict = Hindi_Patna.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Patna.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BHAGALPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Bhagalpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bhagalpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MUJAFFARPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Mujaffarpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Mujaffarpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == GAYA.lower():
        if maxClusterId:
            categoryDict = Hindi_Gaya.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Gaya.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == DARBHANGA.lower():
        if maxClusterId:
            categoryDict = Hindi_Darbhanga.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Darbhanga.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == POORNIYA.lower():
        if maxClusterId:
            categoryDict = Hindi_Poorniya.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Poorniya.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SEWAN.lower():
        if maxClusterId:
            categoryDict = Hindi_Sewan.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Sewan.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BEGUSARAI.lower():
        if maxClusterId:
            categoryDict = Hindi_Begusarai.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Begusarai.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == KATIHAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Katihar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Katihar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JAIPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Jaipur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jaipur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == UDAIPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Udaipur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Udaipur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JODHPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Jodhpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jodhpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == AJMER.lower():
        if maxClusterId:
            categoryDict = Hindi_Ajmer.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Ajmer.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BIKANER.lower():
        if maxClusterId:
            categoryDict = Hindi_Bikaner.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bikaner.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == ALWAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Alwar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Alwar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SIKAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Sikar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Sikar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == KOTA.lower():
        if maxClusterId:
            categoryDict = Hindi_Kota.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Kota.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BHILWARA.lower():
        if maxClusterId:
            categoryDict = Hindi_Bhilwara.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bhilwara.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BHARATPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Bharatpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bharatpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == CHHATIS.lower():
        if maxClusterId:
            categoryDict = Hindi_Chhatis.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Chhatis.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == RAIPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Raipur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Raipur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BHILAI.lower():
        if maxClusterId:
            categoryDict = Hindi_Bhilai.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bhilai.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == RAJNANDGAO.lower():
        if maxClusterId:
            categoryDict = Hindi_Rajnandgao.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Rajnandgao.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == RAIGARH.lower():
        if maxClusterId:
            categoryDict = Hindi_Raigarh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Raigarh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JAGDALPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Jagdalpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jagdalpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == KORVA.lower():
        if maxClusterId:
            categoryDict = Hindi_Korva.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Korva.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == RANCHI.lower():
        if maxClusterId:
            categoryDict = Hindi_Ranchi.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Ranchi.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == DHANBAD.lower():
        if maxClusterId:
            categoryDict = Hindi_Dhanbad.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Dhanbad.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JAMSHEDPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Jamshedpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jamshedpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == GIRIDIHI.lower():
        if maxClusterId:
            categoryDict = Hindi_Giridihi.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Giridihi.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == HAZARIBAGH.lower():
        if maxClusterId:
            categoryDict = Hindi_Hazaribagh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Hazaribagh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BOKARO.lower():
        if maxClusterId:
            categoryDict = Hindi_Bokaro.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bokaro.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == DEHRADUN.lower():
        if maxClusterId:
            categoryDict = Hindi_Dehradun.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Dehradun.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == NAINITAAL.lower():
        if maxClusterId:
            categoryDict = Hindi_Nainitaal.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Nainitaal.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == HARIDWAAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Haridwaar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Haridwaar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == ALMORAH.lower():
        if maxClusterId:
            categoryDict = Hindi_Almorah.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Almorah.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == UDDHAMSINGHNAGAR.lower():
        if maxClusterId:
            categoryDict = Hindi_UddhamSinghNagar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_UddhamSinghNagar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SIMLA.lower():
        if maxClusterId:
            categoryDict = Hindi_Simla.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Simla.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MANDI.lower():
        if maxClusterId:
            categoryDict = Hindi_Mandi.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Mandi.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BILASPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Bilaspur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bilaspur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == AMRITSAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Amritsar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Amritsar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JALANDHAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Jalandhar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jalandhar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == LUDHIANA.lower():
        if maxClusterId:
            categoryDict = Hindi_Ludhiana.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Ludhiana.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == ROPARH.lower():
        if maxClusterId:
            categoryDict = Hindi_Roparh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Roparh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == CHANDIGARH.lower():
        if maxClusterId:
            categoryDict = Hindi_Chandigarh.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Chandigarh.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == ROHTAK.lower():
        if maxClusterId:
            categoryDict = Hindi_Rohtak.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Rohtak.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PANCHKULA.lower():
        if maxClusterId:
            categoryDict = Hindi_Panchkula.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Panchkula.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == AMBALA.lower():
        if maxClusterId:
            categoryDict = Hindi_Ambala.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Ambala.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PANIPAT.lower():
        if maxClusterId:
            categoryDict = Hindi_Panipat.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Panipat.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == GURGAON.lower():
        if maxClusterId:
            categoryDict = Hindi_Gurgaon.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Gurgaon.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == HISSAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Hissar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Hissar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JAMMU.lower():
        if maxClusterId:
            categoryDict = Hindi_Jammu.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jammu.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SRINAGAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Srinagar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Srinagar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == POONCH.lower():
        if maxClusterId:
            categoryDict = Hindi_Poonch.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Poonch.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == KOLKATA.lower():
        if maxClusterId:
            categoryDict = Hindi_Kolkata.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Kolkata.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == JALPAIGURHI.lower():
        if maxClusterId:
            categoryDict = Hindi_Jalpaigurhi.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Jalpaigurhi.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == DARJEELING.lower():
        if maxClusterId:
            categoryDict = Hindi_Darjeeling.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Darjeeling.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == ASANSOL.lower():
        if maxClusterId:
            categoryDict = Hindi_Asansol.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Asansol.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SILIGURHI.lower():
        if maxClusterId:
            categoryDict = Hindi_Siligurhi.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Siligurhi.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == BHUVANESHWAR.lower():
        if maxClusterId:
            categoryDict = Hindi_Bhuvaneshwar.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Bhuvaneshwar.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PURI.lower():
        if maxClusterId:
            categoryDict = Hindi_Puri.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Puri.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == CUTTACK.lower():
        if maxClusterId:
            categoryDict = Hindi_Cuttack.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Cuttack.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == AHMEDABAD.lower():
        if maxClusterId:
            categoryDict = Hindi_Ahmedabad.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Ahmedabad.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == SURAT.lower():
        if maxClusterId:
            categoryDict = Hindi_Surat.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Surat.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == VADODARA.lower():
        if maxClusterId:
            categoryDict = Hindi_Vadodara.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Vadodara.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == MUMBAI.lower():
        if maxClusterId:
            categoryDict = Hindi_Mumbai.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Mumbai.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == NAGPUR.lower():
        if maxClusterId:
            categoryDict = Hindi_Nagpur.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Nagpur.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]
    if category.lower() == PUNE.lower():
        if maxClusterId:
            categoryDict = Hindi_Pune.objects.filter(Is_Rep = 1,Cluster_Id__lt=maxClusterId).order_by('-Cluster_Id')[:limit]
        else:
            categoryDict = Hindi_Pune.objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]



    return parseDateTimeToStringSourceName(categoryDict)

def getHindiNewsForSource(category, limit,sourceId):
    sourceObj = News_Source.objects.get(id=sourceId)
    if category.lower() == UTTARPRADESH.lower():
        categoryDict = Hindi_UttarPradesh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == UTTARAKHAND.lower():
        categoryDict = Hindi_Uttarakhand.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == HIMACHALPRADESH.lower():
        categoryDict = Hindi_HimachalPradesh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == DELHI.lower():
        categoryDict = Hindi_Delhi.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JAMMUKASHMIR.lower():
        categoryDict = Hindi_JammuKashmir.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == PUNJAB.lower():
        categoryDict = Hindi_Punjab.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MADHYAPRADESH.lower():
        categoryDict = Hindi_MadhyaPradesh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JHARKHAND.lower():
        categoryDict = Hindi_Jharkhand.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BIHAR.lower():
        categoryDict = Hindi_Bihar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == HARYANA.lower():
        categoryDict = Hindi_Haryana.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == CHATTISGARH.lower():
        categoryDict = Hindi_Chattisgarh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == RAJASTHAN.lower():
        categoryDict = Hindi_Rajasthan.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == WESTBENGAL.lower():
        categoryDict = Hindi_WestBengal.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ORISSA.lower():
        categoryDict = Hindi_Orissa.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == GUJRAT.lower():
        categoryDict = Hindi_Gujrat.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MAHARASHTRA.lower():
        categoryDict = Hindi_Maharashtra.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == LUCKNOW.lower():
        categoryDict = Hindi_Lucknow.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ALLAHABAD.lower():
        categoryDict = Hindi_Allahabad.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == PRATAPGARH.lower():
        categoryDict = Hindi_Pratapgarh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == KANPUR.lower():
        categoryDict = Hindi_Kanpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MERATH.lower():
        categoryDict = Hindi_Merath.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == AGRA.lower():
        categoryDict = Hindi_Agra.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == NOIDA.lower():
        categoryDict = Hindi_Noida.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == GAZIABAD.lower():
        categoryDict = Hindi_Gaziabad.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BAGPAT.lower():
        categoryDict = Hindi_Bagpat.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SAHARNPUR.lower():
        categoryDict = Hindi_Saharnpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BULANDSHAHAR.lower():
        categoryDict = Hindi_Bulandshahar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == VARANASI.lower():
        categoryDict = Hindi_Varanasi.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == GORAKHPUR.lower():
        categoryDict = Hindi_Gorakhpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JHANSI.lower():
        categoryDict = Hindi_Jhansi.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MUZAFFARNAGAR.lower():
        categoryDict = Hindi_Muzaffarnagar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SITAPUR.lower():
        categoryDict = Hindi_Sitapur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JAUNPUR.lower():
        categoryDict = Hindi_Jaunpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == AZAMGARH.lower():
        categoryDict = Hindi_Azamgarh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MORADABAD.lower():
        categoryDict = Hindi_Moradabad.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BAREILLY.lower():
        categoryDict = Hindi_Bareilly.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BALIA.lower():
        categoryDict = Hindi_Balia.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ALIGARH.lower():
        categoryDict = Hindi_Aligarh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MATHURA.lower():
        categoryDict = Hindi_Mathura.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BHOPAL.lower():
        categoryDict = Hindi_Bhopal.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == INDORE.lower():
        categoryDict = Hindi_Indore.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == GWALIOR.lower():
        categoryDict = Hindi_Gwalior.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JABALPUR.lower():
        categoryDict = Hindi_Jabalpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == UJJAIN.lower():
        categoryDict = Hindi_Ujjain.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == RATLAM.lower():
        categoryDict = Hindi_Ratlam.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SAGAR.lower():
        categoryDict = Hindi_Sagar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == DEWAS.lower():
        categoryDict = Hindi_Dewas.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SATNA.lower():
        categoryDict = Hindi_Satna.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == REWA.lower():
        categoryDict = Hindi_Rewa.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == PATNA.lower():
        categoryDict = Hindi_Patna.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BHAGALPUR.lower():
        categoryDict = Hindi_Bhagalpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MUJAFFARPUR.lower():
        categoryDict = Hindi_Mujaffarpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == GAYA.lower():
        categoryDict = Hindi_Gaya.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == DARBHANGA.lower():
        categoryDict = Hindi_Darbhanga.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == POORNIYA.lower():
        categoryDict = Hindi_Poorniya.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SEWAN.lower():
        categoryDict = Hindi_Sewan.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BEGUSARAI.lower():
        categoryDict = Hindi_Begusarai.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == KATIHAR.lower():
        categoryDict = Hindi_Katihar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JAIPUR.lower():
        categoryDict = Hindi_Jaipur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == UDAIPUR.lower():
        categoryDict = Hindi_Udaipur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JODHPUR.lower():
        categoryDict = Hindi_Jodhpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == AJMER.lower():
        categoryDict = Hindi_Ajmer.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BIKANER.lower():
        categoryDict = Hindi_Bikaner.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ALWAR.lower():
        categoryDict = Hindi_Alwar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SIKAR.lower():
        categoryDict = Hindi_Sikar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == KOTA.lower():
        categoryDict = Hindi_Kota.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BHILWARA.lower():
        categoryDict = Hindi_Bhilwara.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BHARATPUR.lower():
        categoryDict = Hindi_Bharatpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == CHHATIS.lower():
        categoryDict = Hindi_Chhatis.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == RAIPUR.lower():
        categoryDict = Hindi_Raipur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BHILAI.lower():
        categoryDict = Hindi_Bhilai.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == RAJNANDGAO.lower():
        categoryDict = Hindi_Rajnandgao.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == RAIGARH.lower():
        categoryDict = Hindi_Raigarh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JAGDALPUR.lower():
        categoryDict = Hindi_Jagdalpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == KORVA.lower():
        categoryDict = Hindi_Korva.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == RANCHI.lower():
        categoryDict = Hindi_Ranchi.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == DHANBAD.lower():
        categoryDict = Hindi_Dhanbad.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JAMSHEDPUR.lower():
        categoryDict = Hindi_Jamshedpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == GIRIDIHI.lower():
        categoryDict = Hindi_Giridihi.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == HAZARIBAGH.lower():
        categoryDict = Hindi_Hazaribagh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BOKARO.lower():
        categoryDict = Hindi_Bokaro.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == DEHRADUN.lower():
        categoryDict = Hindi_Dehradun.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == NAINITAAL.lower():
        categoryDict = Hindi_Nainitaal.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == HARIDWAAR.lower():
        categoryDict = Hindi_Haridwaar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ALMORAH.lower():
        categoryDict = Hindi_Almorah.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == UDDHAMSINGHNAGAR.lower():
        categoryDict = Hindi_UddhamSinghNagar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SIMLA.lower():
        categoryDict = Hindi_Simla.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MANDI.lower():
        categoryDict = Hindi_Mandi.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BILASPUR.lower():
        categoryDict = Hindi_Bilaspur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == AMRITSAR.lower():
        categoryDict = Hindi_Amritsar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JALANDHAR.lower():
        categoryDict = Hindi_Jalandhar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == LUDHIANA.lower():
        categoryDict = Hindi_Ludhiana.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ROPARH.lower():
        categoryDict = Hindi_Roparh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == CHANDIGARH.lower():
        categoryDict = Hindi_Chandigarh.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ROHTAK.lower():
        categoryDict = Hindi_Rohtak.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == PANCHKULA.lower():
        categoryDict = Hindi_Panchkula.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == AMBALA.lower():
        categoryDict = Hindi_Ambala.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == PANIPAT.lower():
        categoryDict = Hindi_Panipat.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == GURGAON.lower():
        categoryDict = Hindi_Gurgaon.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == HISSAR.lower():
        categoryDict = Hindi_Hissar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JAMMU.lower():
        categoryDict = Hindi_Jammu.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SRINAGAR.lower():
        categoryDict = Hindi_Srinagar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == POONCH.lower():
        categoryDict = Hindi_Poonch.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == KOLKATA.lower():
        categoryDict = Hindi_Kolkata.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == JALPAIGURHI.lower():
        categoryDict = Hindi_Jalpaigurhi.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == DARJEELING.lower():
        categoryDict = Hindi_Darjeeling.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ASANSOL.lower():
        categoryDict = Hindi_Asansol.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SILIGURHI.lower():
        categoryDict = Hindi_Siligurhi.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BHUVANESHWAR.lower():
        categoryDict = Hindi_Bhuvaneshwar.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == PURI.lower():
        categoryDict = Hindi_Puri.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == CUTTACK.lower():
        categoryDict = Hindi_Cuttack.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == AHMEDABAD.lower():
        categoryDict = Hindi_Ahmedabad.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SURAT.lower():
        categoryDict = Hindi_Surat.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == VADODARA.lower():
        categoryDict = Hindi_Vadodara.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == MUMBAI.lower():
        categoryDict = Hindi_Mumbai.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == NAGPUR.lower():
        categoryDict = Hindi_Nagpur.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == PUNE.lower():
        categoryDict = Hindi_Pune.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SPORTS.lower():
        categoryDict = Hindi_Sports.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == TOP_STORIES.lower():
        categoryDict = Hindi_Top_Stories.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == WORLD.lower():
        categoryDict = Hindi_World.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == OPINION.lower():
        categoryDict = Hindi_Opinion.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == HEALTH.lower():
        categoryDict = Hindi_Health.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == LIFESTYLE.lower():
        categoryDict = Hindi_Lifestyle.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ENTERTAINMENT.lower():
        categoryDict = Hindi_Entertainment.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == TECHNOLOGY.lower():
        categoryDict = Hindi_Technology.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == POLITICS.lower():
        categoryDict = Hindi_Politics.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == ENVIRONMENT.lower():
        categoryDict = Hindi_Environment.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == TRAVEL.lower():
        categoryDict = Hindi_Travel.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == SCIENCE.lower():
        categoryDict = Hindi_Science.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == BUSINESS.lower():
        categoryDict = Hindi_Business.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == STOCKS.lower():
        categoryDict = Hindi_Stocks.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == FOOD.lower():
        categoryDict = Hindi_Food.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == WEEKEND.lower():
        categoryDict = Hindi_Weekend.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]
    if category.lower() == FASHION.lower():
        categoryDict = Hindi_Fashion.objects.filter(Source = sourceObj).order_by('-Published_Date')[:limit]


    return parseDateTimeToStringSourceName(categoryDict)










def parseDateTimeToString(dictList):
    thumbStr='Thumbnail'
    isRepStr='Is_Rep'
    titleStr='Title'
    urlStr='URL'
    summStr='Summary'
    clusterStr='-Published_Date'
    sourceStr='Source_id'
    articleStr='Article_id'
    idStr='id'
    pubDateStr='Published_Date'
    currDateStr = 'Current_Date'
    newsDictList=[]
    for rec in dictList:
     newsDict={}
     newsDict[thumbStr]=rec.Thumbnail
     if rec.Is_Rep:
      newsDict[isRepStr]=1
     else:
      newsDict[isRepStr]=0
     newsDict[titleStr]=rec.Title
     finalUrl = checkForMobileURL(rec.URL,rec.Source_id)
     newsDict[urlStr]=finalUrl
     newsDict[summStr]=rec.Summary
     newsDict[clusterStr]=rec.Cluster_Id
     newsDict[sourceStr]=rec.Source_id
     newsDict[articleStr]=rec.Article_id
     newsDict[idStr]=rec.id
     articleObj = News_Article.objects.get(id = rec.Article_id)
     if articleObj.Current_Date - rec.Published_Date < datetime.timedelta(minutes=2) and articleObj.Current_Date - rec.Published_Date >= datetime.timedelta(minutes=0):
         rec.Published_Date = rec.Published_Date + datetime.timedelta(hours=5,minutes=30)
     newsDict[pubDateStr]=rec.Published_Date.strftime('%Y-%m-%d %H:%M')
     newsDictList.append(newsDict)
    return newsDictList

def parseDateTimeToStringSourceName(dictList):
    thumbStr='Thumbnail'
    isRepStr='Is_Rep'
    titleStr='Title'
    urlStr='URL'
    summStr='Summary'
    clusterStr='Cluster_Id'
    sourceStr='Source_id'
    sourceStrForNews='Source_id_News'
    articleStr='Article_id'
    idStr='id'
    pubDateStr='Published_Date'
    currDateStr = 'Current_Date'
    newsDictList=[]
    for rec in dictList:
        newsDict={}
        newsDict[thumbStr]=rec.Thumbnail
        if rec.Is_Rep:
            newsDict[isRepStr]=1
        else:
            newsDict[isRepStr]=0
        newsDict[titleStr]=rec.Title
        finalUrl = checkForMobileURL(rec.URL,rec.Source_id)
        newsDict[urlStr]=finalUrl
        newsDict[summStr]=rec.Summary
        newsDict[clusterStr]=rec.Cluster_Id
        newsDict[sourceStrForNews] = rec.Source_id

        sourceObj = News_Source.objects.get(id=rec.Source_id)
        foundSource = False
        f=open(SOURCE_MARATHI_FILE,'r')
        for line in f:
            marathiSourceLine = line
            marathiSourceId = marathiSourceLine.split('=')[0]
            marathiSourceName = marathiSourceLine.split('=')[1]
            marathiSourceName = marathiSourceName.split('\r\n')[0]
            if foundSource == False and rec.Source_id == int(marathiSourceId):
                newsDict[sourceStr]=marathiSourceName
                foundSource = True
        f.close()
        if foundSource == False:
            newsDict[sourceStr]=sourceObj.Name

        newsDict[articleStr]=rec.Article_id
        newsDict[idStr]=rec.id
        articleObj = News_Article.objects.get(id = rec.Article_id)
        if articleObj.Current_Date - rec.Published_Date < datetime.timedelta(minutes=3) and articleObj.Current_Date - rec.Published_Date >= datetime.timedelta(minutes=0):
            rec.Published_Date = rec.Published_Date + datetime.timedelta(hours=5,minutes=30)
        newsDict[pubDateStr]=rec.Published_Date.strftime('%Y-%m-%d %H:%M')
        newsDictList.append(newsDict)
    return newsDictList

def __if_number_get_string(number):
    converted_str = number
    if isinstance(number, int) or \
       isinstance(number, float):
        converted_str = str(number)
    return converted_str

def get_unicode(strOrUnicode, encoding='utf-8'):
    strOrUnicode = __if_number_get_string(strOrUnicode)
    if isinstance(strOrUnicode, unicode):
        return strOrUnicode
    return unicode(strOrUnicode, encoding, errors='ignore')


def getSimilarTopN(lang):
    #Send Notifications
    if lang.lower() == ENGLISH.lower():
        categoryDict = TopN_English.objects.filter()

    if lang.lower() == MARATHI.lower():
        categoryDict = TopN_Marathi.objects.filter()

    if lang.lower() == HINDI.lower():
        categoryDict = TopN_Hindi.objects.filter()

    return parseDateTimeToStringTopN(categoryDict)

def parseDateTimeToStringTopN(dictList):
    thumbStr='Thumbnail'
    #isRepStr='Is_Rep'
    titleStr='Title'
    urlStr='URL'
    summStr='Summary'
    #clusterStr='Cluster_Id'
    sourceStr='Source_id'
    articleStr='Article_id'
    idStr='id'
    pubDateStr='Published_Date'
    newsDictList=[]
    for rec in dictList:
     newsDict={}
     newsDict[thumbStr]=rec.Thumbnail
     #if rec.Is_Rep:
      #newsDict[isRepStr]=1
     #else:
      #newsDict[isRepStr]=0
     newsDict[titleStr]=rec.Title
     newsDict[urlStr]=rec.URL
     newsDict[summStr]=rec.Summary
     #newsDict[clusterStr]=rec.Cluster_Id
     newsDict[sourceStr]=rec.Source_id
     newsDict[articleStr]=rec.Article_id
     newsDict[idStr]=rec.id
     newsDict[pubDateStr]=rec.Published_Date.strftime('%Y-%m-%d %H:%M')
     newsDictList.append(newsDict)
    return newsDictList

def getSimilarTopNVideo(lang):
    #Send Notifications
    if lang.lower() == ENGLISH.lower():
        categoryDict = TopN_English_Video.objects.filter()

    if lang.lower() == MARATHI.lower():
        categoryDict = TopN_Marathi_Video.objects.filter()

    if lang.lower() == HINDI.lower():
        categoryDict = TopN_Hindi_Video.objects.filter()

    return parseDateTimeToStringTopNVideo(categoryDict)

def parseDateTimeToStringTopNVideo(dictList):
    thumbStr='Thumbnail'
    videoIDStr='VideoId'
    videoTableIDStr='VideoTableId'
    titleStr='Title'
    urlStr='URL'
    summStr='Summary'
    #clusterStr='Cluster_Id'
    sourceStr='Source_id'
    idStr='id'
    pubDateStr='Published_Date'
    newsDictList=[]
    for rec in dictList:
        newsDict={}
        newsDict[idStr]=rec.id
        newsDict[videoTableIDStr] = rec.Video_id
        newsDict[videoIDStr]=rec.VideoId
        newsDict[urlStr]=rec.URL
        newsDict[titleStr]=rec.Title
        newsDict[summStr]=rec.Summary
        newsDict[thumbStr]=rec.Thumbnail
        newsDict[sourceStr]=rec.Source_id
        newsDict[pubDateStr]=rec.Published_Date.strftime('%Y-%m-%d %H:%M')
        newsDictList.append(newsDict)
    return newsDictList

def convertMobileSite(URL,Source_id):
    mobileURL = URL
    if URL[7:10]=='www':
        mobileURL = 'http://m.' + URL[11:]
    elif Source_id == 30:
        mobileURL = 'http://m.maharashtratimes.com' + URL[38:]
    elif Source_id == 153:
        if URL[7:17] == 'mp.patrika' or URL[7:17] == 'up.patrika':
            return URL
    else:
        mobileURL = 'http://m.' + URL[7:]
    return mobileURL


def checkForMobileURL(URL,Source_id):
    for mobileURLId in sourceIdForMobileURL:
        if mobileURLId == Source_id:
            URL = convertMobileSite(URL,Source_id)


    for transcodeId in transcode:
        if transcodeId == Source_id:
            URL = GOOGLEWEBLIGHT + URL
            if Source_id == 39:
                URL = URL.encode("utf-8")
    return URL


