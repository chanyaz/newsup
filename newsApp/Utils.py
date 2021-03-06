# -*- coding: utf-8 -*-

from collections import defaultdict
from HTMLParser import HTMLParser
import codecs
import os
import feedparser
from dateutil import parser
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from gensim import corpora,similarities
import gensim
from scipy import cluster
import requests
from scrapeImage import *
from tableQuery import *
from scrapeComment import *

logger = logging.getLogger('django')


def getFeeds(lang, category):
    logger.info("Entered getFeeds ")
    feedsList = []
    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=category)
    feedsObj = News_Feed.objects.filter(Language=langObj, Category=categoryObj)

    for i in feedsObj:
        feedsDict = {}
        feedsDict['URL'] = i.URL
        feedsDict['Source'] = i.Source_id
        feedsDict['Type'] = i.Type
        feedsList.append(feedsDict)

    logger.info("Exited getFeeds ")
    return feedsList

def getRSS2FeedParserData(lang, category, feedsDict):
    #logger.info("Entered getRSS2FeedParserData ")
    feed = feedparser.parse(feedsDict['URL'])
    #if sys.stdout.encoding != 'cp850':
    #    sys.stdout = codecs.getwriter('cp850')(sys.stdout, 'xmlcharrefreplace')
    #if sys.stderr.encoding != 'cp850':
    #    sys.stderr = codecs.getwriter('cp850')(sys.stderr, 'xmlcharrefreplace')

    newsDictList = []
    inc = 0
    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=category)
    for post in feed.entries:
        newsDict = {}
        newsDict['Language_id'] = langObj
        newsDict['Category_id'] = categoryObj
        newsDict['smallImage'] = ""
        newsDict['title'] = ""
        newsDict['summary'] = ""
        newsDict['link'] = ""
        newsDict['published'] = ""
        newsDict['Source_id'] = feedsDict['Source']

        if 'media_content' in post.keys():
            dc_thumbnailDictList = post['media_content']
            dc_thumbnailDict = dc_thumbnailDictList[0]
            if 'url' in dc_thumbnailDict.keys():
                newsDict['smallImage'] = dc_thumbnailDict['url']

        elif 'media_thumbnail' in post.keys():
            dc_thumbnailDictList = post['media_thumbnail']
            dc_thumbnailDict = dc_thumbnailDictList[0]
            if 'url' in dc_thumbnailDict.keys():
                newsDict['smallImage'] = dc_thumbnailDict['url']

        elif 'postimage' in post.keys():
            dc_thumbnailDict = post['postimage']
            newsDict['smallImage'] = dc_thumbnailDict

        elif 'dc_thumbnail' in post.keys():
            dc_thumbnailDict = post['dc_thumbnail']
            if 'url' in dc_thumbnailDict.keys():
                newsDict['smallImage'] = dc_thumbnailDict['url']


        if not newsDict['smallImage']:
            # this means that we have come across a news feed which doesn't have small image
            # now either 1. the news feed doesn't provide image at all OR
            # the image is in summary field. So to explore the second possibility, pass on the summary to the function
            #if post.summary:
            if 'summary' in post.keys():
                summDict = returnImageURL(post.summary)
                if summDict['imageURLList']:
                    newsDict['smallImage'] = summDict['imageURLList'][0]

        if 'title' in post.keys():
            newsDict['title'] = post.title

        if 'summary' in post.keys():
            # we need to take sumary directly from the feed only when 1. there is no existing summary already present
            if not newsDict['summary']:
                summDict = returnData(post.summary)
                if summDict['summaryData']:
                    sumFinal = " ".join(summDict['summaryData'])
                    if len(sumFinal) > 295:
                         sumFinal = sumFinal[0:295].rsplit(' ', 1)[0]
                    else:
                        sumFinal = sumFinal.rsplit(' ', 1)[0]
                    summaryFinal = trailingDots(sumFinal)
                    newsDict['summary'] = summaryFinal

        if 'link' in post.keys():
            newsDict['link'] = post.link

        if 'published' in post.keys():
            if post.published:
                newsDict['published'] = post.published

        newsDictList.insert(inc, newsDict)
        inc += 1
    #logger.info("Exited getRSS2FeedParserData ")
    return newsDictList

def getAPI2ParserData(lang,category,feedsDict):
    newsList=[]
    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=category)
    r = requests.get(feedsDict['URL'])
    try:
        wjson = r.json()

        for dict in wjson['results']:
            newsDict={}
            newsDict['Language_id'] = langObj
            newsDict['Category_id'] = categoryObj
            newsDict['link'] = dict['link']
            newsDict['title'] = dict['title/_text']
            newsDict['smallImage'] = ""
            newsDict['summary'] = ""
            newsDict['published'] = ""
            newsDict['Source_id'] = feedsDict['Source']
            if 'summary' in dict.keys():
                sumFinal = dict['summary']
                if len(sumFinal) > 295:
                    sumFinal = sumFinal[0:295].rsplit(' ', 1)[0]
                else:
                    sumFinal = sumFinal.rsplit(' ', 1)[0]
                newsDict['summary'] = trailingDots(sumFinal)
            else:
                newsDict['summary'] = ''
            newsList.append(newsDict)
    except:
        pass
    return newsList

