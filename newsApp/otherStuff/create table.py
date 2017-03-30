# -*- coding: utf-8 -*-
import os

city = [
'UttarPradesh',
'Uttarakhand',
'HimachalPradesh',
'Delhi',
'JammuKashmir',
'Punjab',
'MadhyaPradesh',
'Jharkhand',
'Bihar',
'Haryana',
'Chattisgarh',
'Rajasthan',
'WestBengal',
'Orissa',
'Gujrat',
'Maharashtra',
'Lucknow',
'Allahabad',
'Pratapgarh',
'Kanpur',
'Merath',
'Agra',
'Noida',
'Gaziabad',
'Bagpat',
'Saharnpur',
'Bulandshahar',
'Varanasi',
'Gorakhpur',
'Jhansi',
'Muzaffarnagar',
'Sitapur',
'Jaunpur',
'Azamgarh',
'Moradabad',
'Bareilly',
'Balia',
'Aligarh',
'Mathura',
'Bhopal',
'Indore',
'Gwalior',
'Jabalpur',
'Ujjain',
'Ratlam',
'Sagar',
'Dewas',
'Satna',
'Rewa',
'Patna',
'Bhagalpur',
'Mujaffarpur',
'Gaya',
'Darbhanga',
'Poorniya',
'Sewan',
'Begusarai',
'Katihar',
'Jaipur',
'Udaipur',
'Jodhpur',
'Ajmer',
'Bikaner',
'Alwar',
'Sikar',
'Kota',
'Bhilwara',
'Bharatpur',
'Chhatis',
'Raipur',
'Bhilai',
'Rajnandgao',
'Raigarh',
'Jagdalpur',
'Korva',
'Ranchi',
'Dhanbad',
'Jamshedpur',
'Giridihi',
'Hazaribagh',
'Bokaro',
'Dehradun',
'Nainitaal',
'Haridwaar',
'Almorah',
'UddhamSinghNagar',
'Simla',
'Mandi',
'Bilaspur',
'Amritsar',
'Jalandhar',
'Ludhiana',
'Roparh',
'Chandigarh',
'Rohtak',
'Panchkula',
'Ambala',
'Panipat',
'Gurgaon',
'Hissar',
'Jammu',
'Srinagar',
'Poonch',
'Kolkata',
'Jalpaigurhi',
'Darjeeling',
'Asansol',
'Siligurhi',
'Bhuvaneshwar',
'Puri',
'Cuttack',
'Ahmedabad',
'Surat',
'Vadodara',
'Mumbai',
'Nagpur',
'Pune',
]
categoryObj=[
'Sports',
'Top_Stories',
'World',
'Opinion',
'Health',
'Lifestyle',
'Entertainment',
'Technology',
'Politics',
'Environment',
'Travel',
'Science',
'Business',
'Stocks',
'Food',
'Weekend',
'Fashion',
]


def writeTable(lang, item):
    string = "\n" + "class " + lang + "_" + item + "_Rerun(models.Model):"
    f.write(string)
    string = "\n" + "    " + "Cluster_Id = models.IntegerField()"
    f.write(string)
    string = "\n" + "    " + "Article = models.ForeignKey(News_Article)"
    f.write(string)
    string = "\n" + "    " + "URL = models.URLField(max_length=300)"
    f.write(string)
    string = "\n" + "    " + "Title = models.CharField(max_length=100)"
    f.write(string)
    string = "\n" + "    " + "Summary = models.CharField(max_length=200)"
    f.write(string)
    string = "\n" + "    " + "Thumbnail = models.URLField(max_length=300,null=True,blank=True)"
    f.write(string)
    string = "\n" + "    " + "Source = models.ForeignKey(News_Source)"
    f.write(string)
    string = "\n" + "    " + "Published_Date=models.DateTimeField()"
    f.write(string)
    string = "\n" + "    " + "Is_Rep = models.BooleanField(default=False)"
    f.write(string)
    string = "\n" + "\n" + "    " + "def __unicode__(self):"
    f.write(string)
    string = "\n" + "    " + "    " + "return '%s %s %s' % (self.Title,self.URL,self.Source)"
    f.write(string)
    string = "\n"
    f.write(string)


