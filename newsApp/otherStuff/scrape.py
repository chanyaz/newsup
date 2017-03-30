import urllib2
from bs4 import BeautifulSoup
import re
from newspaper import Article

articleSourceName =[
    'IB Times','Digit','Blog To Bollywood','FilmiBeat','Mid Day',
    'ANI','Bold Sky','Travelmasti','News Nation','Travel Daily Media','Firstpost','New Kerela','Cricket Country',
    'Daily Climate','Amar Ujala','Bhaskar','Patrika','Jagran Hindi','Navbharat Times','Nai Duniya',
    'Rajasthan Patrika','Pratah Kal','Prabhat Khabar','Ranchi Express','DeshBandhu','Jansatta','ABP News',
    'Aaj Tak','ZeeNews Hindi','WebDuniya Hindi','Live Hindustan'
]
def scrapeArticleForImage(url,sourceName):
    #logger.info("Entered scrapeArticleForImage ")
    print sourceName
    try:
        html = urllib2.urlopen(url, None, 10)
        soup = BeautifulSoup(html)

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
            found = False
            for img in imgs:
                if found == False:
                    found = True
                    return img['src']

        if sourceName == "Business Standard":
            imgs = soup.findAll("img", {"class":"imgCont"})
            found = False
            for img in imgs:
                if found == False:
                    found = True
                    return img['src']

        if sourceName == "The Statesman":
            imgs = soup.findAll("img", {"alt":"title="})
            found = False
            for img in imgs:
                if found == False:
                    found = True
                    return img['src']

        if sourceName == "Business Wire":
            imgs = soup.findAll("div", {"id":"bwbodyimg"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']


        if sourceName == "Financial Express" :
            imgs = soup.findAll("div", {"class":"storypic"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']

        if sourceName == "Jagran" :
            imgs = soup.findAll("div", {"class":"stryimg"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['data-src']

        if sourceName == "Deccan Herald" :
            imgs = soup.findAll("img", {"class":"floatLeftImg"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink['src']

        if sourceName == "Asian Age" :
            imgs = soup.findAll("img", {"class":"image image-content_image "})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink['src']

        if sourceName == "Economy Watch" :
            imgs = soup.findAll("div", {"class":"field-item odd"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']

        if sourceName == "Filmfare" :
            imgs = soup.findAll("div", {"class":"upperBlk"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.figure.img['src']

        if sourceName == "Techtree" :
            imgs = soup.findAll("div", {"class":"preview-img"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']


        if sourceName == "BGR" :
            imgs = soup.findAll("div", {"class":"post-img-wrap bgr-style-normal"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']

        if sourceName == "EurekAlert" :
            imgs = soup.findAll("div", {"class":"img-wrapper"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']

        if sourceName == "Travelmasti" :
            imgs = soup.findAll("img", {"id":"myPicture"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink['src']

        if sourceName == "Huffington Post" :
            imgs = soup.findAll("div", {"class":"main-visual group embedded-image"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    if imglink.span :
                        return imglink.span.img['src']
                    else:
                        return imglink.img['src']

        if sourceName == "Indian Express" :
            imgs = soup.findAll("span", {"class":"custom-caption"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    if imglink.img:
                        return imglink.img['src']

        if sourceName == "India TV" :
            imgs = soup.findAll("div", {"class":"mad-first-img"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']
        if sourceName == "Filmy Monkey" :
            imgs = soup.findAll("div", {"class":"featured"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.div.a.img['src']
        if sourceName == "Maharashtra Times" :
            imgs = soup.findAll("div", {"class":"thumbImage"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']

        if sourceName == "Divya Marathi" :
            imgs = soup.findAll("img", {"class":"lazy"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink['data-href']

        if sourceName == "Firstpost":
            imgs = soup.findAll("div", {"class":"wp-caption alignleft"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.a.img['data-original']

        if sourceName == "Samna":
            imgs = soup.findAll("div", {"class":"col-lg-3 col-xs-12 pic-newslist"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']
        if sourceName == "Elle" :
            imgs = soup.findAll("div", {"class":"embedded-image--inner"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['data-src']
        if sourceName == "Loksatta" :
            imgs = soup.findAll("div", {"class":"imgholder"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']
        if sourceName == "IBNLive" :
            imgs = soup.findAll("figure", {"class":"article_img"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']

        if sourceName == "Hindustan Times" :
            imgs = soup.findAll("div", {"class":"news_photo"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    imageUrl = 'http://www.hindustantimes.com' +  imglink.img['src']
                    return imageUrl

        if sourceName == "The Hindu Business Line" :
            imgs = soup.findAll("div", {"id":"hcenter"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']

        if sourceName == "BBC" :
            imgs = soup.findAll("span", {"id":"image-and-copyright-container"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']
        if sourceName == "Tecake" :
            imgs = soup.findAll("div", {"class":"td-post-featured-image"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']
        if sourceName == "India" :
            imgs = soup.findAll("section", {"class":"content-wrap eventtracker"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.div.img['src']
        if sourceName == "Cricket Country" :
            imgs = soup.findAll("div", {"class":"wp-caption aligncenter"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.img['src']
        if sourceName == "Medical News Today" :
            imgs = soup.findAll("div", {"class":"photobox_right"})
            found = False
            for imglink in imgs:
                if found == False:
                    found = True
                    return imglink.data-src['src']

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



    except Exception, e:
        print("For %s , image not found" %url)
	#logger.info("Exited scrapeArticleForImage ")

src = scrapeArticleForImage('http://naidunia.jagran.com/chhattisgarh/bhilai-winners-received-prizes-666760',
                            'Jagran Hindi')
print src