def insertNewsArticle(newsDictList,deltaHours,isNew):
    #logger.info("Entered insertNewsArticle ")
    #deltaDate = datetime.date.today() - datetime.timedelta(days=deltaDays)
    #deltaDate = timezone.localtime(timezone.now()).date() - datetime.timedelta(days=deltaDays)
    deltaDate = datetime.datetime.now() - datetime.timedelta(hours=deltaHours)


    newsArticleObj = News_Article.objects.all()
    for newsDict in newsDictList:
        sourceObj = News_Source.objects.get(id=newsDict['Source_id'])
        if newsDict['published']:
            dt = parser.parse(newsDict['published'])
        else:
            #date = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%a, %d. %B %Y %H:%M:%S")
            #date = timezone.datetime.today().strftime("%a, %d. %B %Y %H:%M:%S")
            date = datetime.datetime.today().strftime("%a, %d. %B %Y %H:%M:%S")
            dt = parser.parse(date)
            logger.info(newsDict['link'])
            logger.info(dt)
        dtNaive = dt.replace(tzinfo=None)

        if dtNaive >= deltaDate:
            found = 0
            for item in newsArticleObj:
                if item.URL.lower() == newsDict['link'].lower():
                    found = 1
            if newsDict['Source_id'] == 30:
                if newsDict['link'][0:24] == MAHARASHTRA_TIMES_AD:
                    found = 1
            if not found:
                if newsDict['Source_id'] == 3:
                    newsDict['smallImage'] = scrapeArticleForImage(newsDict['link'],newsDict['Source_id'])

                if newsDict['Source_id'] == 28:
                    if newsDict['summary'].partition(' ')[0] == IBN_PLUS:
                        newsDict['summary'] = ''

                if not newsDict['smallImage']:
                    newsDict['smallImage'] = scrapeArticleForImage(newsDict['link'],newsDict['Source_id'])

                if newsDict['smallImage']:
                    isUrl = isUrlanImage(newsDict['smallImage'])
                    if not isUrl:
                        newsDict['smallImage'] = ''

                article = News_Article(Language=newsDict['Language_id'],
                                       Category=newsDict['Category_id'],
                                       URL=newsDict['link'],
                                       Title=newsDict['title'],
                                       Summary=newsDict['summary'],
                                       Thumbnail=newsDict['smallImage'],
                                       Source=sourceObj,
                                       Published_Date=dt,
                                       Is_New=isNew)
                article.save()
    #logger.info("Exited insertNewsArticle ")

def bagOfWords(lang, category, isNew,deltaHours):
    logger.info("Entered bagOfWords ")
    corpusList = []
    titles = []

    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=category)
    #deltaDate = datetime.date.today() - datetime.timedelta(days=deltaDays)
    #deltaDate = timezone.localtime(timezone.now()).date() - datetime.timedelta(days=deltaDays)
    deltaDate = datetime.datetime.now() - datetime.timedelta(hours=deltaHours)

    articleObj = News_Article.objects.filter(Language=langObj,
                                             Category=categoryObj,
                                             Is_New=isNew,
                                             Published_Date__gt=deltaDate).order_by('-Published_Date')
    for article in articleObj:
        soup = article.Title
        if lang.lower() == MARATHI.lower():
            soup = translateTitle(soup, GOOGLE_MR, GOOGLE_EN)
        elif lang.lower() == HINDI.lower():
            soup = translateTitle(soup, GOOGLE_HI, GOOGLE_EN)
        letters_only = re.sub("[^a-zA-Z]",  # The pattern to search for
                              " ",  # The pattern to replace it with
                              soup)  # Source
        lower_case = letters_only.lower()

        wordList2 = lower_case.split()

        st = LancasterStemmer()
        wordList3 = [st.stem(w) for w in wordList2]

        stops = set(stopwords.words("english"))
        finalWordlist = [w for w in wordList3 if not w in stops]

        corpusList.append(finalWordlist)
        string = str(article.id) + ' ' + str(letters_only)
        titles.append(string)
    resultDict = {}
    resultDict['corpusList'] = corpusList
    resultDict['titles'] = titles
    logger.info("Exited bagOfWords ")
    return resultDict

def convertCorpustoDict(corpusList, path_dict, path_dict_mm):
    logger.info("Entered convertCorpustoDict ")
    frequency = defaultdict(int)  # remove words that appear only once
    for text in corpusList:
        for token in text:
            frequency[token] += 1

    corpus = [[token for token in text if frequency[token] > 1]
              for text in corpusList]

    dictionary = corpora.Dictionary(corpus)

    dictionary.save(path_dict)  # store the dictionary, for future reference


    corpus = [dictionary.doc2bow(text) for text in corpus]  #convert tokenized documents to vectors
    corpora.MmCorpus.serialize(path_dict_mm, corpus)  # store to disk, for later use
    logger.info("Exited convertCorpustoDict ")

def transformationsTFIDF(corpus):
    logger.info("Entered transformationsTFIDF ")
    # training the corpus
    #training consists simply of going through the
    tfidf = gensim.models.TfidfModel(corpus)  # supplied corpus once and computing document
    # frequencies of all its features
    corpus_tfidf = tfidf[corpus]  # apply a transformation to a whole corpus
    logger.info("Exited transformationsTFIDF ")
    return corpus_tfidf

def transformationsLSI(corpus_tfidf, dictionary):
    logger.info("Entered transformationsLSI ")
    lsi = gensim.models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=50)  # initialize an LSI transformation
    corpus_lsi = lsi[corpus_tfidf]  # both bow->tfidf and tfidf->lsi transformations
    logger.info("Exited transformationsLSI ")
    return corpus_lsi

def similarityMatrx(corpus_lsi):
    logger.info("Entered similarityMatrx ")
    index = similarities.MatrixSimilarity(corpus_lsi)
    logger.info("Exited similarityMatrx ")
    return index

def extract_clusters(Z, threshold, n):
    logger.info("Entered extract_clusters ")
    clusters = {}
    ct = n
    for row in Z:
        if row[2] < threshold:
            n1 = int(row[0])
            n2 = int(row[1])

            if n1 >= n:
                l1 = clusters[n1]
                del (clusters[n1])
            else:
                l1 = [n1]

            if n2 >= n:
                l2 = clusters[n2]
                del (clusters[n2])
            else:
                l2 = [n2]
            l1.extend(l2)
            clusters[ct] = l1
            ct += 1

        else:
            logger.info("Exited extract_clusters ")
            return clusters