def writeVariables():
    for item in categoryObj:
        string = item.upper() + ' ' + "=" + ' ' + "'" + item + "'" + '\n'
        f.write(string)
    for item in city:
        string = item.upper() + ' ' + "=" + ' ' + "'" + item + "'" + '\n'
        f.write(string)


def writeMaxquery(lang, cat):
    #string = "if lang.lower() == " + lang.upper() + ".lower()" + ":" + '\n'
    #f.write(string)
    string = "    elif category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "        maxDict = " + lang + "_" + cat + "_Rerun.objects.all().aggregate(Max('Cluster_Id'))" + '\n'
    f.write(string)


def writeInsert(lang, cat):
    string = "    if lang.lower() == " + lang.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "        if category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "            langCategoryObj = " + lang + "_" + cat  + "( Article = articleObj," + '\n'
    f.write(string)
    string = "                                        URL = articleObj.URL," + '\n'
    f.write(string)
    string = "                                        Title = articleObj.Title," + '\n'
    f.write(string)
    string = "                                        Summary = articleObj.Summary," + '\n'
    f.write(string)
    string = "                                        Thumbnail = articleObj.Thumbnail," + '\n'
    f.write(string)
    string = "                                        Source = articleObj.Source," + '\n'
    f.write(string)
    string = "                                        Published_Date=articleObj.Published_Date," + '\n'
    f.write(string)
    string = "                                        Cluster_Id = articleObj.Cluster_Id," + '\n'
    f.write(string)
    string = "                                        Is_Rep = articleObj.Is_Rep)" + '\n'
    f.write(string)
    string = "            langCategoryObj.save()" + '\n'
    f.write(string)


def writeSelect(lang, cat):
    #string = "if lang.lower() == " + lang.upper() + ".lower()" + ":" + '\n'
    #f.write(string)
    string = "    if category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "        try:" + '\n'
    f.write(string)
    string = "            langCategoryObj = " + lang + "_" + cat + ".objects.get(URL = URL)" + '\n'
    f.write(string)
    string = "            return True" + '\n'
    f.write(string)
    string = "        except " + lang + "_" + cat + ".DoesNotExist:" + '\n'
    f.write(string)
    string = "            return False" + '\n'
    f.write(string)

def writeSelectAll(lang, cat):
    string = "if lang.lower() == " + lang.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "    if category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "        langCategotyAll = " + lang + "_" + cat + ".objects.all()" + '\n'
    f.write(string)


def deleteFrom(lang, cat):
    string = "if lang.lower() == " + lang.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "    if category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "        langCategoryObj = " + lang + "_" + cat + ".objects.all().delete()" + '\n'
    f.write(string)


def writeAllquery(lang, cat):
    string = "if lang.lower() == " + lang.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "    if category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "        langCategotyAll = " + lang + "_" + cat + "_Rerun" + ".objects.all()" + '\n'
    f.write(string)


def writeFunction(lang, cat):
    string = "clusterOnLanguageCategory(" + lang.upper() + ',' + cat.upper() + ")" + '\n'
    f.write(string)

def writeInsertRaw(lang, cat):
    string = "if lang.lower() == " + lang.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "    if category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "        langObj = Language.objects.get(Name=lang)" + '\n'
    f.write(string)
    string = "        categoryObj = News_Category.objects.get(Name = category)" + '\n'
    f.write(string)

    string = "        cursor = connection.cursor()" + '\n'
    f.write(string)
    string = "        cursor.execute('''INSERT INTO news_schema.newsapp_"+ lang.lower()+'_'+ cat.lower()+'_rerun' + '\n'
    f.write(string)
    string = "                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)" + '\n'
    f.write(string)
    string = "                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s" + '\n'
    f.write(string)
    string = "                           from news_schema.newsapp_news_article" + '\n'
    f.write(string)
    string = "                           WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])" + '\n'
    f.write(string)

def writeInsertRaw2(lang, cat):
    string = "if lang.lower() == " + lang.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "    if category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "        langObj = Language.objects.get(Name=lang)" + '\n'
    f.write(string)
    string = "        categoryObj = News_Category.objects.get(Name = category)" + '\n'
    f.write(string)

    string = "        cursor = connection.cursor()" + '\n'
    f.write(string)
    string = "        cursor.execute('''INSERT INTO news_schema.newsapp_"+ lang.lower()+'_'+ cat.lower() + '\n'
    f.write(string)
    string = "                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)" + '\n'
    f.write(string)
    string = "                           SELECT Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep" + '\n'
    f.write(string)
    string = "                           from news_schema.newsapp_news_article" + '\n'
    f.write(string)
    string = "                           WHERE Language_id = %s and Category_id = %s and id = %s''',[langObj.id,categoryObj.id,articleObj.id])" + '\n'
    f.write(string)

def writeAlter(lang, cat):
    string = "alter table news_schema.newsapp_" + lang.lower()+"_" + cat.lower() + " modify Title blob;" + '\n'
    f.write(string)
    string = "alter database news_schema charset=utf8;" + '\n'
    f.write(string)
    string = "alter table news_schema.newsapp_" + lang.lower()+"_"  + cat.lower() + " modify Title varchar(200) character set utf8;" + '\n'+ '\n'+ '\n'
    f.write(string)
    string = "alter table news_schema.newsapp_" + lang.lower()+"_"  + cat.lower() +"_Rerun"+ " modify Title blob;" + '\n'
    f.write(string)
    string = "alter database news_schema charset=utf8;" + '\n'
    f.write(string)
    string = "alter table news_schema.newsapp_" + lang.lower()+"_"  + cat.lower() +"_Rerun"+ " modify Title varchar(200) character set utf8;" + '\n'+'\n'+ '\n'
    f.write(string)

def deleteTable(lang,cat):
    #string = '    if lang.lower() == ' + lang.upper() + '.lower():' + '\n'
    #f.write(string)
    string = "        elif category.lower() == " + cat.upper() + ".lower()" + ":" + '\n'
    f.write(string)
    string = "            langCategoryObj = " + lang + '_' + cat + ".objects.all().delete()" + '\n'
    f.write(string)
def deleteRerunTable(lang,cat):
    string = "delete from news_schema.newsApp_" + lang.lower()+"_"  + cat.lower() +"_Rerun"+ ';\n'
    f.write(string)

def exception(lang,cat):
    string="    try:"+ '\n'
    f.write(string)
    string="        clusterOnLanguageCategory("+lang.upper()+","+cat.upper()+")"+ '\n'
    f.write(string)
    string="    except Exception, e:"+ '\n'
    f.write(string)
    string="        print "+'"You have an exception :"'+ '\n'
    f.write(string)
    string="        print e.args"+ '\n'+ '\n'
    f.write(string)

def trailingDots(string):
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

def createFolder(name):
    newpath = 'E:/NewsApp/OutputFiles/Hindi/' + name
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def createClusteron(lang,cat,delta):
    string = 'try:'+'\n'
    f.write(string)
    string = '    insertWithoutClustering('+lang.upper() + ',' + cat.upper() + ',' +delta+')'+'\n'
    f.write(string)
    string = 'except Exception, e:'+'\n'
    f.write(string)
    string = '    logger.exception("You have an exception :%s",e.args)'+'\n'
    f.write(string)

def createGetCategory(cat):
    string = 'if category.lower() == '+ cat.upper()+'.lower():'+'\n'
    f.write(string)
    #string='    if maxClusterId:'+'\n'
    #f.write(string)
    string='    categoryDict = Hindi_'+cat+".objects.filter(Source = sourceObj,Cluster_Id__gt=maxClusterId).order_by('Cluster_Id')[:limit]"+'\n'
    f.write(string)
    #string='    else:'+'\n'
    #f.write(string)
    #string='        categoryDict = Hindi_'+cat+".objects.filter(Is_Rep = 1).order_by('-Cluster_Id')[:limit]"+'\n'
    #f.write(string)
f= open("E:\NewsApp\models.txt",'w')

def getSimilarNews(cat):
    string = 'if category.lower() == '+cat.upper()+'.lower():'+'\n'
    f.write(string)
    string = '    categoryDict = Hindi_'+cat+".objects.filter(Is_Rep = 0,Cluster_Id=clusterId).order_by('-Published_Date')[:limit]"+'\n'
    f.write(string)

for item in city:
    deleteTable('Hindi',item)
'''for item in categoryObj:
    createGetCategory(item)'''
f.close()




