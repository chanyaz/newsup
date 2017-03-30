from bs4 import BeautifulSoup
import urllib2
from models import *
from newspaper import Article
import re
import logging
import socket
from userConstants import articleSourceName

logger = logging.getLogger('django')

def scrapeArticleForImage(url,sourceId):
    #logger.info("Entered scrapeArticleForImage ")
    try:
        html = urllib2.urlopen(url, None, 10)
        soup = BeautifulSoup(html)
        sourceObj = News_Source.objects.get(id=sourceId)
        sourceName = sourceObj.Name
        if sourceName == "ABP Majha":
            imgs = soup.find_all("img", {"class":"media "})
            for img in imgs:
                return img['src']

        if sourceName == 'IBN Lokmat':
            imgs = soup.find_all('img', class_=re.compile('aligncenter'))
            for img in imgs:
                return img['src']
            else:
                imgs = soup.find_all('img', class_=re.compile('alignleft'))
                for img in imgs:
                    return img['src']

        if sourceName == 'Lokmat':
            imgs = soup.findAll("img", {"style":"max-width:320px;margin-top:7px;"})
            for img in imgs:
                return img['src']

        if sourceName == 'Zeenews':
            imgs = soup.findAll("div", {"class":"field-item even"})
            for imglink in imgs:
                return imglink.img['src']

        if sourceName == 'Webdunia':
            imgs = soup.findAll("img", {"class":"imgCont"})
            for img in imgs:
                return img['src']

        if sourceName == "Business Standard":
            imgs = soup.findAll("img", {"class":"imgCont"})
            for img in imgs:
                return img['src']

        if sourceName == "The Statesman":
            imgs = soup.findAll("img", {"alt":"title="})
            for img in imgs:
                return img['src']

        if sourceName == "Business Wire":
            imgs = soup.findAll("div", {"id":"bwbodyimg"})
            for imglink in imgs:
                return imglink.img['src']


        if sourceName == "Financial Express" :
            imgs = soup.findAll("div", {"class":"storypic"})
            for imglink in imgs:
                return imglink.img['src']

        if sourceName == "Jagran" :
            imgs = soup.findAll("div", {"class":"stryimg"})
            for imglink in imgs:
                return imglink.img['data-src']

        if sourceName == "Deccan Herald" :
            imgs = soup.findAll("img", {"class":"floatLeftImg"})
            for imglink in imgs:
                return imglink['src']

        if sourceName == "Asian Age" :
            imgs = soup.findAll("img", {"class":"image image-content_image "})
            for imglink in imgs:
                return imglink['src']

        if sourceName == "Economy Watch" :
            imgs = soup.findAll("div", {"class":"field-item odd"})
            for imglink in imgs:
                return imglink.img['src']

        if sourceName == "Filmfare" :
            imgs = soup.findAll("div", {"class":"upperBlk"})
            for imglink in imgs:
                return imglink.figure.img['src']

        if sourceName == "Techtree" :
            imgs = soup.findAll("div", {"class":"preview-img"})
            for imglink in imgs:
                return imglink.img['src']


        if sourceName == "BGR" :
            imgs = soup.findAll("div", {"class":"post-img-wrap bgr-style-normal"})
            for imglink in imgs:
                return imglink.img['src']

        if sourceName == "EurekAlert" :
            imgs = soup.findAll("div", {"class":"img-wrapper"})
            for imglink in imgs:
                return imglink.img['src']

        if sourceName == "Travelmasti" :
            imgs = soup.findAll("img", {"id":"myPicture"})
            for imglink in imgs:
                return imglink['src']

        if sourceName == "Huffington Post" :
            imgs = soup.findAll("div", {"class":"main-visual group embedded-image"})
            for imglink in imgs:
                if imglink.span :
                    return imglink.span.img['src']
                else:
                    return imglink.img['src']

        if sourceName == "Indian Express" :
            imgs = soup.findAll("span", {"class":"custom-caption"})
            for imglink in imgs:
                if imglink.img:
                    return imglink.img['src']

        if sourceName == "India TV" :
            imgs = soup.findAll("div", {"class":"mad-first-img"})
            for imglink in imgs:
                return imglink.img['src']
        if sourceName == "Filmy Monkey" :
            imgs = soup.findAll("div", {"class":"featured"})
            for imglink in imgs:
                return imglink.div.a.img['src']
        if sourceName == "Maharashtra Times" :
            imgs = soup.findAll("div", {"class":"thumbImage"})
            for imglink in imgs:
                return imglink.img['src']

        if sourceName == "Divya Marathi" :
            imgs = soup.findAll("img", {"class":"lazy"})
            for imglink in imgs:
                return imglink['data-href']

        if sourceName == "Samna":
            imgs = soup.findAll("div", {"class":"col-lg-3 col-xs-12 pic-newslist"})
            for imglink in imgs:
                return imglink.img['src']
        if sourceName == "Elle" :
            imgs = soup.findAll("div", {"class":"embedded-image--inner"})
            for imglink in imgs:
                return imglink.img['data-src']
        if sourceName == "Loksatta" :
            imgs = soup.findAll("div", {"class":"imgholder"})
            for imglink in imgs:
                return imglink.img['src']
        if sourceName == "IBNLive" :
            imgs = soup.findAll("figure", {"class":"article_img"})
            for imglink in imgs:
                return imglink.img['src']
        if sourceName == "Hindustan Times" :
            imgs = soup.findAll("div", {"class":"news_photo"})
            for imglink in imgs:
                imageUrl = 'http://www.hindustantimes.com' +  imglink.img['src']
                return imageUrl

        if sourceName == "The Hindu Business Line" :
            imgs = soup.findAll("div", {"id":"hcenter"})
            for imglink in imgs:
                return imglink.img['src']

        if sourceName == "BBC" :
            imgs = soup.findAll("span", {"id":"image-and-copyright-container"})
            for imglink in imgs:
                return imglink.img['src']
        if sourceName == "tecake" :
            imgs = soup.findAll("div", {"class":"td-post-featured-image"})
            for imglink in imgs:
                return imglink.img['src']
        if sourceName == "India" :
            imgs = soup.findAll("section", {"class":"content-wrap eventtracker"})
            for imglink in imgs:
                return imglink.div.img['src']
        if sourceName == "Cricket Country" :
            imgs = soup.findAll("div", {"class":"wp-caption aligncenter"})
            for imglink in imgs:
                return imglink.img['src']
        if sourceName == 'Nationnal Duniya':
            imgs = soup.findAll("div", {"align":"center"})
            for imglink in imgs:
                return imglink.img['src']
        if sourceName == 'Haribhoomi':
            imgs = soup.findAll("div", {"class":"entry-img featured-img"})
            for imglink in imgs:
                return imglink.img['src']


        for articleSource in articleSourceName:
            if sourceName == articleSource:
                article = Article(url)
                article.download()
                article.parse()
                if article.top_image:
                    return  article.top_image



        logger.info("For %s , image not found" %url)

    except socket.timeout:
        logger.info("For %s , timed out error!!!!!!" %url)
    except Exception, e:
        logger.info("For %s , image not found" %url)
	#logger.info("Exited scrapeArticleForImage ")