def insertCategory(lang, category, cluster_file, outlier_file):
    logger.info("Entered insertCategory ")
    maxDict = getMaxClusterId(lang, category)
    if maxDict['Cluster_Id__max']:
        maxClusterId = maxDict['Cluster_Id__max'] + 1
    else:
        maxClusterId = 1

    deleteLangCategoryTable(lang, category)
    try:
        f = open(cluster_file, 'r')
        clusterIdPrev = -1
        for line in f:
            clusterId = int(line.split()[0])
            key1 = line.split()[1]
            articleObj = News_Article.objects.get(id=int(key1))
            if clusterIdPrev == -1:  # For the first line of the file
                insertLangCategoryTable(int(key1), lang, category, articleObj, maxClusterId, isRep=1)
            else:
                if clusterId == clusterIdPrev:  # When articles of same Cluster
                    insertLangCategoryTable(int(key1), lang, category, articleObj, maxClusterId, isRep=0)
                else:
                    maxClusterId += 1  # When articles of different Cluster
                    insertLangCategoryTable(int(key1), lang, category, articleObj, maxClusterId, isRep=1)
            clusterIdPrev = clusterId
        f.close()
        maxDict = getMaxClusterId(lang, category)
        if maxDict['Cluster_Id__max']:
            maxClusterId = maxDict['Cluster_Id__max'] + 1
        else:
            maxClusterId = 1
    except Exception,e:
        logger.error("You have an exception :",e.args)
    try:
        f2 = open(outlier_file, 'r')
        for line in f2:
            key1 = line.split()[1]
            articleObj = News_Article.objects.get(id=int(key1))
            insertLangCategoryTable(int(key1), lang, category, articleObj, maxClusterId, isRep=True)
            maxClusterId += 1
        f2.close()
    except Exception,e:
        logger.error("You have an exception :",e.args)
    logger.info("Exited insertCategory ")


def returnImageURL(tag):
    # create a subclass and override the handler methods
    summDict = {}
    summDict['imageURLList'] = []

    class MyHTMLParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.dataList = []
            self.imgURLList = []

        def handle_starttag(self, tag, attrs):
            if tag == 'img':
                # some NYT articles contain ads in form of images so check them via
                # RE and filter them
                for name, value in attrs:
                    if name == "src":
                        if value:
                            pattern1 = ".feedsportal.com"
                            pattern2 = '[^ ].*?(gif)'
                            pattern3 = 'big.assets.huffingtonpost.com'

                            matchObj2 = re.search(pattern1, value, re.I)
                            # skip this image as it is an ad image from NYT
                            if not matchObj2:
                                # check for p2
                                matchObj2 = re.search(pattern2, value, re.I)
                                if not matchObj2:
                                    matchObj2 = re.search(pattern3, value, re.I)
                                    if not matchObj2:
                                        # this means that the current image is OK to proceed as it does not match the above 3 patterns
                                        self.imgURLList.append(value)

        def handle_endtag(self, tag):
            if tag == 'img':
                summDict['imageURLList'] = self.imgURLList

        def handle_data(self, data):
            pass


            # instantiate the parser and feed it the summary

    parser = MyHTMLParser()
    parser.feed(tag)
    return summDict

def returnData(tag):
    # create a subclass and override the handler methods
    summDict = {}
    summDict['summaryData'] = []

    class MyHTMLParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.dataList = []
            self.imgURLList = []

        def handle_starttag(self, tag, attrs):
            pass

        def handle_endtag(self, tag):
            pass

        def handle_data(self, data):
            self.dataList.append(data)
            summDict['summaryData'] = self.dataList


            # instantiate the parser and feed it the summary

    parser = MyHTMLParser()
    parser.feed(tag)
    return summDict

def isInClusteredIdsList(i, clusteredIdsList):
    #logger.info("Entered isInClusteredIdsList ")
    if i in clusteredIdsList:
        #logger.info("Exited isInClusteredIdsList ")
        return 1
    else:
        #logger.info("Exited isInClusteredIdsList ")
        return 0

def getTitlesFromTables(clusterLanguage):  # Hit tables of all categories and get all Titles
    #logger.info("Entered getTitlesFromTables ")
    titlesList = []
    langObj = Language.objects.get(Name=clusterLanguage)

    #deltaDate = datetime.date.today() - datetime.timedelta(days=1)
    deltaDate = timezone.localtime(timezone.now()).date() - datetime.timedelta(days=1)
    articleObj = News_Article.objects.filter(Language = langObj,
                                             Published_Date__gt=deltaDate).order_by('id')
    for article in articleObj:
        titlesDict = {}
        titlesDict['Article'] = article
        titlesDict['title'] = article.Title
        titlesDict['id'] = article.id
        titlesDict['URL'] = article.URL
        titlesDict['Source'] = article.Source
        titlesDict['Summary'] = article.Summary
        titlesDict['Thumbnail'] = article.Thumbnail
        titlesDict['Published_Date'] = article.Published_Date
        titlesList.append(titlesDict)
    #logger.info("Exited getTitlesFromTables ")
    return titlesList

def preProcessTitles(titlesList):
    #logger.info("Entered preProcessTitles ")
    corpusList = []
    for titleDict in titlesList:
        soup = titleDict['title']

        letters_only = re.sub("[^a-zA-Z]",  # The pattern to search for
                              " ",  # The pattern to replace it with
                              soup)  # Source
        lower_case = letters_only.lower()

        wordList2 = lower_case.split()

        st = LancasterStemmer()
        wordList3 = [st.stem(w) for w in wordList2]

        stops = set(stopwords.words("english"))
        finalWordlist = [w for w in wordList3 if not w in stops]

        corpusList.append(finalWordlist)
    #logger.info("Exited preProcessTitles ")
    return corpusList

def insertTopNewsArticle(newsDictList):
    logger.info("Entered insertTopNewsArticle ")
    deltaDate = datetime.date.today() - datetime.timedelta(days=1)
    #deltaDate = timezone.localtime(timezone.now()).date() - datetime.timedelta(days=1)
    newsArticleObj = TopN_News_Article.objects.all()
    for newsDict in newsDictList:
        sourceObj = News_Source.objects.get(id=newsDict['Source_id'])
        if newsDict['published']:
            dt = parser.parse(newsDict['published'])
        else:
            date = datetime.datetime.today().strftime("%a, %d. %B %Y %H:%M:%S")
            #date = timezone.datetime.today().strftime("%a, %d. %B %Y %H:%M:%S")
            dt = parser.parse(date)
        if dt.date() > deltaDate:
            found = 0
            for item in newsArticleObj:
                if item.URL == newsDict['link']:
                    found = 1
            if not found:
                article = TopN_News_Article(Language=newsDict['Language_id'],
                                            Category=newsDict['Category_id'],
                                            URL=newsDict['link'],
                                            Title=newsDict['title'],
                                            Summary=newsDict['summary'],
                                            Thumbnail=newsDict['smallImage'],
                                            Source=sourceObj,
                                            Published_Date=dt)
                article.save()
    logger.info("Exited insertTopNewsArticle ")

