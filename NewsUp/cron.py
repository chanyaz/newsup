from newsApp.Utils import *
from newsApp.youtube import *
from newsApp.userConstants import *
import logging

logger = logging.getLogger('django_crontab')

def my_scheduled_job_daily():
    
    try:
        clusterOnLanguageCategory(MARATHI,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,MAHARASHTRA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,ENTERTAINMENT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,ENTERTAINMENT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,SPORTS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(MARATHI,SPORTS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,OPINION,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(MARATHI,WORLD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,MUMBAI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,PUNE,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,NAGPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,NASIK,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,AURANGABAD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,SOLAPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,KOLHAPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,SATARA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,SANGLI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,AKOLA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,AHMEDNAGAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,JALGAON,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,GOA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,CHANDRAPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,WARDHA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,POLITICS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,WORLD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)    
    try:
        clusterOnLanguageCategory(ENGLISH,ECONOMY,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,HEALTH,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,LIFESTYLE,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,TECHNOLOGY,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,ENVIRONMENT,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,TRAVEL,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,SCIENCE,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,BUSINESS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,STOCKS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(ENGLISH,FOOD,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,FASHION,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    
    try:
        insertWithoutClustering(MARATHI,HEALTH,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,LIFESTYLE,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,BUSINESS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(ENGLISH,OPINION,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(ENGLISH,MUMBAI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(ENGLISH,PUNE,DELTA_DAYS_ONE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        socialIndicators(ENGLISH,TOP_STORIES)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        socialIndicators(MARATHI,TOP_STORIES)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        socialIndicators(HINDI,TOP_STORIES)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)


def my_schedule_job_video_daily():
    try:
        getVideoForLanguageCategory(ENGLISH,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(MARATHI,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(HINDI,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(MARATHI,ENTERTAINMENT,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,ENTERTAINMENT,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,SPORTS,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,WORLD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,BUSINESS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,LIFESTYLE,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,HEALTH,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,FASHION,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,TECHNOLOGY,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,ENVIRONMENT,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,SCIENCE,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,FOOD,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(HINDI,ENTERTAINMENT,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(HINDI,BUSINESS,DELTA_HOURS_THREE_SIXTY)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

def my_scheduled_job_hourly():
    try:
        clusterWithNewDocument(ENGLISH,STOCKS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,BUSINESS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,ENTERTAINMENT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,ENTERTAINMENT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,MAHARASHTRA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(MARATHI,SPORTS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(MARATHI,WORLD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,POLITICS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,WORLD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,ECONOMY,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,SPORTS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(ENGLISH,OPINION,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,OPINION,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,HEALTH,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,LIFESTYLE,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,TECHNOLOGY,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,ENVIRONMENT,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,TRAVEL,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,SCIENCE,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(ENGLISH,FOOD,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterWithNewDocument(ENGLISH,FASHION,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,HEALTH,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,LIFESTYLE,DELTA_HOURS_FOURTY_EIGHT)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,BUSINESS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(ENGLISH,MUMBAI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(ENGLISH,PUNE,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,MUMBAI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,PUNE,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,NAGPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,NASIK,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,AURANGABAD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(MARATHI,SOLAPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,KOLHAPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,SATARA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,SANGLI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,AKOLA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,AHMEDNAGAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,JALGAON,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,GOA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,CHANDRAPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        insertWithoutClustering(MARATHI,WARDHA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

def my_scheduled_job_TopN():
    try:
        createTopN(MARATHI)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        createTopN(ENGLISH)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        createTopN(HINDI)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

def my_scheduled_job_delete_TopN():
    try:
        deleteLangCategoryTable(ENGLISH, TOPN)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        deleteLangCategoryTable(MARATHI, TOPN)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

def my_scheduled_job_delete_article():
    try:
        deleteArticleTable(DELTA_DAYS_SEVEN)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

def my_scheduled_job_Top_News():

    try:
        clusterOnLanguageCategory(MARATHI,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        sortForRep(MARATHI,TOP_STORIES)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(ENGLISH,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        sortForRep(ENGLISH,TOP_STORIES)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(HINDI,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(ENGLISH,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(MARATHI,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        getVideoForLanguageCategory(HINDI,TOP_STORIES,DELTA_HOURS_TWELVE)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        socialIndicators(ENGLISH,TOP_STORIES)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        socialIndicators(MARATHI,TOP_STORIES)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

    try:
        socialIndicators(HINDI,TOP_STORIES)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

def my_scheduled_job_Hindi():

    try:
        clusterOnLanguageCategory(HINDI,SPORTS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(HINDI,WORLD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,OPINION,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,HEALTH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,LIFESTYLE,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ENTERTAINMENT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,TECHNOLOGY,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,AUTO,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,POLITICS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,TRAVEL,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SCIENCE,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BUSINESS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        clusterOnLanguageCategory(HINDI,FASHION,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,CRIME,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,UTTARPRADESH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,UTTARAKHAND,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,HIMACHALPRADESH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,DELHI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JAMMUKASHMIR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,PUNJAB,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MADHYAPRADESH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JHARKHAND,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BIHAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,HARYANA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,CHATTISGARH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,RAJASTHAN,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,WESTBENGAL,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ORISSA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,GUJRAT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MAHARASHTRA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,LUCKNOW,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ALLAHABAD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,PRATAPGARH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,KANPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MERATH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,AGRA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,NOIDA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,GAZIABAD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BAGPAT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SAHARNPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BULANDSHAHAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,VARANASI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,GORAKHPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JHANSI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MUZAFFARNAGAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SITAPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JAUNPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,AZAMGARH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MORADABAD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BAREILLY,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BALIA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ALIGARH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MATHURA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BHOPAL,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,INDORE,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,GWALIOR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JABALPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,UJJAIN,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,RATLAM,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SAGAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,DEWAS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SATNA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,REWA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,PATNA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BHAGALPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MUJAFFARPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,GAYA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,DARBHANGA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,POORNIYA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SEWAN,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BEGUSARAI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,KATIHAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JAIPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,UDAIPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JODHPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,AJMER,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BIKANER,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ALWAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SIKAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,KOTA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BHILWARA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BHARATPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,CHHATIS,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,RAIPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BHILAI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,RAJNANDGAO,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,RAIGARH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JAGDALPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,KORVA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,RANCHI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,DHANBAD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JAMSHEDPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,GIRIDIHI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,HAZARIBAGH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BOKARO,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,DEHRADUN,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,NAINITAAL,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,HARIDWAAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ALMORAH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,UDDHAMSINGHNAGAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SIMLA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MANDI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BILASPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,AMRITSAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JALANDHAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,LUDHIANA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ROPARH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,CHANDIGARH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ROHTAK,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,PANCHKULA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,AMBALA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,PANIPAT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,GURGAON,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,HISSAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JAMMU,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SRINAGAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,POONCH,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,KOLKATA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,JALPAIGURHI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,DARJEELING,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,ASANSOL,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SILIGURHI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,BHUVANESHWAR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,PURI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,CUTTACK,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,AHMEDABAD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,SURAT,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,VADODARA,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,MUMBAI,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,NAGPUR,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,PUNE,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)
    try:
        insertWithoutClustering(HINDI,FARIDABAD,DELTA_HOURS_TWENTY_FOUR)
    except Exception, e:
        logger.exception("You have an exception :%s",e.args)