def convertCorpustoDict4NewDoc(corpusList, path_dict, path_dict_mm):
    #logger.info("Entered convertCorpustoDict4NewDoc ")
    frequency = defaultdict(int)  # remove words that appear only once
    for text in corpusList:
        for token in text:
            frequency[token] += 1

    corpus = [[token for token in text]  # if frequency[token] > 1]
              for text in corpusList]
    oldDictionary = corpora.Dictionary.load(path_dict)
    oldDictionary.add_documents(corpus)

    corpus = [oldDictionary.doc2bow(text) for text in corpus]  # convert tokenized documents to vectors
    oldCorpus = corpora.MmCorpus(path_dict_mm)

    oldCorpus = list(oldCorpus)

    for text in corpus:
        oldCorpus.append(text)

    corpora.MmCorpus.serialize(path_dict_mm, oldCorpus)  # store to disk, for later use

    oldDictionary.save(path_dict)  # store the dictionary, for future reference
    #logger.info("Exited convertCorpustoDict4NewDoc ")

def translateTitle(query, srcLang, dstLang):
    #logger.info("Entered translateTitle ")
    if srcLang == GOOGLE_MR:
        sanitisedquery = returnSanitisedTitleString(WORDLIST_MARATHI, query)
        sanitisedquery = returnSanitisedTtileString1(sanitisedquery)
        sanitisedquery = returnSlicedTitle(sanitisedquery)
    if srcLang == GOOGLE_HI:
        sanitisedquery = query
    sanitisedquery = re.sub(r'[?|$|.|!@|#|%|^|&|*|_]', r'', sanitisedquery)
    r = requests.get(
        'https://www.googleapis.com/language/translate/v2?key=AIzaSyAs7K0Axc1YuAWz8ltKh6nmY0C1-fDf2M4&source='
        + srcLang + '&target=' + dstLang + '&q=' + sanitisedquery)
    wjson = r.json()
    #logger.info("Exited translateTitle ")
    return wjson['data']['translations'][0]['translatedText']

def returnSanitisedTitleString(fileName, title):
    sanitisedtitleList = []
    whiteSpace = " "
    titleList = title.split()
    for word in titleList:
        sanitisedWord = returnMarathiRootWord(fileName, word)
        sanitisedtitleList.append(sanitisedWord)
    return whiteSpace.join(sanitisedtitleList)

def returnSanitisedTtileString1(title):
    titleList = title.split()
    newTitleList = []
    whiteSpace = " "
    for titleWord in titleList:
        newTitleWord = returnSanitisedTitleWord(titleWord)
        newTitleList.append(newTitleWord)
    return whiteSpace.join(newTitleList)

def returnSanitisedTitleWord(titleWord):
    word = {}

    word['2'] = "प्रमाणेच"
    word['4'] = "मुळे"
    word['8'] = "प्रमाणे"
    word['12'] = "मध्येही"
    word['13'] = "मध्ये"
    word['14'] = "सुद्धा"

    for key in word:
        try:
            if word[key] in titleWord:
                sanitisedWord = titleWord.replace(word[key], " ")
                return sanitisedWord
            else:
                sanitisedWord = titleWord
        except:
            sanitisedWord = titleWord
    return sanitisedWord

def returnMarathiRootWord(fileName, token):
    with codecs.open(fileName, 'r', encoding='utf-8') as f:
        for lines in f:
            if token in lines:
                strArray = lines.split('[')
                custStrArr = strArray[1].split('-')

                if (custStrArr[0]):
                    return custStrArr[0]

                if not (custStrArr[0]):
                    # check p3
                    strArray = lines.split('{')
                    custStrArr = strArray[1].split('|')
                    return custStrArr[0]
            return token

def returnSlicedTitle(title):
    #logger.info("Entered returnSlicedTitle ")
    newWordList = []
    for word in title.split():
        slicedWord = returnSlicedWord(word)
        if slicedWord:
            newWordList.append(slicedWord)
        else:
            newWordList.append(word)
    #logger.info("Exited returnSlicedTitle ")
    return " ".join(newWordList)

def returnSlicedWord(word):
    #logger.info("Entered returnSlicedWord ")
    sliceWord = {}
    sliceWord['1'] = "प्रकरणी"
    sliceWord['2'] = "विरुद्ध"
    sliceWord['3'] = "कडे"
    sliceWord['4'] = "वर"
    sliceWord['5'] = "कडून"
    sliceWord['6'] = "करिता"
    sliceWord['7'] = "वरून"
    sliceWord['8'] = "खालुन"
    sliceWord['9'] = "खालून"
    sliceWord['10'] = "साठी"
    sliceWord['11'] = "देखील"
    sliceWord['12'] = "सह"
    sliceWord['13'] = "हुन"
    sliceWord['14'] = "हून"
    sliceWord['15'] = "जवळ"
    sliceWord['16'] = "चे"
    sliceWord['17'] = "च्या"
    sliceWord['18'] = "ची"
    sliceWord['19'] = "तील"
    sliceWord['20'] = "मागे"
    sliceWord['21'] = "पुढे"
    sliceWord['22'] = "चा"
    sliceWord['23'] = "मुक्त"
    sliceWord['24'] = "टंचाई"
    sliceWord['25'] = "मधील"
    sliceWord['26'] = "वाद"
    sliceWord['27'] = "प्रकरणा"
    sliceWord['28'] = "भेद"
    sliceWord['29'] = "विरोधात"
    sliceWord['30'] = "द्वारे"
    sliceWord['31'] = "युक्त"
    sliceWord['32'] = "बरोबर"
    sliceWord['33'] = "ही"
    sliceWord['34'] = "पर्यंत"
    sliceWord['35'] = "खाली"
    sliceWord['36'] = "ऐवजी"
    sliceWord['37'] = "पूर्ती"

    slicedWordList = []
    try:
        for key in sliceWord:
            if sliceWord[key] in word:
                newSlicedWord = " " + sliceWord[key]
                sanitisedWord = word.replace(sliceWord[key], newSlicedWord)
                slicedWordList.append(sanitisedWord)

                break
    except:
        return " ".join(slicedWordList)
    #logger.info("Exited returnSlicedWord ")
    return " ".join(slicedWordList)

def trailingDots(string):
    try :
        string = string.rstrip()
        lastword = string.rsplit(' ', 1)[1]
        if lastword.endswith('...'):
            lastword =  lastword[:-3]
        elif lastword.endswith('..'):
            lastword = lastword[:-2]
        elif lastword.endswith('.'):
            lastword =  lastword[:-1]
        summary = string.rsplit(' ', 1)[0] +' ' + lastword + "..."
        return summary
    except:
        logger.info("Exited trailingDots ")
        return string


def findMaxListIndex(list):
    #logger.info("Entered findMaxListIndex ")
    count = 0
    for item in list:
        if item == max(list):
            #logger.info("Exited findMaxListIndex ")
            return count
        else :
            count +=1
    #logger.info("Exited findMaxListIndex ")
    return -1

def insertTopNLanguage(language,articleDict):
    #logger.info("Entered insertTopNLanguage ")
    if language == ENGLISH:
        langTopNObj = TopN_English(Article=articleDict['Article'],
                                  URL=articleDict['URL'],
                                  Title=articleDict['title'],
                                  Summary=articleDict['Summary'],
                                  Thumbnail=articleDict['Thumbnail'],
                                  Source=articleDict['Source'],
                                  Published_Date=articleDict['Published_Date'])
        langTopNObj.save()
    if language == MARATHI:
        langTopNObj = TopN_Marathi(Article=articleDict['Article'],
                                  URL=articleDict['URL'],
                                  Title=articleDict['title'],
                                  Summary=articleDict['Summary'],
                                  Thumbnail=articleDict['Thumbnail'],
                                  Source=articleDict['Source'],
                                  Published_Date=articleDict['Published_Date'])
        langTopNObj.save()
    #logger.info("Exited insertTopNLanguage ")

def deleteFiles(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            logger.error("You have an exception :",e.args)

def clusterOnLanguageCategory(clusterLanguage,clusterCategory,deltaHours):

#This function does the following
#1) Deletes the following files a)Cluster File b) Outlier File c)Titles-Dictionary File d)Titles dictionary MM serialized File e)All Titles file
#2) Gets the feeds for respective language and categories
#3) Parses those feeds to get the required data of the articles in the feeds like the titles, summary, photos etc
#4) Inserts them into article table
#5) Retrieves all the articles for article table and creates bag of words, Also writes the titles in All Titles file
#6) If total number of articles are less than 5 all are considered outliers and written in the Outlier files
#7) If the total number of articles are more than 5 than Take the bag og words convert them in to corpus of words with freq more than 1
#8) Write this corpus into titles dictionary file
#9) Convert and write the Dictionary into MM serialized dictionary
#10)load the corpus from MM serialized dictionary
#11)transform the corpus into TFIDF corpus
#12)transform the corpus into LSI corpus
#13)extract clusters from this LSI corpus
#14) insert these clusters into lang category table

    logger.info("Entered clusterOnLanguageCategory ")
    logger.info("%s,%s" %(clusterLanguage,clusterCategory))

    langCatFilesPath = PATH + "/" + clusterLanguage + "/" + clusterCategory
    cluster_file = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + CLUSTER_FILE
    outlier_file = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + OUTLIER_FILE
    path_dict = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + TITLES_DICT
    path_dict_mm = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + TITLES_DICT_MM
    titles_all = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + TITLES_ALL

    deleteFiles(langCatFilesPath)

    isNew = 0
    feedsList = getFeeds(clusterLanguage,clusterCategory)
    for feedsDict in feedsList:
        if str(feedsDict['Type']) == 'RSS 2.0':
            newsDictList = getRSS2FeedParserData(clusterLanguage,clusterCategory,feedsDict)
        else:
            newsDictList = getAPI2ParserData(clusterLanguage,clusterCategory,feedsDict)
        insertNewsArticle(newsDictList,deltaHours,isNew)

    resultDict = bagOfWords(clusterLanguage,clusterCategory,isNew,deltaHours)
    corpusList = resultDict['corpusList']
    titles = resultDict['titles']

    f = open(titles_all, 'w')
    cnt = -1
    for item in titles:
        cnt += 1
        string = str(cnt) + " " + item + "\n"
        f.write(string)
    f.close()

    if cnt == -1:
        logger.info("Total articles : %s" % (cnt + 1))
    elif cnt >- 1 and cnt<5:
        i=0
        countOutliers = 0
        f2 = open(outlier_file, 'w')
        while i <= cnt:
            string =  str(i) + ' ' + str(titles[i]) + '\n'
            f2.write(string)
            countOutliers+=1
            i+=1
        f2.close()
        logger.info("Total Outlier articles : %s" % countOutliers)
        insertArchive(clusterLanguage,clusterCategory)
        insertCategory(clusterLanguage,clusterCategory,cluster_file,outlier_file)
    else:
        logger.info("Total Outlier articles : %s" % (cnt + 1))
        convertCorpustoDict(corpusList,path_dict,path_dict_mm)

        dictionary = corpora.Dictionary.load(path_dict)
        corpus = corpora.MmCorpus(path_dict_mm)

        corpus_tfidf=transformationsTFIDF(corpus)
        corpus_lsi = transformationsLSI(corpus_tfidf,dictionary)

        index=similarityMatrx(corpus_lsi)

        mat = []
        for doc in index:
            list = []
            for d in doc:
                list.append(d)
            mat.append(list)
        t = 1.2
        n = len(mat[0])

        Z = cluster.hierarchy.linkage(mat, 'single')
        clusters = extract_clusters(Z,t,n)
        clusteredIdsList = []


        f = open(cluster_file, 'w')
        count = 0
        for key in clusters:
            for id in clusters[key]:
                string =  str(key) + ' ' + str(titles[id]) + '\n'
                f.write(string)
                count +=1
                clusteredIdsList.append(id)
        f.close()
        logger.info("Total clustered articles : %s" % count)
        i=0
        countOutliers = 0
        f2 = open(outlier_file, 'w')
        while i < len(titles):
            result = isInClusteredIdsList(i,clusteredIdsList)
            if result == False:
                string =  str(i) + ' ' + str(titles[i]) + '\n'
                f2.write(string)
                countOutliers+=1
            i+=1
        f2.close()
        logger.info("Total Outlier articles : %s" % countOutliers)

        insertArchive(clusterLanguage,clusterCategory)
        insertCategory(clusterLanguage,clusterCategory,cluster_file,outlier_file)
    logger.info("%s,%s" %(clusterLanguage,clusterCategory))
    logger.info("Exited clusterOnLanguageCategory ")

def clusterWithNewDocument(clusterLanguage,clusterCategory,deltaHours):
    logger.info("Entered clusterWithNewDocument ")
    logger.info("%s,%s" %(clusterLanguage,clusterCategory))

    cluster_file = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + CLUSTER_FILE
    outlier_file = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + OUTLIER_FILE
    path_dict = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + TITLES_DICT
    path_dict_mm = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + TITLES_DICT_MM
    titles_all = PATH + "/" + clusterLanguage + "/" + clusterCategory + "/" + TITLES_ALL

    isNew = 1
    feedsList = getFeeds(clusterLanguage,clusterCategory)
    for feedsDict in feedsList:
        if str(feedsDict['Type']) == 'RSS 2.0':
            newsDictList = getRSS2FeedParserData(clusterLanguage,clusterCategory,feedsDict)
        else:
            newsDictList = getAPI2ParserData(clusterLanguage,clusterCategory,feedsDict)
        insertNewsArticle(newsDictList,deltaHours,isNew)
    resultDict = bagOfWords(clusterLanguage,clusterCategory,isNew,deltaHours)
    corpusList = resultDict['corpusList']
    titles = resultDict['titles']
    if titles:
        try:
            f = open(titles_all, 'a')
        except:
            f = open(titles_all, 'w')
        cnt = -1
        for item in titles:
            cnt += 1
            string =  str(cnt) + " " + item + "\n"
            f.write(string)
        f.close()
        logger.info("Total new articles : %s" % (cnt + 1))
        convertCorpustoDict4NewDoc(corpusList,path_dict,path_dict_mm)

        dictionary = corpora.Dictionary.load(path_dict)
        corpus = corpora.MmCorpus(path_dict_mm)

        corpus_tfidf=transformationsTFIDF(corpus)
        corpus_lsi = transformationsLSI(corpus_tfidf,dictionary)

        index=similarityMatrx(corpus_lsi)

        mat = []
        for doc in index:
            list = []
            for d in doc:
                list.append(d)
            mat.append(list)
        t = 1.2
        n = len(mat[0])

        Z = cluster.hierarchy.linkage(mat, 'single')
        clusters = extract_clusters(Z,t,n)
        clusteredIdsList = []

        finalTitle = []

        fTitle = open(titles_all, 'r')
        for line in fTitle:
            finalTitle.append(line.split()[1])
        fTitle.close()

        f = open(cluster_file, 'w')
        count = 0
        for key in clusters:
            for id in clusters[key]:
                string =  str(key) + ' ' + str(finalTitle[id]) + '\n'
                f.write(string)
                count +=1
                clusteredIdsList.append(id)
        f.close()
        logger.info("Total clustered articles : %s" % count)
        i=0
        countOutliers = 0
        f2 = open(outlier_file, 'w')
        while i < len(finalTitle):
            result = isInClusteredIdsList(i,clusteredIdsList)
            if result == 0:
                string =  str(i) + ' ' + str(finalTitle[i]) + '\n'
                f2.write(string)
                countOutliers+=1
            i+=1
        f2.close()
        logger.info("Total Outlier articles : %s" % countOutliers)

        insertCategoryNewDoc(clusterLanguage,clusterCategory,cluster_file,outlier_file)
        deleteLangCategoryTable(clusterLanguage,clusterCategory)
        langCategotyAll = selectRerunTable(clusterLanguage,clusterCategory)
        for articleObj in langCategotyAll:
            insertLangCategoryFromRerunTable(clusterLanguage,clusterCategory,articleObj)
        updateArticleTable(clusterLanguage,clusterCategory)
    logger.info("Exited clusterWithNewDocument ")

def insertWithoutClustering(clusterLanguage,clusterCategory,deltaHours):
    logger.info("Entered insertWithoutClustering ")
    logger.info("%s,%s" %(clusterLanguage,clusterCategory))
    isNew = 0
    langObj = Language.objects.get(Name=clusterLanguage)
    categoryObj = News_Category.objects.get(Name=clusterCategory)

    maxDict = getMaxClusterId(clusterLanguage,clusterCategory)
    if maxDict['Cluster_Id__max'] :
        maxClusterId = maxDict['Cluster_Id__max'] + 1
    else :
        maxClusterId = 1

    #deltaDate = datetime.date.today() - datetime.timedelta(days=deltaDays)
    #deltaDate = timezone.localtime(timezone.now()).date() - datetime.timedelta(days=deltaDays)
    deltaDate = datetime.datetime.now() - datetime.timedelta(hours=deltaHours)

    feedsList = getFeeds(clusterLanguage,clusterCategory)
    for feedsDict in feedsList:
        if str(feedsDict['Type']) == 'RSS 2.0':
            newsDictList = getRSS2FeedParserData(clusterLanguage,clusterCategory,feedsDict)
        else:
            newsDictList = getAPI2ParserData(clusterLanguage,clusterCategory,feedsDict)
        insertNewsArticle(newsDictList,deltaHours,isNew)


    articleObj =  News_Article.objects.filter(Language = langObj,Category = categoryObj).order_by('Published_Date')

    deleteLangCategoryTable(clusterLanguage, clusterCategory)
    cnt = 0
    for article in articleObj:
        #if article.Published_Date.date() >= deltaDate:
        dtNaive = article.Published_Date.replace(tzinfo=None)
        if dtNaive >= deltaDate:
            newsArticleObjFound = selectLangCategoryTable(clusterLanguage,clusterCategory,article.URL)
            if not newsArticleObjFound:
                cnt+=1
                insertLangCategoryTable(article.id,clusterLanguage,clusterCategory,article,maxClusterId,isRep=True)
                maxClusterId+=1
    logger.info("Number of inserted articles : %s" %cnt)
    logger.info("%s,%s" %(clusterLanguage,clusterCategory))
    logger.info("Exited insertWithoutClustering ")

def insertCategoryNewDoc(lang, category, cluster_file, outlier_file):
    logger.info("Entered insertCategoryNewDoc ")
    maxDict = getMaxClusterId(lang, category)
    if maxDict['Cluster_Id__max']:
        maxClusterId = maxDict['Cluster_Id__max'] + 1
    else:
        maxClusterId = 1

    maxDict = getMaxClusterIdForRerun(lang, category)
    if maxDict['Cluster_Id__max']:
        maxClusterIdForRerun = maxDict['Cluster_Id__max'] + 1
    else:
        maxClusterIdForRerun = 1

    deleteRerunTable(lang, category)

    f = open(cluster_file, 'r')
    clusterIdPrev = -1
    for line in f:
        clusterId = int(line.split()[0])
        key = line.split()[1]
        articleObj = News_Article.objects.get(id=int(key))
        if clusterIdPrev == -1:  # For the first line of the file
            insertLangCategoryRerunTable(int(key),lang, category, articleObj, maxClusterId, isRep=1)

        else:
            if clusterId == clusterIdPrev:  # When articles of same Cluster
                insertLangCategoryRerunTable(int(key),lang, category, articleObj, maxClusterId, isRep=0)
            else:
                maxClusterId += 1  # When articles of different Cluster
                insertLangCategoryRerunTable(int(key),lang, category, articleObj, maxClusterId, isRep=1)
        clusterIdPrev = clusterId
    f.close()

    maxDict = getMaxClusterIdForRerun(lang, category)
    if maxDict['Cluster_Id__max']:
        maxClusterId = maxDict['Cluster_Id__max'] + 1
    else:
        maxClusterId = maxClusterIdForRerun

    f2 = open(outlier_file, 'r')
    for line in f2:
        key = line.split()[1]
        articleObj = News_Article.objects.get(id=int(key))
        insertLangCategoryRerunTable(int(key),lang, category, articleObj, maxClusterId, isRep=1)
        maxClusterId += 1
    f2.close()
    logger.info("Exited insertCategoryNewDoc ")

def sortForRep(lang, category):
    langCategotyAll = []
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategotyAll = English_Top_Stories.objects.all().order_by('Cluster_Id','-Published_Date')
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategotyAll = Marathi_Top_Stories.objects.all().order_by('Cluster_Id','-Published_Date')

    prevClusterId = -1
    isRepFound = False
    isRepIds =[]
    cnt = 0
    for langCatObj in langCategotyAll:
        if prevClusterId != langCatObj.Cluster_Id:
            isRepIds.insert(cnt,langCatObj.id)
            prevClusterId = langCatObj.Cluster_Id
            cnt +=1

    for langCatObj in langCategotyAll:
        for ids in isRepIds:
            if langCatObj.id == ids:
                isRepFound = True
        if isRepFound == True:
            updateRep(lang,category,langCatObj,isRep=True)
        else :
            updateRep(lang,category,langCatObj,isRep=False)
        isRepFound = False

def socialIndicators(lang, category):

    langCategotyAll = []
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoty = English_Top_Stories.objects.all().order_by('Cluster_Id')[:1]
            minClusterId = getMinClusterId(langCategoty)
            maxClusterId = minClusterId + 11
            langCategotyAll = English_Top_Stories.objects.filter(Cluster_Id__lt = maxClusterId).order_by('Cluster_Id','-Is_Rep')
    elif lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoty = Marathi_Top_Stories.objects.all().order_by('Cluster_Id')[:1]
            minClusterId = getMinClusterId(langCategoty)
            maxClusterId = minClusterId + 11
            langCategotyAll = Marathi_Top_Stories.objects.filter(Cluster_Id__lt = maxClusterId).order_by('Cluster_Id','-Is_Rep')
    elif lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoty = Hindi_Top_Stories.objects.all().order_by('Cluster_Id')[:1]
            minClusterId = getMinClusterId(langCategoty)
            maxClusterId = minClusterId + 11
            langCategotyAll = Hindi_Top_Stories.objects.filter(Cluster_Id__lt = maxClusterId).order_by('Cluster_Id','-Is_Rep')

    prevClusterId = -1
    socialAPI = "https://graph.facebook.com/fql?q=SELECT%20url,%20normalized_url,%20share_count,%20like_count,%20comment_count,%20total_count,%20commentsbox_count,%20comments_fbid,%20click_count%20FROM%20link_stat%20WHERE%20url='"
    clusterSocialList = []
    '''if lang.lower() == ENGLISH.lower():
        f= open(SOCIAL_URL_FILE_ENG,'a')
    elif lang.lower() == MARATHI.lower():
        f= open(SOCIAL_URL_FILE_MAR,'a')
    elif lang.lower() == HINDI.lower():
        f= open(SOCIAL_URL_FILE_HIN,'a')'''

    for langCatObj in langCategotyAll:
        socialAPIURL = socialAPI + langCatObj.URL + "'"
        try:
            r = requests.get(socialAPIURL)
            wjson = r.json()
        except:
            wjson['facebook']['total_count'] = 0

        if prevClusterId == langCatObj.Cluster_Id:
            commentCount = scrape4comments(langCatObj.URL,langCatObj.Source_id)
            clusterSocialDict['fbShareCount'] = clusterSocialDict['fbShareCount'] + wjson['data'][0]['total_count'] + int(commentCount)
        else:
            if prevClusterId != -1:
                clusterSocialList.append(clusterSocialDict)
            clusterSocialDict = {}
            clusterSocialDict['Cluster_id'] = langCatObj.Cluster_Id
            clusterSocialDict['repTitle'] = langCatObj.Title
            clusterSocialDict['fbShareCount'] = 0
            commentCount = scrape4comments(langCatObj.URL,langCatObj.Source_id)
            clusterSocialDict['fbShareCount'] = clusterSocialDict['fbShareCount'] + wjson['data'][0]['total_count'] + int(commentCount)
        prevClusterId = langCatObj.Cluster_Id
    string = '\n' + '\n'
    '''f.write(string)
    string = str(datetime.datetime.now()) + '\n'
    f.write(string)
    for dict in clusterSocialList:
        string = str(dict['Cluster_id']) + ' ' + dict['repTitle'].encode('utf-8') + '\n'
        f.write(string)'''
    clusterSocialList2 = bubleSort(clusterSocialList)


    #string = '\n' + '\n'
    #f.write(string)
    newClusterid = minClusterId
    for dict1 in clusterSocialList2:
        dict1['Cluster_id_new'] = newClusterid
        newClusterid +=1
        #string = str(dict1['Cluster_id']) + ' ' + dict1['repTitle'].encode('utf-8') + '\n'
        #f.write(string)
    #f.close()


    for dict3 in clusterSocialList2:
        for langCategotyObj in langCategotyAll:
            if langCategotyObj.Cluster_Id == dict3['Cluster_id']:
                TopStories = English_Top_Stories.objects.filter(id = langCategotyObj.id)
                for TopStoriesObj in TopStories:
                    TopStoriesObj.Cluster_Id = dict3['Cluster_id_new']
                    TopStoriesObj.save()

def bubleSort(clusterSocialList):
    swapped = True
    while swapped == True:
        swapped = False
        total = len(clusterSocialList)
        cnt =0
        for index, item in enumerate(clusterSocialList):
            cnt+=1
            next = index + 1
            if cnt < total:
                if clusterSocialList[index]['fbShareCount'] < clusterSocialList[next]['fbShareCount']:
                    clusterSocialList[index],clusterSocialList[next] = swap(clusterSocialList[index], clusterSocialList[next])
                    swapped = True
    return clusterSocialList

def swap(dict1,dict2):

    dict3 = dict1
    dict1 = dict2
    return dict1,dict3

def getMinClusterId(langCategotyAll):
    for langCatObj in langCategotyAll:
        return langCatObj.Cluster_Id

def isUrlanImage(URL):
    #logger.info("Entered isUrlanImage ")
    try:
        response= urllib2.urlopen(HeadRequest(URL))
        maintype= response.headers['Content-Type'].split(';')[0].lower()
        if maintype not in ('image/png', 'image/jpeg', 'image/gif'):
            #logger.info("Exited isUrlanImage ")
            return False
        else:
            #logger.info("Exited isUrlanImage ")
            return True
    except :
        #logger.info("Exited isUrlanImage ")
        return False

class HeadRequest(urllib2.Request):
    logger.info("Entered HeadRequest ")
    def get_method(self):
        return 'HEAD'
    logger.info("Exited HeadRequest ")

def createTopN(clusterLanguage):
    logger.info("Entered createTopN ")
    deleteLangCategoryTable(clusterLanguage, TOPN)
    langObj = Language.objects.get(Name=clusterLanguage)
    categoryObj = News_Category.objects.get(Name=TOP_STORIES)
    #f=open(SUMMARY_MARATHI_FILE,'r')
    #for line in f:
    #    SUMMARY_MARATHI = line
    #f.close()
    #SUMMARY_MARATHI = SUMMARY_MARATHI.split('= ')[1]
    try:
        if clusterLanguage.lower()==ENGLISH.lower():
            englsihCategoryObj = English_Top_Stories.objects.filter(Is_Rep = 1).order_by('Cluster_Id')
            cnt  = 0
            for catObj in englsihCategoryObj:
                if cnt < 1:
                    if catObj.Thumbnail:
                        articleObj = News_Article.objects.get(id = catObj.Article.id,
                                                          Language = langObj,
                                                          Category = categoryObj)
                        topNObject = TopN_English(Article = articleObj,
                                                    URL = articleObj.URL,
                                                    Title = articleObj.Title,
                                                    Summary = SUMMARY,
                                                    Thumbnail = articleObj.Thumbnail,
                                                    Source = articleObj.Source,
                                                    Published_Date=articleObj.Published_Date)
                        topNObject.save()
                        cnt+=1
    except Exception, e:
        logger.info("No data in English_Top_Stories Table")
    try:
        if clusterLanguage.lower()==MARATHI.lower():
            marathiCategoryObj = Marathi_Top_Stories.objects.filter(Is_Rep = 1).order_by('Cluster_Id')
            cnt  = 0
            for catObj in marathiCategoryObj:
                if cnt < 1:
                    if catObj.Thumbnail:
                        articleObj = News_Article.objects.get(id = catObj.Article.id,
                                                          Language = langObj,
                                                          Category = categoryObj)
                        topNObject = TopN_Marathi(Article = articleObj,
                                                    URL = articleObj.URL,
                                                    Title = articleObj.Title,
                                                    Summary = SUMMARY_MARATHI,
                                                    Thumbnail = articleObj.Thumbnail,
                                                    Source = articleObj.Source,
                                                    Published_Date=articleObj.Published_Date)
                        topNObject.save()
                        cnt+=1
    except Exception, e:
        logger.info("No data in Marathi_Top_Stories Table")


    if clusterLanguage.lower()==HINDI.lower():
        hindiCategoryObj = Hindi_Top_Stories.objects.filter(Is_Rep = 1).order_by('Cluster_Id')
        cnt  = 0
        for catObj in hindiCategoryObj:
            if cnt < 1:
                if catObj.Thumbnail:

                    articleObj = News_Article.objects.get(id = catObj.Article.id,
                                                      Language = langObj,
                                                      Category = categoryObj)

                    topNObject = TopN_Hindi(Article = articleObj,
                                                URL = articleObj.URL,
                                                Title = articleObj.Title,
                                                Summary = SUMMARY_HINDI,
                                                Thumbnail = articleObj.Thumbnail,
                                                Source = articleObj.Source,
                                                Published_Date=articleObj.Published_Date)
                    topNObject.save()
                    cnt+=1



    logger.info("Exited createTopN ")


