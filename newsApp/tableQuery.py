from models import *
from userConstants import *
from django.db.models import Max
from django.db import connection
import datetime


def getMaxClusterId(lang, category):
    #logger.info("Entered getMaxClusterId ")
    if lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            maxDict = Hindi_Sports.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == TOP_STORIES.lower():
            maxDict = Hindi_Top_Stories.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == WORLD.lower():
            maxDict = Hindi_World.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == OPINION.lower():
            maxDict = Hindi_Opinion.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == HEALTH.lower():
            maxDict = Hindi_Health.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == LIFESTYLE.lower():
            maxDict = Hindi_Lifestyle.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ENTERTAINMENT.lower():
            maxDict = Hindi_Entertainment.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == TECHNOLOGY.lower():
            maxDict = Hindi_Technology.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == POLITICS.lower():
            maxDict = Hindi_Politics.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ENVIRONMENT.lower():
            maxDict = Hindi_Environment.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BOOKS.lower():
            maxDict = Hindi_Books.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == TRAVEL.lower():
            maxDict = Hindi_Travel.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SCIENCE.lower():
            maxDict = Hindi_Science.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BUSINESS.lower():
            maxDict = Hindi_Business.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == STOCKS.lower():
            maxDict = Hindi_Stocks.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == FOOD.lower():
            maxDict = Hindi_Food.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == WEEKEND.lower():
            maxDict = Hindi_Weekend.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == FASHION.lower():
            maxDict = Hindi_Fashion.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == UTTARPRADESH.lower():
            maxDict = Hindi_UttarPradesh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == UTTARAKHAND.lower():
            maxDict = Hindi_Uttarakhand.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == HIMACHALPRADESH.lower():
            maxDict = Hindi_HimachalPradesh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == DELHI.lower():
            maxDict = Hindi_Delhi.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JAMMUKASHMIR.lower():
            maxDict = Hindi_JammuKashmir.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == PUNJAB.lower():
            maxDict = Hindi_Punjab.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MADHYAPRADESH.lower():
            maxDict = Hindi_MadhyaPradesh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JHARKHAND.lower():
            maxDict = Hindi_Jharkhand.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BIHAR.lower():
            maxDict = Hindi_Bihar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == HARYANA.lower():
            maxDict = Hindi_Haryana.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == CHATTISGARH.lower():
            maxDict = Hindi_Chattisgarh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == RAJASTHAN.lower():
            maxDict = Hindi_Rajasthan.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == WESTBENGAL.lower():
            maxDict = Hindi_WestBengal.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ORISSA.lower():
            maxDict = Hindi_Orissa.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == GUJRAT.lower():
            maxDict = Hindi_Gujrat.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MAHARASHTRA.lower():
            maxDict = Hindi_Maharashtra.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == LUCKNOW.lower():
            maxDict = Hindi_Lucknow.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ALLAHABAD.lower():
            maxDict = Hindi_Allahabad.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == PRATAPGARH.lower():
            maxDict = Hindi_Pratapgarh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == KANPUR.lower():
            maxDict = Hindi_Kanpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MERATH.lower():
            maxDict = Hindi_Merath.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == AGRA.lower():
            maxDict = Hindi_Agra.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == NOIDA.lower():
            maxDict = Hindi_Noida.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == GAZIABAD.lower():
            maxDict = Hindi_Gaziabad.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BAGPAT.lower():
            maxDict = Hindi_Bagpat.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SAHARNPUR.lower():
            maxDict = Hindi_Saharnpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BULANDSHAHAR.lower():
            maxDict = Hindi_Bulandshahar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == VARANASI.lower():
            maxDict = Hindi_Varanasi.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == GORAKHPUR.lower():
            maxDict = Hindi_Gorakhpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JHANSI.lower():
            maxDict = Hindi_Jhansi.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MUZAFFARNAGAR.lower():
            maxDict = Hindi_Muzaffarnagar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SITAPUR.lower():
            maxDict = Hindi_Sitapur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JAUNPUR.lower():
            maxDict = Hindi_Jaunpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == AZAMGARH.lower():
            maxDict = Hindi_Azamgarh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MORADABAD.lower():
            maxDict = Hindi_Moradabad.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BAREILLY.lower():
            maxDict = Hindi_Bareilly.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BALIA.lower():
            maxDict = Hindi_Balia.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ALIGARH.lower():
            maxDict = Hindi_Aligarh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MATHURA.lower():
            maxDict = Hindi_Mathura.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BHOPAL.lower():
            maxDict = Hindi_Bhopal.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == INDORE.lower():
            maxDict = Hindi_Indore.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == GWALIOR.lower():
            maxDict = Hindi_Gwalior.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JABALPUR.lower():
            maxDict = Hindi_Jabalpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == UJJAIN.lower():
            maxDict = Hindi_Ujjain.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == RATLAM.lower():
            maxDict = Hindi_Ratlam.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SAGAR.lower():
            maxDict = Hindi_Sagar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == DEWAS.lower():
            maxDict = Hindi_Dewas.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SATNA.lower():
            maxDict = Hindi_Satna.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == REWA.lower():
            maxDict = Hindi_Rewa.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == PATNA.lower():
            maxDict = Hindi_Patna.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BHAGALPUR.lower():
            maxDict = Hindi_Bhagalpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MUJAFFARPUR.lower():
            maxDict = Hindi_Mujaffarpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == GAYA.lower():
            maxDict = Hindi_Gaya.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == DARBHANGA.lower():
            maxDict = Hindi_Darbhanga.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == POORNIYA.lower():
            maxDict = Hindi_Poorniya.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SEWAN.lower():
            maxDict = Hindi_Sewan.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BEGUSARAI.lower():
            maxDict = Hindi_Begusarai.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == KATIHAR.lower():
            maxDict = Hindi_Katihar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JAIPUR.lower():
            maxDict = Hindi_Jaipur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == UDAIPUR.lower():
            maxDict = Hindi_Udaipur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JODHPUR.lower():
            maxDict = Hindi_Jodhpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == AJMER.lower():
            maxDict = Hindi_Ajmer.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BIKANER.lower():
            maxDict = Hindi_Bikaner.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ALWAR.lower():
            maxDict = Hindi_Alwar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SIKAR.lower():
            maxDict = Hindi_Sikar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == KOTA.lower():
            maxDict = Hindi_Kota.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BHILWARA.lower():
            maxDict = Hindi_Bhilwara.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BHARATPUR.lower():
            maxDict = Hindi_Bharatpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == CHHATIS.lower():
            maxDict = Hindi_Chhatis.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == RAIPUR.lower():
            maxDict = Hindi_Raipur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BILASPUR.lower():
            maxDict = Hindi_Bilaspur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BHILAI.lower():
            maxDict = Hindi_Bhilai.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == RAJNANDGAO.lower():
            maxDict = Hindi_Rajnandgao.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == RAIGARH.lower():
            maxDict = Hindi_Raigarh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JAGDALPUR.lower():
            maxDict = Hindi_Jagdalpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == KORVA.lower():
            maxDict = Hindi_Korva.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == RANCHI.lower():
            maxDict = Hindi_Ranchi.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == DHANBAD.lower():
            maxDict = Hindi_Dhanbad.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JAMSHEDPUR.lower():
            maxDict = Hindi_Jamshedpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == GIRIDIHI.lower():
            maxDict = Hindi_Giridihi.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == HAZARIBAGH.lower():
            maxDict = Hindi_Hazaribagh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BOKARO.lower():
            maxDict = Hindi_Bokaro.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == DEHRADUN.lower():
            maxDict = Hindi_Dehradun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == NAINITAAL.lower():
            maxDict = Hindi_Nainitaal.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == HARIDWAAR.lower():
            maxDict = Hindi_Haridwaar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ALMORAH.lower():
            maxDict = Hindi_Almorah.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == UDDHAMSINGHNAGAR.lower():
            maxDict = Hindi_UddhamSinghNagar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SIMLA.lower():
            maxDict = Hindi_Simla.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MANDI.lower():
            maxDict = Hindi_Mandi.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == AMRITSAR.lower():
            maxDict = Hindi_Amritsar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JALANDHAR.lower():
            maxDict = Hindi_Jalandhar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == LUDHIANA.lower():
            maxDict = Hindi_Ludhiana.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ROPARH.lower():
            maxDict = Hindi_Roparh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == CHANDIGARH.lower():
            maxDict = Hindi_Chandigarh.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ROHTAK.lower():
            maxDict = Hindi_Rohtak.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == PANCHKULA.lower():
            maxDict = Hindi_Panchkula.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == AMBALA.lower():
            maxDict = Hindi_Ambala.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == PANIPAT.lower():
            maxDict = Hindi_Panipat.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == GURGAON.lower():
            maxDict = Hindi_Gurgaon.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == HISSAR.lower():
            maxDict = Hindi_Hissar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JAMMU.lower():
            maxDict = Hindi_Jammu.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SRINAGAR.lower():
            maxDict = Hindi_Srinagar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == POONCH.lower():
            maxDict = Hindi_Poonch.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == KOLKATA.lower():
            maxDict = Hindi_Kolkata.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == JALPAIGURHI.lower():
            maxDict = Hindi_Jalpaigurhi.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == DARJEELING.lower():
            maxDict = Hindi_Darjeeling.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ASANSOL.lower():
            maxDict = Hindi_Asansol.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SILIGURHI.lower():
            maxDict = Hindi_Siligurhi.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BHUVANESHWAR.lower():
            maxDict = Hindi_Bhuvaneshwar.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == PURI.lower():
            maxDict = Hindi_Puri.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == CUTTACK.lower():
            maxDict = Hindi_Cuttack.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == AHMEDABAD.lower():
            maxDict = Hindi_Ahmedabad.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SURAT.lower():
            maxDict = Hindi_Surat.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == VADODARA.lower():
            maxDict = Hindi_Vadodara.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == MUMBAI.lower():
            maxDict = Hindi_Mumbai.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == NAGPUR.lower():
            maxDict = Hindi_Nagpur.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == PUNE.lower():
            maxDict = Hindi_Pune.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == AUTO.lower():
            maxDict = Hindi_Auto.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == CRIME.lower():
            maxDict = Hindi_Crime.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == FARIDABAD.lower():
            maxDict = Hindi_Faridabad.objects.all().aggregate(Max('Cluster_Id'))

    elif lang == ENGLISH:
        if category.lower() == ECONOMY.lower():
            maxDict = English_Economy.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == SPORTS.lower():
            maxDict = English_Sports.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == TOP_STORIES.lower():
            maxDict = English_Top_Stories.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == WORLD.lower():
            maxDict = English_World.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == OPINION.lower():
            maxDict = English_Opinion.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == HEALTH.lower():
            maxDict = English_Health.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == LIFESTYLE.lower():
            maxDict = English_Lifestyle.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == ENTERTAINMENT.lower():
            maxDict = English_Entertainment.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == TECHNOLOGY.lower():
            maxDict = English_Technology.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == POLITICS.lower():
            maxDict = English_Politics.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == ENVIRONMENT.lower():
            maxDict = English_Environment.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == TRAVEL.lower():
            maxDict = English_Travel.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == SCIENCE.lower():
            maxDict = English_Science.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == BUSINESS.lower():
            maxDict = English_Business.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == STOCKS.lower():
            maxDict = English_Stocks.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == FOOD.lower():
            maxDict = English_Food.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == FASHION.lower():
            maxDict = English_Fashion.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == MUMBAI.lower():
            maxDict = English_Mumbai.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == PUNE.lower():
            maxDict = English_Pune.objects.all().aggregate(Max('Cluster_Id'))


    elif lang.lower() == MARATHI.lower():
        
        if category.lower() == SPORTS.lower():
            maxDict = Marathi_Sports.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == TOP_STORIES.lower():
            maxDict = Marathi_Top_Stories.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == MAHARASHTRA.lower():
            maxDict = Marathi_Maharashtra.objects.all().aggregate(Max('Cluster_Id'))
        
        elif category.lower() == WORLD.lower():
            maxDict = Marathi_World.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == OPINION.lower():
            maxDict = Marathi_Opinion.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == HEALTH.lower():
            maxDict = Marathi_Health.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == LIFESTYLE.lower():
            maxDict = Marathi_Lifestyle.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == ENTERTAINMENT.lower():
            maxDict = Marathi_Entertainment.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == POLITICS.lower():
            maxDict = Marathi_Politics.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == ENVIRONMENT.lower():
            maxDict = Marathi_Environment.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == TRAVEL.lower():
            maxDict = Marathi_Travel.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == SCIENCE.lower():
            maxDict = Marathi_Science.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == BUSINESS.lower():
            maxDict = Marathi_Business.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == STOCKS.lower():
            maxDict = Marathi_Stocks.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == FASHION.lower():
            maxDict = Marathi_Fashion.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == MUMBAI.lower():
            maxDict = Marathi_Mumbai.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == PUNE.lower():
            maxDict = Marathi_Pune.objects.all().aggregate(Max('Cluster_Id'))
    
        elif category.lower() == NAGPUR.lower():
            maxDict = Marathi_Nagpur.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == NASIK.lower():
            maxDict = Marathi_Nasik.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == AURANGABAD.lower():
            maxDict = Marathi_Aurangabad.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == SOLAPUR.lower():
            maxDict = Marathi_Solapur.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == KOLHAPUR.lower():
            maxDict = Marathi_Kolhapur.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == SATARA.lower():
            maxDict = Marathi_Satara.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == SANGLI.lower():
            maxDict = Marathi_Sangli.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == AKOLA.lower():
            maxDict = Marathi_Akola.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == AHMEDNAGAR.lower():
            maxDict = Marathi_Ahmednagar.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == JALGAON.lower():
            maxDict = Marathi_Jalgaon.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == GOA.lower():
            maxDict = Marathi_Goa.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == CHANDRAPUR.lower():
            maxDict = Marathi_Chandrapur.objects.all().aggregate(Max('Cluster_Id'))
   
        elif category.lower() == WARDHA.lower():
            maxDict = Marathi_Wardha.objects.all().aggregate(Max('Cluster_Id'))

    #logger.info("Exited getMaxClusterId ")
    return maxDict

def insertLangCategoryTable(key, lang, category, articleObj, maxClusterId, isRep):
    #logger.info("Entered insertLangCategoryTable ")
    if lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = Hindi_Sports( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Hindi_Top_Stories( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = Hindi_World( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == OPINION.lower():
            langCategoryObj = Hindi_Opinion( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = Hindi_Health( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = Hindi_Lifestyle( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Hindi_Entertainment( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = Hindi_Technology( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == POLITICS.lower():
            langCategoryObj = Hindi_Politics( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = Hindi_Environment( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BOOKS.lower():
            langCategoryObj = Hindi_Books( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TRAVEL.lower():
            langCategoryObj = Hindi_Travel( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = Hindi_Science( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = Hindi_Business( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == STOCKS.lower():
            langCategoryObj = Hindi_Stocks( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = Hindi_Food( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == WEEKEND.lower():
            langCategoryObj = Hindi_Weekend( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = Hindi_Fashion( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == AUTO.lower():
            langCategoryObj = Hindi_Auto( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == CRIME.lower():
            langCategoryObj = Hindi_Crime( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == UTTARPRADESH.lower():
            langCategoryObj = Hindi_UttarPradesh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == UTTARAKHAND.lower():
            langCategoryObj = Hindi_Uttarakhand( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == HIMACHALPRADESH.lower():
            langCategoryObj = Hindi_HimachalPradesh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == DELHI.lower():
            langCategoryObj = Hindi_Delhi( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAMMUKASHMIR.lower():
            langCategoryObj = Hindi_JammuKashmir( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == PUNJAB.lower():
            langCategoryObj = Hindi_Punjab( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MADHYAPRADESH.lower():
            langCategoryObj = Hindi_MadhyaPradesh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JHARKHAND.lower():
            langCategoryObj = Hindi_Jharkhand( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BIHAR.lower():
            langCategoryObj = Hindi_Bihar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == HARYANA.lower():
            langCategoryObj = Hindi_Haryana( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == CHATTISGARH.lower():
            langCategoryObj = Hindi_Chattisgarh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == RAJASTHAN.lower():
            langCategoryObj = Hindi_Rajasthan( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == WESTBENGAL.lower():
            langCategoryObj = Hindi_WestBengal( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ORISSA.lower():
            langCategoryObj = Hindi_Orissa( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == GUJRAT.lower():
            langCategoryObj = Hindi_Gujrat( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MAHARASHTRA.lower():
            langCategoryObj = Hindi_Maharashtra( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == LUCKNOW.lower():
            langCategoryObj = Hindi_Lucknow( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ALLAHABAD.lower():
            langCategoryObj = Hindi_Allahabad( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == PRATAPGARH.lower():
            langCategoryObj = Hindi_Pratapgarh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == KANPUR.lower():
            langCategoryObj = Hindi_Kanpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MERATH.lower():
            langCategoryObj = Hindi_Merath( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == AGRA.lower():
            langCategoryObj = Hindi_Agra( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == NOIDA.lower():
            langCategoryObj = Hindi_Noida( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == GAZIABAD.lower():
            langCategoryObj = Hindi_Gaziabad( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BAGPAT.lower():
            langCategoryObj = Hindi_Bagpat( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SAHARNPUR.lower():
            langCategoryObj = Hindi_Saharnpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BULANDSHAHAR.lower():
            langCategoryObj = Hindi_Bulandshahar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == VARANASI.lower():
            langCategoryObj = Hindi_Varanasi( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == GORAKHPUR.lower():
            langCategoryObj = Hindi_Gorakhpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JHANSI.lower():
            langCategoryObj = Hindi_Jhansi( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MUZAFFARNAGAR.lower():
            langCategoryObj = Hindi_Muzaffarnagar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SITAPUR.lower():
            langCategoryObj = Hindi_Sitapur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAUNPUR.lower():
            langCategoryObj = Hindi_Jaunpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == AZAMGARH.lower():
            langCategoryObj = Hindi_Azamgarh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MORADABAD.lower():
            langCategoryObj = Hindi_Moradabad( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BAREILLY.lower():
            langCategoryObj = Hindi_Bareilly( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BALIA.lower():
            langCategoryObj = Hindi_Balia( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ALIGARH.lower():
            langCategoryObj = Hindi_Aligarh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MATHURA.lower():
            langCategoryObj = Hindi_Mathura( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHOPAL.lower():
            langCategoryObj = Hindi_Bhopal( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == INDORE.lower():
            langCategoryObj = Hindi_Indore( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == GWALIOR.lower():
            langCategoryObj = Hindi_Gwalior( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JABALPUR.lower():
            langCategoryObj = Hindi_Jabalpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == UJJAIN.lower():
            langCategoryObj = Hindi_Ujjain( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == RATLAM.lower():
            langCategoryObj = Hindi_Ratlam( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SAGAR.lower():
            langCategoryObj = Hindi_Sagar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == DEWAS.lower():
            langCategoryObj = Hindi_Dewas( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SATNA.lower():
            langCategoryObj = Hindi_Satna( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == REWA.lower():
            langCategoryObj = Hindi_Rewa( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == PATNA.lower():
            langCategoryObj = Hindi_Patna( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHAGALPUR.lower():
            langCategoryObj = Hindi_Bhagalpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MUJAFFARPUR.lower():
            langCategoryObj = Hindi_Mujaffarpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == GAYA.lower():
            langCategoryObj = Hindi_Gaya( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == DARBHANGA.lower():
            langCategoryObj = Hindi_Darbhanga( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == POORNIYA.lower():
            langCategoryObj = Hindi_Poorniya( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SEWAN.lower():
            langCategoryObj = Hindi_Sewan( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BEGUSARAI.lower():
            langCategoryObj = Hindi_Begusarai( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == KATIHAR.lower():
            langCategoryObj = Hindi_Katihar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAIPUR.lower():
            langCategoryObj = Hindi_Jaipur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == UDAIPUR.lower():
            langCategoryObj = Hindi_Udaipur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JODHPUR.lower():
            langCategoryObj = Hindi_Jodhpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == AJMER.lower():
            langCategoryObj = Hindi_Ajmer( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BIKANER.lower():
            langCategoryObj = Hindi_Bikaner( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ALWAR.lower():
            langCategoryObj = Hindi_Alwar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SIKAR.lower():
            langCategoryObj = Hindi_Sikar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == KOTA.lower():
            langCategoryObj = Hindi_Kota( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHILWARA.lower():
            langCategoryObj = Hindi_Bhilwara( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHARATPUR.lower():
            langCategoryObj = Hindi_Bharatpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == CHHATIS.lower():
            langCategoryObj = Hindi_Chhatis( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == RAIPUR.lower():
            langCategoryObj = Hindi_Raipur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHILAI.lower():
            langCategoryObj = Hindi_Bhilai( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == RAJNANDGAO.lower():
            langCategoryObj = Hindi_Rajnandgao( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == RAIGARH.lower():
            langCategoryObj = Hindi_Raigarh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAGDALPUR.lower():
            langCategoryObj = Hindi_Jagdalpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == KORVA.lower():
            langCategoryObj = Hindi_Korva( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == RANCHI.lower():
            langCategoryObj = Hindi_Ranchi( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == DHANBAD.lower():
            langCategoryObj = Hindi_Dhanbad( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAMSHEDPUR.lower():
            langCategoryObj = Hindi_Jamshedpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == GIRIDIHI.lower():
            langCategoryObj = Hindi_Giridihi( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == HAZARIBAGH.lower():
            langCategoryObj = Hindi_Hazaribagh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BOKARO.lower():
            langCategoryObj = Hindi_Bokaro( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == DEHRADUN.lower():
            langCategoryObj = Hindi_Dehradun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == NAINITAAL.lower():
            langCategoryObj = Hindi_Nainitaal( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == HARIDWAAR.lower():
            langCategoryObj = Hindi_Haridwaar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ALMORAH.lower():
            langCategoryObj = Hindi_Almorah( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == UDDHAMSINGHNAGAR.lower():
            langCategoryObj = Hindi_UddhamSinghNagar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SIMLA.lower():
            langCategoryObj = Hindi_Simla( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MANDI.lower():
            langCategoryObj = Hindi_Mandi( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BILASPUR.lower():
            langCategoryObj = Hindi_Bilaspur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == AMRITSAR.lower():
            langCategoryObj = Hindi_Amritsar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JALANDHAR.lower():
            langCategoryObj = Hindi_Jalandhar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == LUDHIANA.lower():
            langCategoryObj = Hindi_Ludhiana( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ROPARH.lower():
            langCategoryObj = Hindi_Roparh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == CHANDIGARH.lower():
            langCategoryObj = Hindi_Chandigarh( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ROHTAK.lower():
            langCategoryObj = Hindi_Rohtak( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == PANCHKULA.lower():
            langCategoryObj = Hindi_Panchkula( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == AMBALA.lower():
            langCategoryObj = Hindi_Ambala( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == PANIPAT.lower():
            langCategoryObj = Hindi_Panipat( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == GURGAON.lower():
            langCategoryObj = Hindi_Gurgaon( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == HISSAR.lower():
            langCategoryObj = Hindi_Hissar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAMMU.lower():
            langCategoryObj = Hindi_Jammu( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SRINAGAR.lower():
            langCategoryObj = Hindi_Srinagar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == POONCH.lower():
            langCategoryObj = Hindi_Poonch( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == KOLKATA.lower():
            langCategoryObj = Hindi_Kolkata( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == JALPAIGURHI.lower():
            langCategoryObj = Hindi_Jalpaigurhi( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == DARJEELING.lower():
            langCategoryObj = Hindi_Darjeeling( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ASANSOL.lower():
            langCategoryObj = Hindi_Asansol( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SILIGURHI.lower():
            langCategoryObj = Hindi_Siligurhi( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHUVANESHWAR.lower():
            langCategoryObj = Hindi_Bhuvaneshwar( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == PURI.lower():
            langCategoryObj = Hindi_Puri( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == CUTTACK.lower():
            langCategoryObj = Hindi_Cuttack( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == AHMEDABAD.lower():
            langCategoryObj = Hindi_Ahmedabad( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SURAT.lower():
            langCategoryObj = Hindi_Surat( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == VADODARA.lower():
            langCategoryObj = Hindi_Vadodara( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == MUMBAI.lower():
            langCategoryObj = Hindi_Mumbai( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == NAGPUR.lower():
            langCategoryObj = Hindi_Nagpur( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == PUNE.lower():
            langCategoryObj = Hindi_Pune( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()

    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            langCategoryObj = English_Economy(Article=articleObj,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=maxClusterId,
                                              Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = English_Sports(Article=articleObj,
                                             URL=articleObj.URL,
                                             Title=articleObj.Title,
                                             Summary=articleObj.Summary,
                                             Thumbnail=articleObj.Thumbnail,
                                             Source=articleObj.Source,
                                             Published_Date=articleObj.Published_Date,
                                             Cluster_Id=maxClusterId,
                                             Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = English_Top_Stories(Article=articleObj,
                                            URL=articleObj.URL,
                                            Title=articleObj.Title,
                                            Summary=articleObj.Summary,
                                            Thumbnail=articleObj.Thumbnail,
                                            Source=articleObj.Source,
                                            Published_Date=articleObj.Published_Date,
                                            Cluster_Id=maxClusterId,
                                            Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = English_World(Article=articleObj,
                                            URL=articleObj.URL,
                                            Title=articleObj.Title,
                                            Summary=articleObj.Summary,
                                            Thumbnail=articleObj.Thumbnail,
                                            Source=articleObj.Source,
                                            Published_Date=articleObj.Published_Date,
                                            Cluster_Id=maxClusterId,
                                            Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == OPINION.lower():
            langCategoryObj = English_Opinion(Article=articleObj,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=maxClusterId,
                                              Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = English_Health(Article=articleObj,
                                             URL=articleObj.URL,
                                             Title=articleObj.Title,
                                             Summary=articleObj.Summary,
                                             Thumbnail=articleObj.Thumbnail,
                                             Source=articleObj.Source,
                                             Published_Date=articleObj.Published_Date,
                                             Cluster_Id=maxClusterId,
                                             Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = English_Lifestyle(Article=articleObj,
                                                URL=articleObj.URL,
                                                Title=articleObj.Title,
                                                Summary=articleObj.Summary,
                                                Thumbnail=articleObj.Thumbnail,
                                                Source=articleObj.Source,
                                                Published_Date=articleObj.Published_Date,
                                                Cluster_Id=maxClusterId,
                                                Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = English_Entertainment(Article=articleObj,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=maxClusterId,
                                                    Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = English_Technology(Article=articleObj,
                                                 URL=articleObj.URL,
                                                 Title=articleObj.Title,
                                                 Summary=articleObj.Summary,
                                                 Thumbnail=articleObj.Thumbnail,
                                                 Source=articleObj.Source,
                                                 Published_Date=articleObj.Published_Date,
                                                 Cluster_Id=maxClusterId,
                                                 Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == POLITICS.lower():
            langCategoryObj = English_Politics(Article=articleObj,
                                               URL=articleObj.URL,
                                               Title=articleObj.Title,
                                               Summary=articleObj.Summary,
                                               Thumbnail=articleObj.Thumbnail,
                                               Source=articleObj.Source,
                                               Published_Date=articleObj.Published_Date,
                                               Cluster_Id=maxClusterId,
                                               Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = English_Environment(Article=articleObj,
                                                  URL=articleObj.URL,
                                                  Title=articleObj.Title,
                                                  Summary=articleObj.Summary,
                                                  Thumbnail=articleObj.Thumbnail,
                                                  Source=articleObj.Source,
                                                  Published_Date=articleObj.Published_Date,
                                                  Cluster_Id=maxClusterId,
                                                  Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BOOKS.lower():
            langCategoryObj = English_Books(Article=articleObj,
                                            URL=articleObj.URL,
                                            Title=articleObj.Title,
                                            Summary=articleObj.Summary,
                                            Thumbnail=articleObj.Thumbnail,
                                            Source=articleObj.Source,
                                            Published_Date=articleObj.Published_Date,
                                            Cluster_Id=maxClusterId,
                                            Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TRAVEL.lower():
            langCategoryObj = English_Travel(Article=articleObj,
                                             URL=articleObj.URL,
                                             Title=articleObj.Title,
                                             Summary=articleObj.Summary,
                                             Thumbnail=articleObj.Thumbnail,
                                             Source=articleObj.Source,
                                             Published_Date=articleObj.Published_Date,
                                             Cluster_Id=maxClusterId,
                                             Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = English_Science(Article=articleObj,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=maxClusterId,
                                              Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = English_Business(Article=articleObj,
                                               URL=articleObj.URL,
                                               Title=articleObj.Title,
                                               Summary=articleObj.Summary,
                                               Thumbnail=articleObj.Thumbnail,
                                               Source=articleObj.Source,
                                               Published_Date=articleObj.Published_Date,
                                               Cluster_Id=maxClusterId,
                                               Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == STOCKS.lower():
            langCategoryObj = English_Stocks(Article=articleObj,
                                             URL=articleObj.URL,
                                             Title=articleObj.Title,
                                             Summary=articleObj.Summary,
                                             Thumbnail=articleObj.Thumbnail,
                                             Source=articleObj.Source,
                                             Published_Date=articleObj.Published_Date,
                                             Cluster_Id=maxClusterId,
                                             Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = English_Food(Article=articleObj,
                                           URL=articleObj.URL,
                                           Title=articleObj.Title,
                                           Summary=articleObj.Summary,
                                           Thumbnail=articleObj.Thumbnail,
                                           Source=articleObj.Source,
                                           Published_Date=articleObj.Published_Date,
                                           Cluster_Id=maxClusterId,
                                           Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WEEKEND.lower():
            langCategoryObj = English_Weekend(Article=articleObj,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=maxClusterId,
                                              Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = English_Fashion(Article=articleObj,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=maxClusterId,
                                              Is_Rep=isRep)
            langCategoryObj.save()

    if lang.lower() == ENGLISH.lower():
        if category.lower() == MUMBAI.lower():
            langCategoryObj = English_Mumbai(Article=articleObj,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=maxClusterId,
                                              Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == PUNE.lower():
            langCategoryObj = English_Pune(Article=articleObj,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=maxClusterId,
                                              Is_Rep=isRep)
            langCategoryObj.save()

    if lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_economy
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SPORTS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_sports
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_top_stories
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == MAHARASHTRA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_maharashtra
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WORLD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_world
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == OPINION.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_opinion
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == HEALTH.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_health
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == LIFESTYLE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_lifestyle
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_entertainment
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_technology
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == POLITICS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_politics
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_environment
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == BOOKS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_books
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TRAVEL.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_travel
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SCIENCE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_science
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == BUSINESS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_business
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == STOCKS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_stocks
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == FOOD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_food
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WEEKEND.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_weekend
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == FASHION.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_fashion
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == MUMBAI.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_mumbai
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == PUNE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_pune
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == NAGPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_nagpur
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == NASIK.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_nasik
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AURANGABAD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_aurangabad
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SOLAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_solapur
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == KOLHAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_kolhapur
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SATARA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_satara
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SANGLI.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_sangli
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AKOLA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_akola
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AHMEDNAGAR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_ahmednagar
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == JALGAON.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_jalgaon
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == GOA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_goa
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == CHANDRAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_chandrapur
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WARDHA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name=category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_wardha
                          (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                           SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                           from news_schema.newsApp_news_article
                           WHERE Language_id = %s and Category_id = %s and id = %s''',
                           [maxClusterId, isRep, langObj.id, categoryObj.id, key])
    #logger.info("Exited insertLangCategoryTable ")

def insertLangCategoryRerunTable(key, lang, category, articleObj, maxClusterId, isRep):
    #logger.info("Entered insertLangCategoryRerunTable ")
    if lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = Hindi_Sports_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Hindi_Top_Stories_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = Hindi_World_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == OPINION.lower():
            langCategoryObj = Hindi_Opinion_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = Hindi_Health_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = Hindi_Lifestyle_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Hindi_Entertainment_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = Hindi_Technology_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == POLITICS.lower():
            langCategoryObj = Hindi_Politics_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = Hindi_Environment_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TRAVEL.lower():
            langCategoryObj = Hindi_Travel_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = Hindi_Science_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = Hindi_Business_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == STOCKS.lower():
            langCategoryObj = Hindi_Stocks_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = Hindi_Food_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == WEEKEND.lower():
            langCategoryObj = Hindi_Weekend_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = Hindi_Fashion_Rerun( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = maxClusterId,
                                        Is_Rep = isRep)
            langCategoryObj.save()

    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            langCategoryObj = English_Economy_Rerun(Article=articleObj,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=maxClusterId,
                                                    Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = English_Sports_Rerun(Article=articleObj,
                                                   URL=articleObj.URL,
                                                   Title=articleObj.Title,
                                                   Summary=articleObj.Summary,
                                                   Thumbnail=articleObj.Thumbnail,
                                                   Source=articleObj.Source,
                                                   Published_Date=articleObj.Published_Date,
                                                   Cluster_Id=maxClusterId,
                                                   Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = English_Top_Stories_Rerun(Article=articleObj,
                                                  URL=articleObj.URL,
                                                  Title=articleObj.Title,
                                                  Summary=articleObj.Summary,
                                                  Thumbnail=articleObj.Thumbnail,
                                                  Source=articleObj.Source,
                                                  Published_Date=articleObj.Published_Date,
                                                  Cluster_Id=maxClusterId,
                                                  Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = English_World_Rerun(Article=articleObj,
                                                  URL=articleObj.URL,
                                                  Title=articleObj.Title,
                                                  Summary=articleObj.Summary,
                                                  Thumbnail=articleObj.Thumbnail,
                                                  Source=articleObj.Source,
                                                  Published_Date=articleObj.Published_Date,
                                                  Cluster_Id=maxClusterId,
                                                  Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == OPINION.lower():
            langCategoryObj = English_Opinion_Rerun(Article=articleObj,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=maxClusterId,
                                                    Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = English_Health_Rerun(Article=articleObj,
                                                   URL=articleObj.URL,
                                                   Title=articleObj.Title,
                                                   Summary=articleObj.Summary,
                                                   Thumbnail=articleObj.Thumbnail,
                                                   Source=articleObj.Source,
                                                   Published_Date=articleObj.Published_Date,
                                                   Cluster_Id=maxClusterId,
                                                   Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = English_Lifestyle_Rerun(Article=articleObj,
                                                      URL=articleObj.URL,
                                                      Title=articleObj.Title,
                                                      Summary=articleObj.Summary,
                                                      Thumbnail=articleObj.Thumbnail,
                                                      Source=articleObj.Source,
                                                      Published_Date=articleObj.Published_Date,
                                                      Cluster_Id=maxClusterId,
                                                      Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = English_Entertainment_Rerun(Article=articleObj,
                                                          URL=articleObj.URL,
                                                          Title=articleObj.Title,
                                                          Summary=articleObj.Summary,
                                                          Thumbnail=articleObj.Thumbnail,
                                                          Source=articleObj.Source,
                                                          Published_Date=articleObj.Published_Date,
                                                          Cluster_Id=maxClusterId,
                                                          Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = English_Technology_Rerun(Article=articleObj,
                                                       URL=articleObj.URL,
                                                       Title=articleObj.Title,
                                                       Summary=articleObj.Summary,
                                                       Thumbnail=articleObj.Thumbnail,
                                                       Source=articleObj.Source,
                                                       Published_Date=articleObj.Published_Date,
                                                       Cluster_Id=maxClusterId,
                                                       Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == POLITICS.lower():
            langCategoryObj = English_Politics_Rerun(Article=articleObj,
                                                     URL=articleObj.URL,
                                                     Title=articleObj.Title,
                                                     Summary=articleObj.Summary,
                                                     Thumbnail=articleObj.Thumbnail,
                                                     Source=articleObj.Source,
                                                     Published_Date=articleObj.Published_Date,
                                                     Cluster_Id=maxClusterId,
                                                     Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = English_Environment_Rerun(Article=articleObj,
                                                        URL=articleObj.URL,
                                                        Title=articleObj.Title,
                                                        Summary=articleObj.Summary,
                                                        Thumbnail=articleObj.Thumbnail,
                                                        Source=articleObj.Source,
                                                        Published_Date=articleObj.Published_Date,
                                                        Cluster_Id=maxClusterId,
                                                        Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BOOKS.lower():
            langCategoryObj = English_Books_Rerun(Article=articleObj,
                                                  URL=articleObj.URL,
                                                  Title=articleObj.Title,
                                                  Summary=articleObj.Summary,
                                                  Thumbnail=articleObj.Thumbnail,
                                                  Source=articleObj.Source,
                                                  Published_Date=articleObj.Published_Date,
                                                  Cluster_Id=maxClusterId,
                                                  Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TRAVEL.lower():
            langCategoryObj = English_Travel_Rerun(Article=articleObj,
                                                   URL=articleObj.URL,
                                                   Title=articleObj.Title,
                                                   Summary=articleObj.Summary,
                                                   Thumbnail=articleObj.Thumbnail,
                                                   Source=articleObj.Source,
                                                   Published_Date=articleObj.Published_Date,
                                                   Cluster_Id=maxClusterId,
                                                   Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = English_Science_Rerun(Article=articleObj,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=maxClusterId,
                                                    Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = English_Business_Rerun(Article=articleObj,
                                                     URL=articleObj.URL,
                                                     Title=articleObj.Title,
                                                     Summary=articleObj.Summary,
                                                     Thumbnail=articleObj.Thumbnail,
                                                     Source=articleObj.Source,
                                                     Published_Date=articleObj.Published_Date,
                                                     Cluster_Id=maxClusterId,
                                                     Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == STOCKS.lower():
            langCategoryObj = English_Stocks_Rerun(Article=articleObj,
                                                   URL=articleObj.URL,
                                                   Title=articleObj.Title,
                                                   Summary=articleObj.Summary,
                                                   Thumbnail=articleObj.Thumbnail,
                                                   Source=articleObj.Source,
                                                   Published_Date=articleObj.Published_Date,
                                                   Cluster_Id=maxClusterId,
                                                   Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = English_Food_Rerun(Article=articleObj,
                                                 URL=articleObj.URL,
                                                 Title=articleObj.Title,
                                                 Summary=articleObj.Summary,
                                                 Thumbnail=articleObj.Thumbnail,
                                                 Source=articleObj.Source,
                                                 Published_Date=articleObj.Published_Date,
                                                 Cluster_Id=maxClusterId,
                                                 Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WEEKEND.lower():
            langCategoryObj = English_Weekend_Rerun(Article=articleObj,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=maxClusterId,
                                                    Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = English_Fashion_Rerun(Article=articleObj,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=maxClusterId,
                                                    Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == MUMBAI.lower():
            langCategoryObj = English_Mumbai_Rerun(Article=articleObj,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=maxClusterId,
                                                    Is_Rep=isRep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == PUNE.lower():
            langCategoryObj = English_Pune_Rerun(Article=articleObj,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=maxClusterId,
                                                    Is_Rep=isRep)
            langCategoryObj.save()

    if lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_economy_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SPORTS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_sports_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_top_stories_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WORLD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_world_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == OPINION.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_opinion_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == HEALTH.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_health_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == LIFESTYLE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_lifestyle_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_entertainment_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_technology_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == POLITICS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_politics_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_environment_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == BOOKS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_books_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TRAVEL.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_travel_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SCIENCE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_science_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == BUSINESS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_business_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == STOCKS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_stocks_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == FOOD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_food_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WEEKEND.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_weekend_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == FASHION.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_fashion_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == MUMBAI.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_mumbai_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == PUNE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_pune_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == NAGPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_nagpur_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == NASIK.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_nasik_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AURANGABAD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_aurangabad_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SOLAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_solapur_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == KOLHAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_kolhapur_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SATARA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_satara_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SANGLI.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_sangli_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AKOLA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_akola_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AHMEDNAGAR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_ahmednagar_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == JALGAON.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_jalgaon_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == GOA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_goa_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == CHANDRAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_chandrapur_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WARDHA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_wardha_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    if lang.lower() == MARATHI.lower():
        if category.lower() == MAHARASHTRA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_maharashtra_rerun
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,TITLE,SUMMARY,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[maxClusterId,isRep,langObj.id,categoryObj.id,key])
    #logger.info("Exited insertLangCategoryRerunTable ")

def selectLangCategoryTable(lang, category, URL):
    #logger.info("Entered selectLangCategoryTable ")

    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            try:
                langCategoryObj = English_Economy.objects.get(URL=URL)
                return 1
            except English_Economy.DoesNotExist:
                return 0
    
        elif category.lower() == SPORTS.lower():
            try:
                langCategoryObj = English_Sports.objects.get(URL=URL)
                return 1
            except English_Sports.DoesNotExist:
                return 0
    
        elif category.lower() == TOP_STORIES.lower():
            try:
                langCategoryObj = English_Top_Stories.objects.get(URL=URL)
                return 1
            except English_Top_Stories.DoesNotExist:
                return 0
    
        elif category.lower() == WORLD.lower():
            try:
                langCategoryObj = English_World.objects.get(URL=URL)
                return 1
            except English_World.DoesNotExist:
                return 0
    
        elif category.lower() == OPINION.lower():
            try:
                langCategoryObj = English_Opinion.objects.get(URL=URL)
                return 1
            except English_Opinion.DoesNotExist:
                return 0
    
        elif category.lower() == HEALTH.lower():
            try:
                langCategoryObj = English_Health.objects.get(URL=URL)
                return 1
            except English_Health.DoesNotExist:
                return 0
    
        elif category.lower() == LIFESTYLE.lower():
            try:
                langCategoryObj = English_Lifestyle.objects.get(URL=URL)
                return 1
            except English_Lifestyle.DoesNotExist:
                return 0
    
        elif category.lower() == ENTERTAINMENT.lower():
            try:
                langCategoryObj = English_Entertainment.objects.get(URL=URL)
                return 1
            except English_Entertainment.DoesNotExist:
                return 0
    
        elif category.lower() == TECHNOLOGY.lower():
            try:
                langCategoryObj = English_Technology.objects.get(URL=URL)
                return 1
            except English_Technology.DoesNotExist:
                return 0
    
        elif category.lower() == POLITICS.lower():
            try:
                langCategoryObj = English_Politics.objects.get(URL=URL)
                return 1
            except English_Politics.DoesNotExist:
                return 0
    
        elif category.lower() == ENVIRONMENT.lower():
            try:
                langCategoryObj = English_Environment.objects.get(URL=URL)
                return 1
            except English_Environment.DoesNotExist:
                return 0
    
        elif category.lower() == BOOKS.lower():
            try:
                langCategoryObj = English_Books.objects.get(URL=URL)
                return 1
            except English_Books.DoesNotExist:
                return 0
    
        elif category.lower() == TRAVEL.lower():
            try:
                langCategoryObj = English_Travel.objects.get(URL=URL)
                return 1
            except English_Travel.DoesNotExist:
                return 0
    
        elif category.lower() == SCIENCE.lower():
            try:
                langCategoryObj = English_Science.objects.get(URL=URL)
                return 1
            except English_Science.DoesNotExist:
                return 0
    
        elif category.lower() == BUSINESS.lower():
            try:
                langCategoryObj = English_Business.objects.get(URL=URL)
                return 1
            except English_Business.DoesNotExist:
                return 0
    
        elif category.lower() == STOCKS.lower():
            try:
                langCategoryObj = English_Stocks.objects.get(URL=URL)
                return 1
            except English_Stocks.DoesNotExist:
                return 0
    
        elif category.lower() == FOOD.lower():
            try:
                langCategoryObj = English_Food.objects.get(URL=URL)
                return 1
            except English_Food.DoesNotExist:
                return 0
    
    
        elif category.lower() == FASHION.lower():
            try:
                langCategoryObj = English_Fashion.objects.get(URL=URL)
                return 1
            except English_Fashion.DoesNotExist:
                return 0
    
        elif category.lower() == MUMBAI.lower():
            try:
                langCategoryObj = English_Mumbai.objects.get(URL=URL)
                return 1
            except English_Mumbai.DoesNotExist:
                return 0
    
        elif category.lower() == PUNE.lower():
            try:
                langCategoryObj = English_Pune.objects.get(URL=URL)
                return 1
            except English_Pune.DoesNotExist:
                return 0

    elif lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            try:
                langCategoryObj = Marathi_Economy.objects.get(URL=URL)
                return 1
            except Marathi_Economy.DoesNotExist:
                return 0
    
        elif category.lower() == SPORTS.lower():
            try:
                langCategoryObj = Marathi_Sports.objects.get(URL=URL)
                return 1
            except Marathi_Sports.DoesNotExist:
                return 0
    
        elif category.lower() == TOP_STORIES.lower():
            try:
                langCategoryObj = Marathi_Top_Stories.objects.get(URL=URL)
                return 1
            except Marathi_Top_Stories.DoesNotExist:
                return 0
    
        elif category.lower() == MAHARASHTRA.lower():
            try:
                langCategoryObj = Marathi_Maharashtra.objects.get(URL=URL)
                return 1
            except Marathi_Maharashtra.DoesNotExist:
                return 0

    
        elif category.lower() == WORLD.lower():
            try:
                langCategoryObj = Marathi_World.objects.get(URL=URL)
                return 1
            except Marathi_World.DoesNotExist:
                return 0
    
        elif category.lower() == OPINION.lower():
            try:
                langCategoryObj = Marathi_Opinion.objects.get(URL=URL)
                return 1
            except Marathi_Opinion.DoesNotExist:
                return 0
    
        elif category.lower() == HEALTH.lower():
            try:
                langCategoryObj = Marathi_Health.objects.get(URL=URL)
                return 1
            except Marathi_Health.DoesNotExist:
                return 0
    
        elif category.lower() == LIFESTYLE.lower():
            try:
                langCategoryObj = Marathi_Lifestyle.objects.get(URL=URL)
                return 1
            except Marathi_Lifestyle.DoesNotExist:
                return 0
    
        elif category.lower() == ENTERTAINMENT.lower():
            try:
                langCategoryObj = Marathi_Entertainment.objects.get(URL=URL)
                return 1
            except Marathi_Entertainment.DoesNotExist:
                return 0
    
        elif category.lower() == TECHNOLOGY.lower():
            try:
                langCategoryObj = Marathi_Technology.objects.get(URL=URL)
                return 1
            except Marathi_Technology.DoesNotExist:
                return 0
    
        elif category.lower() == POLITICS.lower():
            try:
                langCategoryObj = Marathi_Politics.objects.get(URL=URL)
                return 1
            except Marathi_Politics.DoesNotExist:
                return 0
    
        elif category.lower() == ENVIRONMENT.lower():
            try:
                langCategoryObj = Marathi_Environment.objects.get(URL=URL)
                return 1
            except Marathi_Environment.DoesNotExist:
                return 0
    
        elif category.lower() == TRAVEL.lower():
            try:
                langCategoryObj = Marathi_Travel.objects.get(URL=URL)
                return 1
            except Marathi_Travel.DoesNotExist:
                return 0
    
        elif category.lower() == SCIENCE.lower():
            try:
                langCategoryObj = Marathi_Science.objects.get(URL=URL)
                return 1
            except Marathi_Science.DoesNotExist:
                return 0
    
        elif category.lower() == BUSINESS.lower():
            try:
                langCategoryObj = Marathi_Business.objects.get(URL=URL)
                return 1
            except Marathi_Business.DoesNotExist:
                return 0
    
        elif category.lower() == STOCKS.lower():
            try:
                langCategoryObj = Marathi_Stocks.objects.get(URL=URL)
                return 1
            except Marathi_Stocks.DoesNotExist:
                return 0
    
        elif category.lower() == FOOD.lower():
            try:
                langCategoryObj = Marathi_Food.objects.get(URL=URL)
                return 1
            except Marathi_Food.DoesNotExist:
                return 0
    
    
        elif category.lower() == FASHION.lower():
            try:
                langCategoryObj = Marathi_Fashion.objects.get(URL=URL)
                return 1
            except Marathi_Fashion.DoesNotExist:
                return 0
    
        elif category.lower() == MUMBAI.lower():
            try:
                langCategoryObj = Marathi_Mumbai.objects.get(URL=URL)
                return 1
            except Marathi_Mumbai.DoesNotExist:
                return 0
    
        elif category.lower() == PUNE.lower():
            try:
                langCategoryObj = Marathi_Pune.objects.get(URL=URL)
                return 1
            except Marathi_Pune.DoesNotExist:
                return 0
    
        elif category.lower() == NAGPUR.lower():
            try:
                langCategoryObj = Marathi_Nagpur.objects.get(URL=URL)
                return 1
            except Marathi_Nagpur.DoesNotExist:
                return 0
    
        elif category.lower() == NASIK.lower():
            try:
                langCategoryObj = Marathi_Nasik.objects.get(URL=URL)
                return 1
            except Marathi_Nasik.DoesNotExist:
                return 0
    
        elif category.lower() == AURANGABAD.lower():
            try:
                langCategoryObj = Marathi_Aurangabad.objects.get(URL=URL)
                return 1
            except Marathi_Aurangabad.DoesNotExist:
                return 0
    
        elif category.lower() == SOLAPUR.lower():
            try:
                langCategoryObj = Marathi_Solapur.objects.get(URL=URL)
                return 1
            except Marathi_Solapur.DoesNotExist:
                return 0
    
        elif category.lower() == KOLHAPUR.lower():
            try:
                langCategoryObj = Marathi_Kolhapur.objects.get(URL=URL)
                return 1
            except Marathi_Kolhapur.DoesNotExist:
                return 0
    
        elif category.lower() == SATARA.lower():
            try:
                langCategoryObj = Marathi_Satara.objects.get(URL=URL)
                return 1
            except Marathi_Satara.DoesNotExist:
                return 0
    
        elif category.lower() == SANGLI.lower():
            try:
                langCategoryObj = Marathi_Sangli.objects.get(URL=URL)
                return 1
            except Marathi_Sangli.DoesNotExist:
                return 0
    
        elif category.lower() == AKOLA.lower():
            try:
                langCategoryObj = Marathi_Akola.objects.get(URL=URL)
                return 1
            except Marathi_Akola.DoesNotExist:
                return 0
    
        elif category.lower() == AHMEDNAGAR.lower():
            try:
                langCategoryObj = Marathi_Ahmednagar.objects.get(URL=URL)
                return 1
            except Marathi_Ahmednagar.DoesNotExist:
                return 0
    
        elif category.lower() == JALGAON.lower():
            try:
                langCategoryObj = Marathi_Jalgaon.objects.get(URL=URL)
                return 1
            except Marathi_Jalgaon.DoesNotExist:
                return 0
    
        elif category.lower() == GOA.lower():
            try:
                langCategoryObj = Marathi_Goa.objects.get(URL=URL)
                return 1
            except Marathi_Goa.DoesNotExist:
                return 0
    
        elif category.lower() == CHANDRAPUR.lower():
            try:
                langCategoryObj = Marathi_Chandrapur.objects.get(URL=URL)
                return 1
            except Marathi_Chandrapur.DoesNotExist:
                return 0
    
        elif category.lower() == WARDHA.lower():
            try:
                langCategoryObj = Marathi_Wardha.objects.get(URL=URL)
                return 1
            except Marathi_Wardha.DoesNotExist:
                return 0
    elif lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            try:
                langCategoryObj = Hindi_Sports.objects.get(URL = URL)
                return True
            except Hindi_Sports.DoesNotExist:
                return False
        if category.lower() == TOP_STORIES.lower():
            try:
                langCategoryObj = Hindi_Top_Stories.objects.get(URL = URL)
                return True
            except Hindi_Top_Stories.DoesNotExist:
                return False
        if category.lower() == WORLD.lower():
            try:
                langCategoryObj = Hindi_World.objects.get(URL = URL)
                return True
            except Hindi_World.DoesNotExist:
                return False
        if category.lower() == OPINION.lower():
            try:
                langCategoryObj = Hindi_Opinion.objects.get(URL = URL)
                return True
            except Hindi_Opinion.DoesNotExist:
                return False
        if category.lower() == HEALTH.lower():
            try:
                langCategoryObj = Hindi_Health.objects.get(URL = URL)
                return True
            except Hindi_Health.DoesNotExist:
                return False
        if category.lower() == LIFESTYLE.lower():
            try:
                langCategoryObj = Hindi_Lifestyle.objects.get(URL = URL)
                return True
            except Hindi_Lifestyle.DoesNotExist:
                return False
        if category.lower() == ENTERTAINMENT.lower():
            try:
                langCategoryObj = Hindi_Entertainment.objects.get(URL = URL)
                return True
            except Hindi_Entertainment.DoesNotExist:
                return False
        if category.lower() == TECHNOLOGY.lower():
            try:
                langCategoryObj = Hindi_Technology.objects.get(URL = URL)
                return True
            except Hindi_Technology.DoesNotExist:
                return False
        if category.lower() == POLITICS.lower():
            try:
                langCategoryObj = Hindi_Politics.objects.get(URL = URL)
                return True
            except Hindi_Politics.DoesNotExist:
                return False
        if category.lower() == ENVIRONMENT.lower():
            try:
                langCategoryObj = Hindi_Environment.objects.get(URL = URL)
                return True
            except Hindi_Environment.DoesNotExist:
                return False
        if category.lower() == BOOKS.lower():
            try:
                langCategoryObj = Hindi_Books.objects.get(URL = URL)
                return True
            except Hindi_Books.DoesNotExist:
                return False
        if category.lower() == TRAVEL.lower():
            try:
                langCategoryObj = Hindi_Travel.objects.get(URL = URL)
                return True
            except Hindi_Travel.DoesNotExist:
                return False
        if category.lower() == SCIENCE.lower():
            try:
                langCategoryObj = Hindi_Science.objects.get(URL = URL)
                return True
            except Hindi_Science.DoesNotExist:
                return False
        if category.lower() == BUSINESS.lower():
            try:
                langCategoryObj = Hindi_Business.objects.get(URL = URL)
                return True
            except Hindi_Business.DoesNotExist:
                return False
        if category.lower() == STOCKS.lower():
            try:
                langCategoryObj = Hindi_Stocks.objects.get(URL = URL)
                return True
            except Hindi_Stocks.DoesNotExist:
                return False
        if category.lower() == FOOD.lower():
            try:
                langCategoryObj = Hindi_Food.objects.get(URL = URL)
                return True
            except Hindi_Food.DoesNotExist:
                return False
        if category.lower() == WEEKEND.lower():
            try:
                langCategoryObj = Hindi_Weekend.objects.get(URL = URL)
                return True
            except Hindi_Weekend.DoesNotExist:
                return False
        if category.lower() == FASHION.lower():
            try:
                langCategoryObj = Hindi_Fashion.objects.get(URL = URL)
                return True
            except Hindi_Fashion.DoesNotExist:
                return False
        if category.lower() == CRIME.lower():
            try:
                langCategoryObj = Hindi_Crime.objects.get(URL = URL)
                return True
            except Hindi_Crime.DoesNotExist:
                return False
        if category.lower() == AUTO.lower():
            try:
                langCategoryObj = Hindi_Auto.objects.get(URL = URL)
                return True
            except Hindi_Auto.DoesNotExist:
                return False
        if category.lower() == UTTARPRADESH.lower():
            try:
                langCategoryObj = Hindi_UttarPradesh.objects.get(URL = URL)
                return True
            except Hindi_UttarPradesh.DoesNotExist:
                return False
        if category.lower() == UTTARAKHAND.lower():
            try:
                langCategoryObj = Hindi_Uttarakhand.objects.get(URL = URL)
                return True
            except Hindi_Uttarakhand.DoesNotExist:
                return False
        if category.lower() == HIMACHALPRADESH.lower():
            try:
                langCategoryObj = Hindi_HimachalPradesh.objects.get(URL = URL)
                return True
            except Hindi_HimachalPradesh.DoesNotExist:
                return False
        if category.lower() == DELHI.lower():
            try:
                langCategoryObj = Hindi_Delhi.objects.get(URL = URL)
                return True
            except Hindi_Delhi.DoesNotExist:
                return False
        if category.lower() == JAMMUKASHMIR.lower():
            try:
                langCategoryObj = Hindi_JammuKashmir.objects.get(URL = URL)
                return True
            except Hindi_JammuKashmir.DoesNotExist:
                return False
        if category.lower() == PUNJAB.lower():
            try:
                langCategoryObj = Hindi_Punjab.objects.get(URL = URL)
                return True
            except Hindi_Punjab.DoesNotExist:
                return False
        if category.lower() == MADHYAPRADESH.lower():
            try:
                langCategoryObj = Hindi_MadhyaPradesh.objects.get(URL = URL)
                return True
            except Hindi_MadhyaPradesh.DoesNotExist:
                return False
        if category.lower() == JHARKHAND.lower():
            try:
                langCategoryObj = Hindi_Jharkhand.objects.get(URL = URL)
                return True
            except Hindi_Jharkhand.DoesNotExist:
                return False
        if category.lower() == BIHAR.lower():
            try:
                langCategoryObj = Hindi_Bihar.objects.get(URL = URL)
                return True
            except Hindi_Bihar.DoesNotExist:
                return False
        if category.lower() == HARYANA.lower():
            try:
                langCategoryObj = Hindi_Haryana.objects.get(URL = URL)
                return True
            except Hindi_Haryana.DoesNotExist:
                return False
        if category.lower() == CHATTISGARH.lower():
            try:
                langCategoryObj = Hindi_Chattisgarh.objects.get(URL = URL)
                return True
            except Hindi_Chattisgarh.DoesNotExist:
                return False
        if category.lower() == RAJASTHAN.lower():
            try:
                langCategoryObj = Hindi_Rajasthan.objects.get(URL = URL)
                return True
            except Hindi_Rajasthan.DoesNotExist:
                return False
        if category.lower() == WESTBENGAL.lower():
            try:
                langCategoryObj = Hindi_WestBengal.objects.get(URL = URL)
                return True
            except Hindi_WestBengal.DoesNotExist:
                return False
        if category.lower() == ORISSA.lower():
            try:
                langCategoryObj = Hindi_Orissa.objects.get(URL = URL)
                return True
            except Hindi_Orissa.DoesNotExist:
                return False
        if category.lower() == GUJRAT.lower():
            try:
                langCategoryObj = Hindi_Gujrat.objects.get(URL = URL)
                return True
            except Hindi_Gujrat.DoesNotExist:
                return False
        if category.lower() == MAHARASHTRA.lower():
            try:
                langCategoryObj = Hindi_Maharashtra.objects.get(URL = URL)
                return True
            except Hindi_Maharashtra.DoesNotExist:
                return False
        if category.lower() == LUCKNOW.lower():
            try:
                langCategoryObj = Hindi_Lucknow.objects.get(URL = URL)
                return True
            except Hindi_Lucknow.DoesNotExist:
                return False
        if category.lower() == ALLAHABAD.lower():
            try:
                langCategoryObj = Hindi_Allahabad.objects.get(URL = URL)
                return True
            except Hindi_Allahabad.DoesNotExist:
                return False
        if category.lower() == PRATAPGARH.lower():
            try:
                langCategoryObj = Hindi_Pratapgarh.objects.get(URL = URL)
                return True
            except Hindi_Pratapgarh.DoesNotExist:
                return False
        if category.lower() == KANPUR.lower():
            try:
                langCategoryObj = Hindi_Kanpur.objects.get(URL = URL)
                return True
            except Hindi_Kanpur.DoesNotExist:
                return False
        if category.lower() == MERATH.lower():
            try:
                langCategoryObj = Hindi_Merath.objects.get(URL = URL)
                return True
            except Hindi_Merath.DoesNotExist:
                return False
        if category.lower() == AGRA.lower():
            try:
                langCategoryObj = Hindi_Agra.objects.get(URL = URL)
                return True
            except Hindi_Agra.DoesNotExist:
                return False
        if category.lower() == NOIDA.lower():
            try:
                langCategoryObj = Hindi_Noida.objects.get(URL = URL)
                return True
            except Hindi_Noida.DoesNotExist:
                return False
        if category.lower() == GAZIABAD.lower():
            try:
                langCategoryObj = Hindi_Gaziabad.objects.get(URL = URL)
                return True
            except Hindi_Gaziabad.DoesNotExist:
                return False
        if category.lower() == BAGPAT.lower():
            try:
                langCategoryObj = Hindi_Bagpat.objects.get(URL = URL)
                return True
            except Hindi_Bagpat.DoesNotExist:
                return False
        if category.lower() == SAHARNPUR.lower():
            try:
                langCategoryObj = Hindi_Saharnpur.objects.get(URL = URL)
                return True
            except Hindi_Saharnpur.DoesNotExist:
                return False
        if category.lower() == BULANDSHAHAR.lower():
            try:
                langCategoryObj = Hindi_Bulandshahar.objects.get(URL = URL)
                return True
            except Hindi_Bulandshahar.DoesNotExist:
                return False
        if category.lower() == VARANASI.lower():
            try:
                langCategoryObj = Hindi_Varanasi.objects.get(URL = URL)
                return True
            except Hindi_Varanasi.DoesNotExist:
                return False
        if category.lower() == GORAKHPUR.lower():
            try:
                langCategoryObj = Hindi_Gorakhpur.objects.get(URL = URL)
                return True
            except Hindi_Gorakhpur.DoesNotExist:
                return False
        if category.lower() == JHANSI.lower():
            try:
                langCategoryObj = Hindi_Jhansi.objects.get(URL = URL)
                return True
            except Hindi_Jhansi.DoesNotExist:
                return False
        if category.lower() == MUZAFFARNAGAR.lower():
            try:
                langCategoryObj = Hindi_Muzaffarnagar.objects.get(URL = URL)
                return True
            except Hindi_Muzaffarnagar.DoesNotExist:
                return False
        if category.lower() == SITAPUR.lower():
            try:
                langCategoryObj = Hindi_Sitapur.objects.get(URL = URL)
                return True
            except Hindi_Sitapur.DoesNotExist:
                return False
        if category.lower() == JAUNPUR.lower():
            try:
                langCategoryObj = Hindi_Jaunpur.objects.get(URL = URL)
                return True
            except Hindi_Jaunpur.DoesNotExist:
                return False
        if category.lower() == AZAMGARH.lower():
            try:
                langCategoryObj = Hindi_Azamgarh.objects.get(URL = URL)
                return True
            except Hindi_Azamgarh.DoesNotExist:
                return False
        if category.lower() == MORADABAD.lower():
            try:
                langCategoryObj = Hindi_Moradabad.objects.get(URL = URL)
                return True
            except Hindi_Moradabad.DoesNotExist:
                return False
        if category.lower() == BAREILLY.lower():
            try:
                langCategoryObj = Hindi_Bareilly.objects.get(URL = URL)
                return True
            except Hindi_Bareilly.DoesNotExist:
                return False
        if category.lower() == BALIA.lower():
            try:
                langCategoryObj = Hindi_Balia.objects.get(URL = URL)
                return True
            except Hindi_Balia.DoesNotExist:
                return False
        if category.lower() == ALIGARH.lower():
            try:
                langCategoryObj = Hindi_Aligarh.objects.get(URL = URL)
                return True
            except Hindi_Aligarh.DoesNotExist:
                return False
        if category.lower() == MATHURA.lower():
            try:
                langCategoryObj = Hindi_Mathura.objects.get(URL = URL)
                return True
            except Hindi_Mathura.DoesNotExist:
                return False
        if category.lower() == BHOPAL.lower():
            try:
                langCategoryObj = Hindi_Bhopal.objects.get(URL = URL)
                return True
            except Hindi_Bhopal.DoesNotExist:
                return False
        if category.lower() == INDORE.lower():
            try:
                langCategoryObj = Hindi_Indore.objects.get(URL = URL)
                return True
            except Hindi_Indore.DoesNotExist:
                return False
        if category.lower() == GWALIOR.lower():
            try:
                langCategoryObj = Hindi_Gwalior.objects.get(URL = URL)
                return True
            except Hindi_Gwalior.DoesNotExist:
                return False
        if category.lower() == JABALPUR.lower():
            try:
                langCategoryObj = Hindi_Jabalpur.objects.get(URL = URL)
                return True
            except Hindi_Jabalpur.DoesNotExist:
                return False
        if category.lower() == UJJAIN.lower():
            try:
                langCategoryObj = Hindi_Ujjain.objects.get(URL = URL)
                return True
            except Hindi_Ujjain.DoesNotExist:
                return False
        if category.lower() == RATLAM.lower():
            try:
                langCategoryObj = Hindi_Ratlam.objects.get(URL = URL)
                return True
            except Hindi_Ratlam.DoesNotExist:
                return False
        if category.lower() == SAGAR.lower():
            try:
                langCategoryObj = Hindi_Sagar.objects.get(URL = URL)
                return True
            except Hindi_Sagar.DoesNotExist:
                return False
        if category.lower() == DEWAS.lower():
            try:
                langCategoryObj = Hindi_Dewas.objects.get(URL = URL)
                return True
            except Hindi_Dewas.DoesNotExist:
                return False
        if category.lower() == SATNA.lower():
            try:
                langCategoryObj = Hindi_Satna.objects.get(URL = URL)
                return True
            except Hindi_Satna.DoesNotExist:
                return False
        if category.lower() == REWA.lower():
            try:
                langCategoryObj = Hindi_Rewa.objects.get(URL = URL)
                return True
            except Hindi_Rewa.DoesNotExist:
                return False
        if category.lower() == PATNA.lower():
            try:
                langCategoryObj = Hindi_Patna.objects.get(URL = URL)
                return True
            except Hindi_Patna.DoesNotExist:
                return False
        if category.lower() == BHAGALPUR.lower():
            try:
                langCategoryObj = Hindi_Bhagalpur.objects.get(URL = URL)
                return True
            except Hindi_Bhagalpur.DoesNotExist:
                return False
        if category.lower() == MUJAFFARPUR.lower():
            try:
                langCategoryObj = Hindi_Mujaffarpur.objects.get(URL = URL)
                return True
            except Hindi_Mujaffarpur.DoesNotExist:
                return False
        if category.lower() == GAYA.lower():
            try:
                langCategoryObj = Hindi_Gaya.objects.get(URL = URL)
                return True
            except Hindi_Gaya.DoesNotExist:
                return False
        if category.lower() == DARBHANGA.lower():
            try:
                langCategoryObj = Hindi_Darbhanga.objects.get(URL = URL)
                return True
            except Hindi_Darbhanga.DoesNotExist:
                return False
        if category.lower() == POORNIYA.lower():
            try:
                langCategoryObj = Hindi_Poorniya.objects.get(URL = URL)
                return True
            except Hindi_Poorniya.DoesNotExist:
                return False
        if category.lower() == SEWAN.lower():
            try:
                langCategoryObj = Hindi_Sewan.objects.get(URL = URL)
                return True
            except Hindi_Sewan.DoesNotExist:
                return False
        if category.lower() == BEGUSARAI.lower():
            try:
                langCategoryObj = Hindi_Begusarai.objects.get(URL = URL)
                return True
            except Hindi_Begusarai.DoesNotExist:
                return False
        if category.lower() == KATIHAR.lower():
            try:
                langCategoryObj = Hindi_Katihar.objects.get(URL = URL)
                return True
            except Hindi_Katihar.DoesNotExist:
                return False
        if category.lower() == JAIPUR.lower():
            try:
                langCategoryObj = Hindi_Jaipur.objects.get(URL = URL)
                return True
            except Hindi_Jaipur.DoesNotExist:
                return False
        if category.lower() == UDAIPUR.lower():
            try:
                langCategoryObj = Hindi_Udaipur.objects.get(URL = URL)
                return True
            except Hindi_Udaipur.DoesNotExist:
                return False
        if category.lower() == JODHPUR.lower():
            try:
                langCategoryObj = Hindi_Jodhpur.objects.get(URL = URL)
                return True
            except Hindi_Jodhpur.DoesNotExist:
                return False
        if category.lower() == AJMER.lower():
            try:
                langCategoryObj = Hindi_Ajmer.objects.get(URL = URL)
                return True
            except Hindi_Ajmer.DoesNotExist:
                return False
        if category.lower() == BIKANER.lower():
            try:
                langCategoryObj = Hindi_Bikaner.objects.get(URL = URL)
                return True
            except Hindi_Bikaner.DoesNotExist:
                return False
        if category.lower() == ALWAR.lower():
            try:
                langCategoryObj = Hindi_Alwar.objects.get(URL = URL)
                return True
            except Hindi_Alwar.DoesNotExist:
                return False
        if category.lower() == SIKAR.lower():
            try:
                langCategoryObj = Hindi_Sikar.objects.get(URL = URL)
                return True
            except Hindi_Sikar.DoesNotExist:
                return False
        if category.lower() == KOTA.lower():
            try:
                langCategoryObj = Hindi_Kota.objects.get(URL = URL)
                return True
            except Hindi_Kota.DoesNotExist:
                return False
        if category.lower() == BHILWARA.lower():
            try:
                langCategoryObj = Hindi_Bhilwara.objects.get(URL = URL)
                return True
            except Hindi_Bhilwara.DoesNotExist:
                return False
        if category.lower() == BHARATPUR.lower():
            try:
                langCategoryObj = Hindi_Bharatpur.objects.get(URL = URL)
                return True
            except Hindi_Bharatpur.DoesNotExist:
                return False
        if category.lower() == CHHATIS.lower():
            try:
                langCategoryObj = Hindi_Chhatis.objects.get(URL = URL)
                return True
            except Hindi_Chhatis.DoesNotExist:
                return False
        if category.lower() == RAIPUR.lower():
            try:
                langCategoryObj = Hindi_Raipur.objects.get(URL = URL)
                return True
            except Hindi_Raipur.DoesNotExist:
                return False
        if category.lower() == BHILAI.lower():
            try:
                langCategoryObj = Hindi_Bhilai.objects.get(URL = URL)
                return True
            except Hindi_Bhilai.DoesNotExist:
                return False
        if category.lower() == RAJNANDGAO.lower():
            try:
                langCategoryObj = Hindi_Rajnandgao.objects.get(URL = URL)
                return True
            except Hindi_Rajnandgao.DoesNotExist:
                return False
        if category.lower() == RAIGARH.lower():
            try:
                langCategoryObj = Hindi_Raigarh.objects.get(URL = URL)
                return True
            except Hindi_Raigarh.DoesNotExist:
                return False
        if category.lower() == JAGDALPUR.lower():
            try:
                langCategoryObj = Hindi_Jagdalpur.objects.get(URL = URL)
                return True
            except Hindi_Jagdalpur.DoesNotExist:
                return False
        if category.lower() == KORVA.lower():
            try:
                langCategoryObj = Hindi_Korva.objects.get(URL = URL)
                return True
            except Hindi_Korva.DoesNotExist:
                return False
        if category.lower() == RANCHI.lower():
            try:
                langCategoryObj = Hindi_Ranchi.objects.get(URL = URL)
                return True
            except Hindi_Ranchi.DoesNotExist:
                return False
        if category.lower() == DHANBAD.lower():
            try:
                langCategoryObj = Hindi_Dhanbad.objects.get(URL = URL)
                return True
            except Hindi_Dhanbad.DoesNotExist:
                return False
        if category.lower() == JAMSHEDPUR.lower():
            try:
                langCategoryObj = Hindi_Jamshedpur.objects.get(URL = URL)
                return True
            except Hindi_Jamshedpur.DoesNotExist:
                return False
        if category.lower() == GIRIDIHI.lower():
            try:
                langCategoryObj = Hindi_Giridihi.objects.get(URL = URL)
                return True
            except Hindi_Giridihi.DoesNotExist:
                return False
        if category.lower() == HAZARIBAGH.lower():
            try:
                langCategoryObj = Hindi_Hazaribagh.objects.get(URL = URL)
                return True
            except Hindi_Hazaribagh.DoesNotExist:
                return False
        if category.lower() == BOKARO.lower():
            try:
                langCategoryObj = Hindi_Bokaro.objects.get(URL = URL)
                return True
            except Hindi_Bokaro.DoesNotExist:
                return False
        if category.lower() == DEHRADUN.lower():
            try:
                langCategoryObj = Hindi_Dehradun.objects.get(URL = URL)
                return True
            except Hindi_Dehradun.DoesNotExist:
                return False
        if category.lower() == NAINITAAL.lower():
            try:
                langCategoryObj = Hindi_Nainitaal.objects.get(URL = URL)
                return True
            except Hindi_Nainitaal.DoesNotExist:
                return False
        if category.lower() == HARIDWAAR.lower():
            try:
                langCategoryObj = Hindi_Haridwaar.objects.get(URL = URL)
                return True
            except Hindi_Haridwaar.DoesNotExist:
                return False
        if category.lower() == ALMORAH.lower():
            try:
                langCategoryObj = Hindi_Almorah.objects.get(URL = URL)
                return True
            except Hindi_Almorah.DoesNotExist:
                return False
        if category.lower() == UDDHAMSINGHNAGAR.lower():
            try:
                langCategoryObj = Hindi_UddhamSinghNagar.objects.get(URL = URL)
                return True
            except Hindi_UddhamSinghNagar.DoesNotExist:
                return False
        if category.lower() == SIMLA.lower():
            try:
                langCategoryObj = Hindi_Simla.objects.get(URL = URL)
                return True
            except Hindi_Simla.DoesNotExist:
                return False
        if category.lower() == MANDI.lower():
            try:
                langCategoryObj = Hindi_Mandi.objects.get(URL = URL)
                return True
            except Hindi_Mandi.DoesNotExist:
                return False
        if category.lower() == BILASPUR.lower():
            try:
                langCategoryObj = Hindi_Bilaspur.objects.get(URL = URL)
                return True
            except Hindi_Bilaspur.DoesNotExist:
                return False
        if category.lower() == AMRITSAR.lower():
            try:
                langCategoryObj = Hindi_Amritsar.objects.get(URL = URL)
                return True
            except Hindi_Amritsar.DoesNotExist:
                return False
        if category.lower() == JALANDHAR.lower():
            try:
                langCategoryObj = Hindi_Jalandhar.objects.get(URL = URL)
                return True
            except Hindi_Jalandhar.DoesNotExist:
                return False
        if category.lower() == LUDHIANA.lower():
            try:
                langCategoryObj = Hindi_Ludhiana.objects.get(URL = URL)
                return True
            except Hindi_Ludhiana.DoesNotExist:
                return False
        if category.lower() == ROPARH.lower():
            try:
                langCategoryObj = Hindi_Roparh.objects.get(URL = URL)
                return True
            except Hindi_Roparh.DoesNotExist:
                return False
        if category.lower() == CHANDIGARH.lower():
            try:
                langCategoryObj = Hindi_Chandigarh.objects.get(URL = URL)
                return True
            except Hindi_Chandigarh.DoesNotExist:
                return False
        if category.lower() == ROHTAK.lower():
            try:
                langCategoryObj = Hindi_Rohtak.objects.get(URL = URL)
                return True
            except Hindi_Rohtak.DoesNotExist:
                return False
        if category.lower() == PANCHKULA.lower():
            try:
                langCategoryObj = Hindi_Panchkula.objects.get(URL = URL)
                return True
            except Hindi_Panchkula.DoesNotExist:
                return False
        if category.lower() == AMBALA.lower():
            try:
                langCategoryObj = Hindi_Ambala.objects.get(URL = URL)
                return True
            except Hindi_Ambala.DoesNotExist:
                return False
        if category.lower() == PANIPAT.lower():
            try:
                langCategoryObj = Hindi_Panipat.objects.get(URL = URL)
                return True
            except Hindi_Panipat.DoesNotExist:
                return False
        if category.lower() == GURGAON.lower():
            try:
                langCategoryObj = Hindi_Gurgaon.objects.get(URL = URL)
                return True
            except Hindi_Gurgaon.DoesNotExist:
                return False
        if category.lower() == HISSAR.lower():
            try:
                langCategoryObj = Hindi_Hissar.objects.get(URL = URL)
                return True
            except Hindi_Hissar.DoesNotExist:
                return False
        if category.lower() == JAMMU.lower():
            try:
                langCategoryObj = Hindi_Jammu.objects.get(URL = URL)
                return True
            except Hindi_Jammu.DoesNotExist:
                return False
        if category.lower() == SRINAGAR.lower():
            try:
                langCategoryObj = Hindi_Srinagar.objects.get(URL = URL)
                return True
            except Hindi_Srinagar.DoesNotExist:
                return False
        if category.lower() == POONCH.lower():
            try:
                langCategoryObj = Hindi_Poonch.objects.get(URL = URL)
                return True
            except Hindi_Poonch.DoesNotExist:
                return False
        if category.lower() == KOLKATA.lower():
            try:
                langCategoryObj = Hindi_Kolkata.objects.get(URL = URL)
                return True
            except Hindi_Kolkata.DoesNotExist:
                return False
        if category.lower() == JALPAIGURHI.lower():
            try:
                langCategoryObj = Hindi_Jalpaigurhi.objects.get(URL = URL)
                return True
            except Hindi_Jalpaigurhi.DoesNotExist:
                return False
        if category.lower() == DARJEELING.lower():
            try:
                langCategoryObj = Hindi_Darjeeling.objects.get(URL = URL)
                return True
            except Hindi_Darjeeling.DoesNotExist:
                return False
        if category.lower() == ASANSOL.lower():
            try:
                langCategoryObj = Hindi_Asansol.objects.get(URL = URL)
                return True
            except Hindi_Asansol.DoesNotExist:
                return False
        if category.lower() == SILIGURHI.lower():
            try:
                langCategoryObj = Hindi_Siligurhi.objects.get(URL = URL)
                return True
            except Hindi_Siligurhi.DoesNotExist:
                return False
        if category.lower() == BHUVANESHWAR.lower():
            try:
                langCategoryObj = Hindi_Bhuvaneshwar.objects.get(URL = URL)
                return True
            except Hindi_Bhuvaneshwar.DoesNotExist:
                return False
        if category.lower() == PURI.lower():
            try:
                langCategoryObj = Hindi_Puri.objects.get(URL = URL)
                return True
            except Hindi_Puri.DoesNotExist:
                return False
        if category.lower() == CUTTACK.lower():
            try:
                langCategoryObj = Hindi_Cuttack.objects.get(URL = URL)
                return True
            except Hindi_Cuttack.DoesNotExist:
                return False
        if category.lower() == AHMEDABAD.lower():
            try:
                langCategoryObj = Hindi_Ahmedabad.objects.get(URL = URL)
                return True
            except Hindi_Ahmedabad.DoesNotExist:
                return False
        if category.lower() == SURAT.lower():
            try:
                langCategoryObj = Hindi_Surat.objects.get(URL = URL)
                return True
            except Hindi_Surat.DoesNotExist:
                return False
        if category.lower() == VADODARA.lower():
            try:
                langCategoryObj = Hindi_Vadodara.objects.get(URL = URL)
                return True
            except Hindi_Vadodara.DoesNotExist:
                return False
        if category.lower() == MUMBAI.lower():
            try:
                langCategoryObj = Hindi_Mumbai.objects.get(URL = URL)
                return True
            except Hindi_Mumbai.DoesNotExist:
                return False
        if category.lower() == NAGPUR.lower():
            try:
                langCategoryObj = Hindi_Nagpur.objects.get(URL = URL)
                return True
            except Hindi_Nagpur.DoesNotExist:
                return False
        if category.lower() == PUNE.lower():
            try:
                langCategoryObj = Hindi_Pune.objects.get(URL = URL)
                return True
            except Hindi_Pune.DoesNotExist:
                return False


def getMaxClusterIdForRerun(lang, category):
    #logger.info("Entered getMaxClusterIdForRerun ")
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            maxDict = English_Economy_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SPORTS.lower():
            maxDict = English_Sports_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            maxDict = English_Top_Stories_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WORLD.lower():
            maxDict = English_World_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == OPINION.lower():
            maxDict = English_Opinion_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == HEALTH.lower():
            maxDict = English_Health_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == LIFESTYLE.lower():
            maxDict = English_Lifestyle_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENTERTAINMENT.lower():
            maxDict = English_Entertainment_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TECHNOLOGY.lower():
            maxDict = English_Technology_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == POLITICS.lower():
            maxDict = English_Politics_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENVIRONMENT.lower():
            maxDict = English_Environment_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BOOKS.lower():
            maxDict = English_Books_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TRAVEL.lower():
            maxDict = English_Travel_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SCIENCE.lower():
            maxDict = English_Science_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BUSINESS.lower():
            maxDict = English_Business_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == STOCKS.lower():
            maxDict = English_Stocks_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FOOD.lower():
            maxDict = English_Food_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WEEKEND.lower():
            maxDict = English_Weekend_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FASHION.lower():
            maxDict = English_Fashion_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == MUMBAI.lower():
            maxDict = English_Mumbai_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == ENGLISH.lower():
        if category.lower() == PUNE.lower():
            maxDict = English_Pune_Rerun.objects.all().aggregate(Max('Cluster_Id'))


    if lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            maxDict = Marathi_Economy_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == SPORTS.lower():
            maxDict = Marathi_Sports_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            maxDict = Marathi_Top_Stories_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == MAHARASHTRA.lower():
            maxDict = Marathi_Maharashtra_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == WORLD.lower():
            maxDict = Marathi_World_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == OPINION.lower():
            maxDict = Marathi_Opinion_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == HEALTH.lower():
            maxDict = Marathi_Health_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == LIFESTYLE.lower():
            maxDict = Marathi_Lifestyle_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            maxDict = Marathi_Entertainment_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == TECHNOLOGY.lower():
            maxDict = Marathi_Technology_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == POLITICS.lower():
            maxDict = Marathi_Politics_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENVIRONMENT.lower():
            maxDict = Marathi_Environment_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == BOOKS.lower():
            maxDict = Marathi_Books_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == TRAVEL.lower():
            maxDict = Marathi_Travel_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == SCIENCE.lower():
            maxDict = Marathi_Science_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == BUSINESS.lower():
            maxDict = Marathi_Business_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == STOCKS.lower():
            maxDict = Marathi_Stocks_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == FOOD.lower():
            maxDict = Marathi_Food_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == WEEKEND.lower():
            maxDict = Marathi_Weekend_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == FASHION.lower():
            maxDict = Marathi_Fashion_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == MUMBAI.lower():
            maxDict = Marathi_Mumbai_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == PUNE.lower():
            maxDict = Marathi_Pune_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == NAGPUR.lower():
            maxDict = Marathi_Nagpur_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == NASIK.lower():
            maxDict = Marathi_Nasik_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == AURANGABAD.lower():
            maxDict = Marathi_Aurangabad_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == SOLAPUR.lower():
            maxDict = Marathi_Solapur_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == KOLHAPUR.lower():
            maxDict = Marathi_Kolhapur_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == SATARA.lower():
            maxDict = Marathi_Satara_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == SANGLI.lower():
            maxDict = Marathi_Sangli_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == AKOLA.lower():
            maxDict = Marathi_Akola_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == AHMEDNAGAR.lower():
            maxDict = Marathi_Ahmednagar_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == JALGAON.lower():
            maxDict = Marathi_Jalgaon_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == GOA.lower():
            maxDict = Marathi_Goa_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == CHANDRAPUR.lower():
            maxDict = Marathi_Chandrapur_Rerun.objects.all().aggregate(Max('Cluster_Id'))
    if lang.lower() == MARATHI.lower():
        if category.lower() == WARDHA.lower():
            maxDict = Marathi_Wardha_Rerun.objects.all().aggregate(Max('Cluster_Id'))

    if lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            maxDict = Hindi_Sports_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == TOP_STORIES.lower():
            maxDict = Hindi_Top_Stories_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == WORLD.lower():
            maxDict = Hindi_World_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == OPINION.lower():
            maxDict = Hindi_Opinion_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == HEALTH.lower():
            maxDict = Hindi_Health_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == LIFESTYLE.lower():
            maxDict = Hindi_Lifestyle_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ENTERTAINMENT.lower():
            maxDict = Hindi_Entertainment_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == TECHNOLOGY.lower():
            maxDict = Hindi_Technology_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == POLITICS.lower():
            maxDict = Hindi_Politics_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == ENVIRONMENT.lower():
            maxDict = Hindi_Environment_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == TRAVEL.lower():
            maxDict = Hindi_Travel_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == SCIENCE.lower():
            maxDict = Hindi_Science_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == BUSINESS.lower():
            maxDict = Hindi_Business_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == STOCKS.lower():
            maxDict = Hindi_Stocks_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == FOOD.lower():
            maxDict = Hindi_Food_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == WEEKEND.lower():
            maxDict = Hindi_Weekend_Rerun.objects.all().aggregate(Max('Cluster_Id'))
        elif category.lower() == FASHION.lower():
            maxDict = Hindi_Fashion_Rerun.objects.all().aggregate(Max('Cluster_Id'))

    #logger.info("Exited selectLangCategoryTable ")
    return maxDict

def deleteRerunTable(lang, category):
    #logger.info("Entered deleteRerunTable ")
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            langCategoryObj = English_Economy_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = English_Sports_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = English_Top_Stories_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = English_World_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == OPINION.lower():
            langCategoryObj = English_Opinion_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = English_Health_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = English_Lifestyle_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = English_Entertainment_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = English_Technology_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == POLITICS.lower():
            langCategoryObj = English_Politics_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = English_Environment_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BOOKS.lower():
            langCategoryObj = English_Books_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TRAVEL.lower():
            langCategoryObj = English_Travel_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = English_Science_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = English_Business_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == STOCKS.lower():
            langCategoryObj = English_Stocks_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = English_Food_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WEEKEND.lower():
            langCategoryObj = English_Weekend_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = English_Fashion_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == MUMBAI.lower():
            langCategoryObj = English_Mumbai_Rerun.objects.all().delete()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == PUNE.lower():
            langCategoryObj = English_Pune_Rerun.objects.all().delete()

    if lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            langCategoryObj = Marathi_Economy_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = Marathi_Sports_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Marathi_Top_Stories_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == MAHARASHTRA.lower():
            langCategoryObj = Marathi_Maharashtra_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = Marathi_World_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == OPINION.lower():
            langCategoryObj = Marathi_Opinion_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = Marathi_Health_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = Marathi_Lifestyle_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Marathi_Entertainment_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = Marathi_Technology_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == POLITICS.lower():
            langCategoryObj = Marathi_Politics_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = Marathi_Environment_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == BOOKS.lower():
            langCategoryObj = Marathi_Books_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TRAVEL.lower():
            langCategoryObj = Marathi_Travel_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = Marathi_Science_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = Marathi_Business_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == STOCKS.lower():
            langCategoryObj = Marathi_Stocks_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = Marathi_Food_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == WEEKEND.lower():
            langCategoryObj = Marathi_Weekend_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = Marathi_Fashion_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == MUMBAI.lower():
            langCategoryObj = Marathi_Mumbai_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == PUNE.lower():
            langCategoryObj = Marathi_Pune_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == NAGPUR.lower():
            langCategoryObj = Marathi_Nagpur_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == NASIK.lower():
            langCategoryObj = Marathi_Nasik_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AURANGABAD.lower():
            langCategoryObj = Marathi_Aurangabad_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SOLAPUR.lower():
            langCategoryObj = Marathi_Solapur_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == KOLHAPUR.lower():
            langCategoryObj = Marathi_Kolhapur_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SATARA.lower():
            langCategoryObj = Marathi_Satara_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SANGLI.lower():
            langCategoryObj = Marathi_Sangli_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AKOLA.lower():
            langCategoryObj = Marathi_Akola_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AHMEDNAGAR.lower():
            langCategoryObj = Marathi_Ahmednagar_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == JALGAON.lower():
            langCategoryObj = Marathi_Jalgaon_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == GOA.lower():
            langCategoryObj = Marathi_Goa_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == CHANDRAPUR.lower():
            langCategoryObj = Marathi_Chandrapur_Rerun.objects.all().delete()
    if lang.lower() == MARATHI.lower():
        if category.lower() == WARDHA.lower():
            langCategoryObj = Marathi_Wardha_Rerun.objects.all().delete()
    if lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = Hindi_Sports_Rerun.objects.all().delete()
        elif category.lower() == TOP_STORIES.lower():
            langCategoryObj = Hindi_Top_Stories_Rerun.objects.all().delete()
        elif category.lower() == WORLD.lower():
            langCategoryObj = Hindi_World_Rerun.objects.all().delete()
        elif category.lower() == OPINION.lower():
            langCategoryObj = Hindi_Opinion_Rerun.objects.all().delete()
        elif category.lower() == HEALTH.lower():
            langCategoryObj = Hindi_Health_Rerun.objects.all().delete()
        elif category.lower() == LIFESTYLE.lower():
            langCategoryObj = Hindi_Lifestyle_Rerun.objects.all().delete()
        elif category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Hindi_Entertainment_Rerun.objects.all().delete()
        elif category.lower() == TECHNOLOGY.lower():
            langCategoryObj = Hindi_Technology_Rerun.objects.all().delete()
        elif category.lower() == POLITICS.lower():
            langCategoryObj = Hindi_Politics_Rerun.objects.all().delete()
        elif category.lower() == ENVIRONMENT.lower():
            langCategoryObj = Hindi_Environment_Rerun.objects.all().delete()
        elif category.lower() == TRAVEL.lower():
            langCategoryObj = Hindi_Travel_Rerun.objects.all().delete()
        elif category.lower() == SCIENCE.lower():
            langCategoryObj = Hindi_Science_Rerun.objects.all().delete()
        elif category.lower() == BUSINESS.lower():
            langCategoryObj = Hindi_Business_Rerun.objects.all().delete()
        elif category.lower() == STOCKS.lower():
            langCategoryObj = Hindi_Stocks_Rerun.objects.all().delete()
        elif category.lower() == FOOD.lower():
            langCategoryObj = Hindi_Food_Rerun.objects.all().delete()
        elif category.lower() == WEEKEND.lower():
            langCategoryObj = Hindi_Weekend_Rerun.objects.all().delete()
        elif category.lower() == FASHION.lower():
            langCategoryObj = Hindi_Fashion_Rerun.objects.all().delete()

    #logger.info("Exited deleteRerunTable ")

def deleteLangCategoryTable(lang, category):
    #logger.info("Entered deleteLangCategoryTable ")
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            langCategoryObj = English_Economy.objects.all().delete()

        elif category.lower() == SPORTS.lower():
            langCategoryObj = English_Sports.objects.all().delete()

        elif category.lower() == TOP_STORIES.lower():
            langCategoryObj = English_Top_Stories.objects.all().delete()

        elif category.lower() == WORLD.lower():
            langCategoryObj = English_World.objects.all().delete()

        elif category.lower() == OPINION.lower():
            langCategoryObj = English_Opinion.objects.all().delete()

        elif category.lower() == HEALTH.lower():
            langCategoryObj = English_Health.objects.all().delete()

        elif category.lower() == LIFESTYLE.lower():
            langCategoryObj = English_Lifestyle.objects.all().delete()

        elif category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = English_Entertainment.objects.all().delete()

        elif category.lower() == TECHNOLOGY.lower():
            langCategoryObj = English_Technology.objects.all().delete()

        elif category.lower() == POLITICS.lower():
            langCategoryObj = English_Politics.objects.all().delete()

        elif category.lower() == ENVIRONMENT.lower():
            langCategoryObj = English_Environment.objects.all().delete()

        elif category.lower() == BOOKS.lower():
            langCategoryObj = English_Books.objects.all().delete()

        elif category.lower() == TRAVEL.lower():
            langCategoryObj = English_Travel.objects.all().delete()

        elif category.lower() == SCIENCE.lower():
            langCategoryObj = English_Science.objects.all().delete()

        elif category.lower() == BUSINESS.lower():
            langCategoryObj = English_Business.objects.all().delete()

        elif category.lower() == TOPN.lower():
            langCategoryObj = TopN_English.objects.all().delete()

        elif category.lower() == STOCKS.lower():
            langCategoryObj = English_Stocks.objects.all().delete()
        elif category.lower() == FOOD.lower():
            langCategoryObj = English_Food.objects.all().delete()
        elif category.lower() == WEEKEND.lower():
            langCategoryObj = English_Weekend.objects.all().delete()
        elif category.lower() == FASHION.lower():
            langCategoryObj = English_Fashion.objects.all().delete()
        elif category.lower() == MUMBAI.lower():
            langCategoryObj = English_Mumbai.objects.all().delete()
        elif category.lower() == PUNE.lower():
            langCategoryObj = English_Pune.objects.all().delete()

    elif lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            langCategoryObj = Marathi_Economy.objects.all().delete()

        elif category.lower() == SPORTS.lower():
            langCategoryObj = Marathi_Sports.objects.all().delete()

        elif category.lower() == TOP_STORIES.lower():
            langCategoryObj = Marathi_Top_Stories.objects.all().delete()

        elif category.lower() == MAHARASHTRA.lower():
            langCategoryObj = Marathi_Maharashtra.objects.all().delete()


        elif category.lower() == WORLD.lower():
            langCategoryObj = Marathi_World.objects.all().delete()

        elif category.lower() == OPINION.lower():
            langCategoryObj = Marathi_Opinion.objects.all().delete()

        elif category.lower() == HEALTH.lower():
            langCategoryObj = Marathi_Health.objects.all().delete()

        elif category.lower() == LIFESTYLE.lower():
            langCategoryObj = Marathi_Lifestyle.objects.all().delete()

        elif category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Marathi_Entertainment.objects.all().delete()

        elif category.lower() == TECHNOLOGY.lower():
            langCategoryObj = Marathi_Technology.objects.all().delete()

        elif category.lower() == POLITICS.lower():
            langCategoryObj = Marathi_Politics.objects.all().delete()

        elif category.lower() == ENVIRONMENT.lower():
            langCategoryObj = Marathi_Environment.objects.all().delete()

        elif category.lower() == BOOKS.lower():
            langCategoryObj = Marathi_Books.objects.all().delete()

        elif category.lower() == TRAVEL.lower():
            langCategoryObj = Marathi_Travel.objects.all().delete()

        elif category.lower() == SCIENCE.lower():
            langCategoryObj = Marathi_Science.objects.all().delete()

        elif category.lower() == BUSINESS.lower():
            langCategoryObj = Marathi_Business.objects.all().delete()

        elif category.lower() == STOCKS.lower():
            langCategoryObj = Marathi_Stocks.objects.all().delete()

        elif category.lower() == FOOD.lower():
            langCategoryObj = Marathi_Food.objects.all().delete()

        elif category.lower() == WEEKEND.lower():
            langCategoryObj = Marathi_Weekend.objects.all().delete()

        elif category.lower() == FASHION.lower():
            langCategoryObj = Marathi_Fashion.objects.all().delete()

        elif category.lower() == MUMBAI.lower():
            langCategoryObj = Marathi_Mumbai.objects.all().delete()

        elif category.lower() == PUNE.lower():
            langCategoryObj = Marathi_Pune.objects.all().delete()

        elif category.lower() == NAGPUR.lower():
            langCategoryObj = Marathi_Nagpur.objects.all().delete()

        elif category.lower() == NASIK.lower():
            langCategoryObj = Marathi_Nasik.objects.all().delete()

        elif category.lower() == AURANGABAD.lower():
            langCategoryObj = Marathi_Aurangabad.objects.all().delete()

        elif category.lower() == SOLAPUR.lower():
            langCategoryObj = Marathi_Solapur.objects.all().delete()

        elif category.lower() == KOLHAPUR.lower():
            langCategoryObj = Marathi_Kolhapur.objects.all().delete()

        elif category.lower() == SATARA.lower():
            langCategoryObj = Marathi_Satara.objects.all().delete()

        elif category.lower() == SANGLI.lower():
            langCategoryObj = Marathi_Sangli.objects.all().delete()

        elif category.lower() == AKOLA.lower():
            langCategoryObj = Marathi_Akola.objects.all().delete()

        elif category.lower() == AHMEDNAGAR.lower():
            langCategoryObj = Marathi_Ahmednagar.objects.all().delete()

        elif category.lower() == JALGAON.lower():
            langCategoryObj = Marathi_Jalgaon.objects.all().delete()

        elif category.lower() == GOA.lower():
            langCategoryObj = Marathi_Goa.objects.all().delete()

        elif category.lower() == CHANDRAPUR.lower():
            langCategoryObj = Marathi_Chandrapur.objects.all().delete()

        elif category.lower() == WARDHA.lower():
            langCategoryObj = Marathi_Wardha.objects.all().delete()

        elif category.lower() == TOPN.lower():
            langCategoryObj = TopN_Marathi.objects.all().delete()
    elif lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = Hindi_Sports.objects.all().delete()
        elif category.lower() == TOP_STORIES.lower():
            langCategoryObj = Hindi_Top_Stories.objects.all().delete()
        elif category.lower() == WORLD.lower():
            langCategoryObj = Hindi_World.objects.all().delete()
        elif category.lower() == OPINION.lower():
            langCategoryObj = Hindi_Opinion.objects.all().delete()
        elif category.lower() == HEALTH.lower():
            langCategoryObj = Hindi_Health.objects.all().delete()
        elif category.lower() == LIFESTYLE.lower():
            langCategoryObj = Hindi_Lifestyle.objects.all().delete()
        elif category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Hindi_Entertainment.objects.all().delete()
        elif category.lower() == TECHNOLOGY.lower():
            langCategoryObj = Hindi_Technology.objects.all().delete()
        elif category.lower() == POLITICS.lower():
            langCategoryObj = Hindi_Politics.objects.all().delete()
        elif category.lower() == ENVIRONMENT.lower():
            langCategoryObj = Hindi_Environment.objects.all().delete()
        elif category.lower() == TRAVEL.lower():
            langCategoryObj = Hindi_Travel.objects.all().delete()
        elif category.lower() == SCIENCE.lower():
            langCategoryObj = Hindi_Science.objects.all().delete()
        elif category.lower() == BUSINESS.lower():
            langCategoryObj = Hindi_Business.objects.all().delete()
        elif category.lower() == STOCKS.lower():
            langCategoryObj = Hindi_Stocks.objects.all().delete()
        elif category.lower() == FOOD.lower():
            langCategoryObj = Hindi_Food.objects.all().delete()
        elif category.lower() == WEEKEND.lower():
            langCategoryObj = Hindi_Weekend.objects.all().delete()
        elif category.lower() == FASHION.lower():
            langCategoryObj = Hindi_Fashion.objects.all().delete()
        elif category.lower() == CRIME.lower():
            langCategoryObj = Hindi_Crime.objects.all().delete()
        elif category.lower() == AUTO.lower():
            langCategoryObj = Hindi_Auto.objects.all().delete()
        elif category.lower() == UTTARPRADESH.lower():
            langCategoryObj = Hindi_UttarPradesh.objects.all().delete()
        elif category.lower() == UTTARAKHAND.lower():
            langCategoryObj = Hindi_Uttarakhand.objects.all().delete()
        elif category.lower() == HIMACHALPRADESH.lower():
            langCategoryObj = Hindi_HimachalPradesh.objects.all().delete()
        elif category.lower() == DELHI.lower():
            langCategoryObj = Hindi_Delhi.objects.all().delete()
        elif category.lower() == JAMMUKASHMIR.lower():
            langCategoryObj = Hindi_JammuKashmir.objects.all().delete()
        elif category.lower() == PUNJAB.lower():
            langCategoryObj = Hindi_Punjab.objects.all().delete()
        elif category.lower() == MADHYAPRADESH.lower():
            langCategoryObj = Hindi_MadhyaPradesh.objects.all().delete()
        elif category.lower() == JHARKHAND.lower():
            langCategoryObj = Hindi_Jharkhand.objects.all().delete()
        elif category.lower() == BIHAR.lower():
            langCategoryObj = Hindi_Bihar.objects.all().delete()
        elif category.lower() == HARYANA.lower():
            langCategoryObj = Hindi_Haryana.objects.all().delete()
        elif category.lower() == CHATTISGARH.lower():
            langCategoryObj = Hindi_Chattisgarh.objects.all().delete()
        elif category.lower() == RAJASTHAN.lower():
            langCategoryObj = Hindi_Rajasthan.objects.all().delete()
        elif category.lower() == WESTBENGAL.lower():
            langCategoryObj = Hindi_WestBengal.objects.all().delete()
        elif category.lower() == ORISSA.lower():
            langCategoryObj = Hindi_Orissa.objects.all().delete()
        elif category.lower() == GUJRAT.lower():
            langCategoryObj = Hindi_Gujrat.objects.all().delete()
        elif category.lower() == MAHARASHTRA.lower():
            langCategoryObj = Hindi_Maharashtra.objects.all().delete()
        elif category.lower() == LUCKNOW.lower():
            langCategoryObj = Hindi_Lucknow.objects.all().delete()
        elif category.lower() == ALLAHABAD.lower():
            langCategoryObj = Hindi_Allahabad.objects.all().delete()
        elif category.lower() == PRATAPGARH.lower():
            langCategoryObj = Hindi_Pratapgarh.objects.all().delete()
        elif category.lower() == KANPUR.lower():
            langCategoryObj = Hindi_Kanpur.objects.all().delete()
        elif category.lower() == MERATH.lower():
            langCategoryObj = Hindi_Merath.objects.all().delete()
        elif category.lower() == AGRA.lower():
            langCategoryObj = Hindi_Agra.objects.all().delete()
        elif category.lower() == NOIDA.lower():
            langCategoryObj = Hindi_Noida.objects.all().delete()
        elif category.lower() == GAZIABAD.lower():
            langCategoryObj = Hindi_Gaziabad.objects.all().delete()
        elif category.lower() == BAGPAT.lower():
            langCategoryObj = Hindi_Bagpat.objects.all().delete()
        elif category.lower() == SAHARNPUR.lower():
            langCategoryObj = Hindi_Saharnpur.objects.all().delete()
        elif category.lower() == BULANDSHAHAR.lower():
            langCategoryObj = Hindi_Bulandshahar.objects.all().delete()
        elif category.lower() == VARANASI.lower():
            langCategoryObj = Hindi_Varanasi.objects.all().delete()
        elif category.lower() == GORAKHPUR.lower():
            langCategoryObj = Hindi_Gorakhpur.objects.all().delete()
        elif category.lower() == JHANSI.lower():
            langCategoryObj = Hindi_Jhansi.objects.all().delete()
        elif category.lower() == MUZAFFARNAGAR.lower():
            langCategoryObj = Hindi_Muzaffarnagar.objects.all().delete()
        elif category.lower() == SITAPUR.lower():
            langCategoryObj = Hindi_Sitapur.objects.all().delete()
        elif category.lower() == JAUNPUR.lower():
            langCategoryObj = Hindi_Jaunpur.objects.all().delete()
        elif category.lower() == AZAMGARH.lower():
            langCategoryObj = Hindi_Azamgarh.objects.all().delete()
        elif category.lower() == MORADABAD.lower():
            langCategoryObj = Hindi_Moradabad.objects.all().delete()
        elif category.lower() == BAREILLY.lower():
            langCategoryObj = Hindi_Bareilly.objects.all().delete()
        elif category.lower() == BALIA.lower():
            langCategoryObj = Hindi_Balia.objects.all().delete()
        elif category.lower() == ALIGARH.lower():
            langCategoryObj = Hindi_Aligarh.objects.all().delete()
        elif category.lower() == MATHURA.lower():
            langCategoryObj = Hindi_Mathura.objects.all().delete()
        elif category.lower() == BHOPAL.lower():
            langCategoryObj = Hindi_Bhopal.objects.all().delete()
        elif category.lower() == INDORE.lower():
            langCategoryObj = Hindi_Indore.objects.all().delete()
        elif category.lower() == GWALIOR.lower():
            langCategoryObj = Hindi_Gwalior.objects.all().delete()
        elif category.lower() == JABALPUR.lower():
            langCategoryObj = Hindi_Jabalpur.objects.all().delete()
        elif category.lower() == UJJAIN.lower():
            langCategoryObj = Hindi_Ujjain.objects.all().delete()
        elif category.lower() == RATLAM.lower():
            langCategoryObj = Hindi_Ratlam.objects.all().delete()
        elif category.lower() == SAGAR.lower():
            langCategoryObj = Hindi_Sagar.objects.all().delete()
        elif category.lower() == DEWAS.lower():
            langCategoryObj = Hindi_Dewas.objects.all().delete()
        elif category.lower() == SATNA.lower():
            langCategoryObj = Hindi_Satna.objects.all().delete()
        elif category.lower() == REWA.lower():
            langCategoryObj = Hindi_Rewa.objects.all().delete()
        elif category.lower() == PATNA.lower():
            langCategoryObj = Hindi_Patna.objects.all().delete()
        elif category.lower() == BHAGALPUR.lower():
            langCategoryObj = Hindi_Bhagalpur.objects.all().delete()
        elif category.lower() == MUJAFFARPUR.lower():
            langCategoryObj = Hindi_Mujaffarpur.objects.all().delete()
        elif category.lower() == GAYA.lower():
            langCategoryObj = Hindi_Gaya.objects.all().delete()
        elif category.lower() == DARBHANGA.lower():
            langCategoryObj = Hindi_Darbhanga.objects.all().delete()
        elif category.lower() == POORNIYA.lower():
            langCategoryObj = Hindi_Poorniya.objects.all().delete()
        elif category.lower() == SEWAN.lower():
            langCategoryObj = Hindi_Sewan.objects.all().delete()
        elif category.lower() == BEGUSARAI.lower():
            langCategoryObj = Hindi_Begusarai.objects.all().delete()
        elif category.lower() == KATIHAR.lower():
            langCategoryObj = Hindi_Katihar.objects.all().delete()
        elif category.lower() == JAIPUR.lower():
            langCategoryObj = Hindi_Jaipur.objects.all().delete()
        elif category.lower() == UDAIPUR.lower():
            langCategoryObj = Hindi_Udaipur.objects.all().delete()
        elif category.lower() == JODHPUR.lower():
            langCategoryObj = Hindi_Jodhpur.objects.all().delete()
        elif category.lower() == AJMER.lower():
            langCategoryObj = Hindi_Ajmer.objects.all().delete()
        elif category.lower() == BIKANER.lower():
            langCategoryObj = Hindi_Bikaner.objects.all().delete()
        elif category.lower() == ALWAR.lower():
            langCategoryObj = Hindi_Alwar.objects.all().delete()
        elif category.lower() == SIKAR.lower():
            langCategoryObj = Hindi_Sikar.objects.all().delete()
        elif category.lower() == KOTA.lower():
            langCategoryObj = Hindi_Kota.objects.all().delete()
        elif category.lower() == BHILWARA.lower():
            langCategoryObj = Hindi_Bhilwara.objects.all().delete()
        elif category.lower() == BHARATPUR.lower():
            langCategoryObj = Hindi_Bharatpur.objects.all().delete()
        elif category.lower() == CHHATIS.lower():
            langCategoryObj = Hindi_Chhatis.objects.all().delete()
        elif category.lower() == RAIPUR.lower():
            langCategoryObj = Hindi_Raipur.objects.all().delete()
        elif category.lower() == BHILAI.lower():
            langCategoryObj = Hindi_Bhilai.objects.all().delete()
        elif category.lower() == RAJNANDGAO.lower():
            langCategoryObj = Hindi_Rajnandgao.objects.all().delete()
        elif category.lower() == RAIGARH.lower():
            langCategoryObj = Hindi_Raigarh.objects.all().delete()
        elif category.lower() == JAGDALPUR.lower():
            langCategoryObj = Hindi_Jagdalpur.objects.all().delete()
        elif category.lower() == KORVA.lower():
            langCategoryObj = Hindi_Korva.objects.all().delete()
        elif category.lower() == RANCHI.lower():
            langCategoryObj = Hindi_Ranchi.objects.all().delete()
        elif category.lower() == DHANBAD.lower():
            langCategoryObj = Hindi_Dhanbad.objects.all().delete()
        elif category.lower() == JAMSHEDPUR.lower():
            langCategoryObj = Hindi_Jamshedpur.objects.all().delete()
        elif category.lower() == GIRIDIHI.lower():
            langCategoryObj = Hindi_Giridihi.objects.all().delete()
        elif category.lower() == HAZARIBAGH.lower():
            langCategoryObj = Hindi_Hazaribagh.objects.all().delete()
        elif category.lower() == BOKARO.lower():
            langCategoryObj = Hindi_Bokaro.objects.all().delete()
        elif category.lower() == DEHRADUN.lower():
            langCategoryObj = Hindi_Dehradun.objects.all().delete()
        elif category.lower() == NAINITAAL.lower():
            langCategoryObj = Hindi_Nainitaal.objects.all().delete()
        elif category.lower() == HARIDWAAR.lower():
            langCategoryObj = Hindi_Haridwaar.objects.all().delete()
        elif category.lower() == ALMORAH.lower():
            langCategoryObj = Hindi_Almorah.objects.all().delete()
        elif category.lower() == UDDHAMSINGHNAGAR.lower():
            langCategoryObj = Hindi_UddhamSinghNagar.objects.all().delete()
        elif category.lower() == SIMLA.lower():
            langCategoryObj = Hindi_Simla.objects.all().delete()
        elif category.lower() == MANDI.lower():
            langCategoryObj = Hindi_Mandi.objects.all().delete()
        elif category.lower() == BILASPUR.lower():
            langCategoryObj = Hindi_Bilaspur.objects.all().delete()
        elif category.lower() == AMRITSAR.lower():
            langCategoryObj = Hindi_Amritsar.objects.all().delete()
        elif category.lower() == JALANDHAR.lower():
            langCategoryObj = Hindi_Jalandhar.objects.all().delete()
        elif category.lower() == LUDHIANA.lower():
            langCategoryObj = Hindi_Ludhiana.objects.all().delete()
        elif category.lower() == ROPARH.lower():
            langCategoryObj = Hindi_Roparh.objects.all().delete()
        elif category.lower() == CHANDIGARH.lower():
            langCategoryObj = Hindi_Chandigarh.objects.all().delete()
        elif category.lower() == ROHTAK.lower():
            langCategoryObj = Hindi_Rohtak.objects.all().delete()
        elif category.lower() == PANCHKULA.lower():
            langCategoryObj = Hindi_Panchkula.objects.all().delete()
        elif category.lower() == AMBALA.lower():
            langCategoryObj = Hindi_Ambala.objects.all().delete()
        elif category.lower() == PANIPAT.lower():
            langCategoryObj = Hindi_Panipat.objects.all().delete()
        elif category.lower() == GURGAON.lower():
            langCategoryObj = Hindi_Gurgaon.objects.all().delete()
        elif category.lower() == HISSAR.lower():
            langCategoryObj = Hindi_Hissar.objects.all().delete()
        elif category.lower() == JAMMU.lower():
            langCategoryObj = Hindi_Jammu.objects.all().delete()
        elif category.lower() == SRINAGAR.lower():
            langCategoryObj = Hindi_Srinagar.objects.all().delete()
        elif category.lower() == POONCH.lower():
            langCategoryObj = Hindi_Poonch.objects.all().delete()
        elif category.lower() == KOLKATA.lower():
            langCategoryObj = Hindi_Kolkata.objects.all().delete()
        elif category.lower() == JALPAIGURHI.lower():
            langCategoryObj = Hindi_Jalpaigurhi.objects.all().delete()
        elif category.lower() == DARJEELING.lower():
            langCategoryObj = Hindi_Darjeeling.objects.all().delete()
        elif category.lower() == ASANSOL.lower():
            langCategoryObj = Hindi_Asansol.objects.all().delete()
        elif category.lower() == SILIGURHI.lower():
            langCategoryObj = Hindi_Siligurhi.objects.all().delete()
        elif category.lower() == BHUVANESHWAR.lower():
            langCategoryObj = Hindi_Bhuvaneshwar.objects.all().delete()
        elif category.lower() == PURI.lower():
            langCategoryObj = Hindi_Puri.objects.all().delete()
        elif category.lower() == CUTTACK.lower():
            langCategoryObj = Hindi_Cuttack.objects.all().delete()
        elif category.lower() == AHMEDABAD.lower():
            langCategoryObj = Hindi_Ahmedabad.objects.all().delete()
        elif category.lower() == SURAT.lower():
            langCategoryObj = Hindi_Surat.objects.all().delete()
        elif category.lower() == VADODARA.lower():
            langCategoryObj = Hindi_Vadodara.objects.all().delete()
        elif category.lower() == MUMBAI.lower():
            langCategoryObj = Hindi_Mumbai.objects.all().delete()
        elif category.lower() == NAGPUR.lower():
            langCategoryObj = Hindi_Nagpur.objects.all().delete()
        elif category.lower() == PUNE.lower():
            langCategoryObj = Hindi_Pune.objects.all().delete()
        elif category.lower() == TOPN.lower():
            langCategoryObj = TopN_Hindi.objects.all().delete()


    #logger.info("Exited deleteLangCategoryTable ")

def insertLangCategoryFromRerunTable(lang, category, articleObj):
    #logger.info("Entered insertLangCategoryFromRerunTable ")
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            langCategoryObj = English_Economy(Article=articleObj.Article,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=articleObj.Cluster_Id,
                                              Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = English_Sports(Article=articleObj.Article,
                                             URL=articleObj.URL,
                                             Title=articleObj.Title,
                                             Summary=articleObj.Summary,
                                             Thumbnail=articleObj.Thumbnail,
                                             Source=articleObj.Source,
                                             Published_Date=articleObj.Published_Date,
                                             Cluster_Id=articleObj.Cluster_Id,
                                             Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = English_Top_Stories(Article=articleObj.Article,
                                            URL=articleObj.URL,
                                            Title=articleObj.Title,
                                            Summary=articleObj.Summary,
                                            Thumbnail=articleObj.Thumbnail,
                                            Source=articleObj.Source,
                                            Published_Date=articleObj.Published_Date,
                                            Cluster_Id=articleObj.Cluster_Id,
                                            Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = English_World(Article=articleObj.Article,
                                            URL=articleObj.URL,
                                            Title=articleObj.Title,
                                            Summary=articleObj.Summary,
                                            Thumbnail=articleObj.Thumbnail,
                                            Source=articleObj.Source,
                                            Published_Date=articleObj.Published_Date,
                                            Cluster_Id=articleObj.Cluster_Id,
                                            Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == OPINION.lower():
            langCategoryObj = English_Opinion(Article=articleObj.Article,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=articleObj.Cluster_Id,
                                              Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = English_Health(Article=articleObj.Article,
                                             URL=articleObj.URL,
                                             Title=articleObj.Title,
                                             Summary=articleObj.Summary,
                                             Thumbnail=articleObj.Thumbnail,
                                             Source=articleObj.Source,
                                             Published_Date=articleObj.Published_Date,
                                             Cluster_Id=articleObj.Cluster_Id,
                                             Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = English_Lifestyle(Article=articleObj.Article,
                                                URL=articleObj.URL,
                                                Title=articleObj.Title,
                                                Summary=articleObj.Summary,
                                                Thumbnail=articleObj.Thumbnail,
                                                Source=articleObj.Source,
                                                Published_Date=articleObj.Published_Date,
                                                Cluster_Id=articleObj.Cluster_Id,
                                                Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = English_Entertainment(Article=articleObj.Article,
                                                    URL=articleObj.URL,
                                                    Title=articleObj.Title,
                                                    Summary=articleObj.Summary,
                                                    Thumbnail=articleObj.Thumbnail,
                                                    Source=articleObj.Source,
                                                    Published_Date=articleObj.Published_Date,
                                                    Cluster_Id=articleObj.Cluster_Id,
                                                    Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = English_Technology(Article=articleObj.Article,
                                                 URL=articleObj.URL,
                                                 Title=articleObj.Title,
                                                 Summary=articleObj.Summary,
                                                 Thumbnail=articleObj.Thumbnail,
                                                 Source=articleObj.Source,
                                                 Published_Date=articleObj.Published_Date,
                                                 Cluster_Id=articleObj.Cluster_Id,
                                                 Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == POLITICS.lower():
            langCategoryObj = English_Politics(Article=articleObj.Article,
                                               URL=articleObj.URL,
                                               Title=articleObj.Title,
                                               Summary=articleObj.Summary,
                                               Thumbnail=articleObj.Thumbnail,
                                               Source=articleObj.Source,
                                               Published_Date=articleObj.Published_Date,
                                               Cluster_Id=articleObj.Cluster_Id,
                                               Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = English_Environment(Article=articleObj.Article,
                                                  URL=articleObj.URL,
                                                  Title=articleObj.Title,
                                                  Summary=articleObj.Summary,
                                                  Thumbnail=articleObj.Thumbnail,
                                                  Source=articleObj.Source,
                                                  Published_Date=articleObj.Published_Date,
                                                  Cluster_Id=articleObj.Cluster_Id,
                                                  Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BOOKS.lower():
            langCategoryObj = English_Books(Article=articleObj.Article,
                                            URL=articleObj.URL,
                                            Title=articleObj.Title,
                                            Summary=articleObj.Summary,
                                            Thumbnail=articleObj.Thumbnail,
                                            Source=articleObj.Source,
                                            Published_Date=articleObj.Published_Date,
                                            Cluster_Id=articleObj.Cluster_Id,
                                            Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TRAVEL.lower():
            langCategoryObj = English_Travel(Article=articleObj.Article,
                                             URL=articleObj.URL,
                                             Title=articleObj.Title,
                                             Summary=articleObj.Summary,
                                             Thumbnail=articleObj.Thumbnail,
                                             Source=articleObj.Source,
                                             Published_Date=articleObj.Published_Date,
                                             Cluster_Id=articleObj.Cluster_Id,
                                             Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = English_Science(Article=articleObj.Article,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=articleObj.Cluster_Id,
                                              Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = English_Business(Article=articleObj.Article,
                                               URL=articleObj.URL,
                                               Title=articleObj.Title,
                                               Summary=articleObj.Summary,
                                               Thumbnail=articleObj.Thumbnail,
                                               Source=articleObj.Source,
                                               Published_Date=articleObj.Published_Date,
                                               Cluster_Id=articleObj.Cluster_Id,
                                               Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == STOCKS.lower():
            langCategoryObj = English_Stocks(Article=articleObj.Article,
                                             URL=articleObj.URL,
                                             Title=articleObj.Title,
                                             Summary=articleObj.Summary,
                                             Thumbnail=articleObj.Thumbnail,
                                             Source=articleObj.Source,
                                             Published_Date=articleObj.Published_Date,
                                             Cluster_Id=articleObj.Cluster_Id,
                                             Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = English_Food(Article=articleObj.Article,
                                           URL=articleObj.URL,
                                           Title=articleObj.Title,
                                           Summary=articleObj.Summary,
                                           Thumbnail=articleObj.Thumbnail,
                                           Source=articleObj.Source,
                                           Published_Date=articleObj.Published_Date,
                                           Cluster_Id=articleObj.Cluster_Id,
                                           Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WEEKEND.lower():
            langCategoryObj = English_Weekend(Article=articleObj.Article,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=articleObj.Cluster_Id,
                                              Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = English_Fashion(Article=articleObj.Article,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=articleObj.Cluster_Id,
                                              Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == MUMBAI.lower():
            langCategoryObj = English_Mumbai(Article=articleObj.Article,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=articleObj.Cluster_Id,
                                              Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == PUNE.lower():
            langCategoryObj = English_Pune(Article=articleObj.Article,
                                              URL=articleObj.URL,
                                              Title=articleObj.Title,
                                              Summary=articleObj.Summary,
                                              Thumbnail=articleObj.Thumbnail,
                                              Source=articleObj.Source,
                                              Published_Date=articleObj.Published_Date,
                                              Cluster_Id=articleObj.Cluster_Id,
                                              Is_Rep=articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_economy
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SPORTS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_sports
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_top_stories
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WORLD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_world
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == OPINION.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_opinion
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == HEALTH.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_health
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == LIFESTYLE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_lifestyle
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_entertainment
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_technology
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == POLITICS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_politics
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_environment
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == BOOKS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_books
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == TRAVEL.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_travel
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SCIENCE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_science
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == BUSINESS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_business
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == STOCKS.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_stocks
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == FOOD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_food
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WEEKEND.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_weekend
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == FASHION.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_fashion
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == MUMBAI.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_mumbai
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == PUNE.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_pune
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == NAGPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_nagpur
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == NASIK.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_nasik
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AURANGABAD.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_aurangabad
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SOLAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_solapur
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == KOLHAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_kolhapur
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SATARA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_satara
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == SANGLI.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_sangli
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AKOLA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_akola
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == AHMEDNAGAR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_ahmednagar
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == JALGAON.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_jalgaon
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == GOA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_goa
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == CHANDRAPUR.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_chandrapur
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == WARDHA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_wardha
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])
    if lang.lower() == MARATHI.lower():
        if category.lower() == MAHARASHTRA.lower():
            langObj = Language.objects.get(Name=lang)
            categoryObj = News_Category.objects.get(Name = category)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO news_schema.newsApp_marathi_maharashtra
                              (Cluster_Id,Article_id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,Is_Rep)
                               SELECT %s,id,URL,Title,Summary,Thumbnail,Source_id,Published_Date,%s
                               from news_schema.newsApp_news_article
                               WHERE Language_id = %s and Category_id = %s and id = %s''',[articleObj.Cluster_Id,articleObj.Is_Rep,langObj.id,categoryObj.id,articleObj.Article_id])

    if lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            langCategoryObj = Hindi_Sports( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategoryObj = Hindi_Top_Stories( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == WORLD.lower():
            langCategoryObj = Hindi_World( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == OPINION.lower():
            langCategoryObj = Hindi_Opinion( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == HEALTH.lower():
            langCategoryObj = Hindi_Health( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategoryObj = Hindi_Lifestyle( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategoryObj = Hindi_Entertainment( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategoryObj = Hindi_Technology( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == POLITICS.lower():
            langCategoryObj = Hindi_Politics( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategoryObj = Hindi_Environment( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == TRAVEL.lower():
            langCategoryObj = Hindi_Travel( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == SCIENCE.lower():
            langCategoryObj = Hindi_Science( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == BUSINESS.lower():
            langCategoryObj = Hindi_Business( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == STOCKS.lower():
            langCategoryObj = Hindi_Stocks( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == FOOD.lower():
            langCategoryObj = Hindi_Food( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == WEEKEND.lower():
            langCategoryObj = Hindi_Weekend( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()
    if lang.lower() == HINDI.lower():
        if category.lower() == FASHION.lower():
            langCategoryObj = Hindi_Fashion( Article = articleObj,
                                        URL = articleObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Cluster_Id = articleObj.Cluster_Id,
                                        Is_Rep = articleObj.Is_Rep)
            langCategoryObj.save()

    #logger.info("Exited insertLangCategoryFromRerunTable ")

def selectRerunTable(lang, category):
    #logger.info("Entered selectRerunTable ")
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            langCategotyAll = English_Economy_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SPORTS.lower():
            langCategotyAll = English_Sports_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategotyAll = English_Top_Stories_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WORLD.lower():
            langCategotyAll = English_World_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == OPINION.lower():
            langCategotyAll = English_Opinion_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == HEALTH.lower():
            langCategotyAll = English_Health_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategotyAll = English_Lifestyle_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategotyAll = English_Entertainment_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategotyAll = English_Technology_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == POLITICS.lower():
            langCategotyAll = English_Politics_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategotyAll = English_Environment_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BOOKS.lower():
            langCategotyAll = English_Books_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TRAVEL.lower():
            langCategotyAll = English_Travel_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SCIENCE.lower():
            langCategotyAll = English_Science_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BUSINESS.lower():
            langCategotyAll = English_Business_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == STOCKS.lower():
            langCategotyAll = English_Stocks_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FOOD.lower():
            langCategotyAll = English_Food_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WEEKEND.lower():
            langCategotyAll = English_Weekend_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FASHION.lower():
            langCategotyAll = English_Fashion_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == MUMBAI.lower():
            langCategotyAll = English_Mumbai_Rerun.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == PUNE.lower():
            langCategotyAll = English_Pune_Rerun.objects.all()

    if lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            langCategotyAll = Marathi_Economy_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SPORTS.lower():
            langCategotyAll = Marathi_Sports_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategotyAll = Marathi_Top_Stories_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == MAHARASHTRA.lower():
            langCategotyAll = Marathi_Maharashtra_Rerun.objects.all()

    if lang.lower() == MARATHI.lower():
        if category.lower() == WORLD.lower():
            langCategotyAll = Marathi_World_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == OPINION.lower():
            langCategotyAll = Marathi_Opinion_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == HEALTH.lower():
            langCategotyAll = Marathi_Health_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategotyAll = Marathi_Lifestyle_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategotyAll = Marathi_Entertainment_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategotyAll = Marathi_Technology_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == POLITICS.lower():
            langCategotyAll = Marathi_Politics_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategotyAll = Marathi_Environment_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == BOOKS.lower():
            langCategotyAll = Marathi_Books_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TRAVEL.lower():
            langCategotyAll = Marathi_Travel_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SCIENCE.lower():
            langCategotyAll = Marathi_Science_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == BUSINESS.lower():
            langCategotyAll = Marathi_Business_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == STOCKS.lower():
            langCategotyAll = Marathi_Stocks_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == FOOD.lower():
            langCategotyAll = Marathi_Food_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == WEEKEND.lower():
            langCategotyAll = Marathi_Weekend_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == FASHION.lower():
            langCategotyAll = Marathi_Fashion_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == MUMBAI.lower():
            langCategotyAll = Marathi_Mumbai_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == PUNE.lower():
            langCategotyAll = Marathi_Pune_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == NAGPUR.lower():
            langCategotyAll = Marathi_Nagpur_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == NASIK.lower():
            langCategotyAll = Marathi_Nasik_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AURANGABAD.lower():
            langCategotyAll = Marathi_Aurangabad_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SOLAPUR.lower():
            langCategotyAll = Marathi_Solapur_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == KOLHAPUR.lower():
            langCategotyAll = Marathi_Kolhapur_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SATARA.lower():
            langCategotyAll = Marathi_Satara_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SANGLI.lower():
            langCategotyAll = Marathi_Sangli_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AKOLA.lower():
            langCategotyAll = Marathi_Akola_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AHMEDNAGAR.lower():
            langCategotyAll = Marathi_Ahmednagar_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == JALGAON.lower():
            langCategotyAll = Marathi_Jalgaon_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == GOA.lower():
            langCategotyAll = Marathi_Goa_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == CHANDRAPUR.lower():
            langCategotyAll = Marathi_Chandrapur_Rerun.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == WARDHA.lower():
            langCategotyAll = Marathi_Wardha_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            langCategotyAll = Hindi_Sports_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategotyAll = Hindi_Top_Stories_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == WORLD.lower():
            langCategotyAll = Hindi_World_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == OPINION.lower():
            langCategotyAll = Hindi_Opinion_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == HEALTH.lower():
            langCategotyAll = Hindi_Health_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategotyAll = Hindi_Lifestyle_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategotyAll = Hindi_Entertainment_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategotyAll = Hindi_Technology_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == POLITICS.lower():
            langCategotyAll = Hindi_Politics_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategotyAll = Hindi_Environment_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == TRAVEL.lower():
            langCategotyAll = Hindi_Travel_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SCIENCE.lower():
            langCategotyAll = Hindi_Science_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BUSINESS.lower():
            langCategotyAll = Hindi_Business_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == STOCKS.lower():
            langCategotyAll = Hindi_Stocks_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == FOOD.lower():
            langCategotyAll = Hindi_Food_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == WEEKEND.lower():
            langCategotyAll = Hindi_Weekend_Rerun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == FASHION.lower():
            langCategotyAll = Hindi_Fashion_Rerun.objects.all()

    #logger.info("Exited selectRerunTable ")
    return langCategotyAll

def selectLangCatAll(lang, category):
    #logger.info("Entered selectLangCatAll ")


    if lang.lower() == ENGLISH.lower():
        if category.lower() == ECONOMY.lower():
            langCategotyAll = English_Economy.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SPORTS.lower():
            langCategotyAll = English_Sports.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategotyAll = English_Top_Stories.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WORLD.lower():
            langCategotyAll = English_World.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == OPINION.lower():
            langCategotyAll = English_Opinion.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == HEALTH.lower():
            langCategotyAll = English_Health.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategotyAll = English_Lifestyle.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategotyAll = English_Entertainment.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategotyAll = English_Technology.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == POLITICS.lower():
            langCategotyAll = English_Politics.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategotyAll = English_Environment.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BOOKS.lower():
            langCategotyAll = English_Books.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == TRAVEL.lower():
            langCategotyAll = English_Travel.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == SCIENCE.lower():
            langCategotyAll = English_Science.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == BUSINESS.lower():
            langCategotyAll = English_Business.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == STOCKS.lower():
            langCategotyAll = English_Stocks.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FOOD.lower():
            langCategotyAll = English_Food.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == WEEKEND.lower():
            langCategotyAll = English_Weekend.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == FASHION.lower():
            langCategotyAll = English_Fashion.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == MUMBAI.lower():
            langCategotyAll = English_Mumbai.objects.all()
    if lang.lower() == ENGLISH.lower():
        if category.lower() == PUNE.lower():
            langCategotyAll = English_Pune.objects.all()

    if lang.lower() == MARATHI.lower():
        if category.lower() == ECONOMY.lower():
            langCategotyAll = Marathi_Economy.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SPORTS.lower():
            langCategotyAll = Marathi_Sports.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategotyAll = Marathi_Top_Stories.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == MAHARASHTRA.lower():
            langCategotyAll = Marathi_Maharashtra.objects.all()

    if lang.lower() == MARATHI.lower():
        if category.lower() == WORLD.lower():
            langCategotyAll = Marathi_World.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == OPINION.lower():
            langCategotyAll = Marathi_Opinion.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == HEALTH.lower():
            langCategotyAll = Marathi_Health.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategotyAll = Marathi_Lifestyle.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategotyAll = Marathi_Entertainment.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategotyAll = Marathi_Technology.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == POLITICS.lower():
            langCategotyAll = Marathi_Politics.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategotyAll = Marathi_Environment.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == BOOKS.lower():
            langCategotyAll = Marathi_Books.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == TRAVEL.lower():
            langCategotyAll = Marathi_Travel.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SCIENCE.lower():
            langCategotyAll = Marathi_Science.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == BUSINESS.lower():
            langCategotyAll = Marathi_Business.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == STOCKS.lower():
            langCategotyAll = Marathi_Stocks.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == FOOD.lower():
            langCategotyAll = Marathi_Food.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == WEEKEND.lower():
            langCategotyAll = Marathi_Weekend.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == FASHION.lower():
            langCategotyAll = Marathi_Fashion.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == MUMBAI.lower():
            langCategotyAll = Marathi_Mumbai.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == PUNE.lower():
            langCategotyAll = Marathi_Pune.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == NAGPUR.lower():
            langCategotyAll = Marathi_Nagpur.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == NASIK.lower():
            langCategotyAll = Marathi_Nasik.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AURANGABAD.lower():
            langCategotyAll = Marathi_Aurangabad.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SOLAPUR.lower():
            langCategotyAll = Marathi_Solapur.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == KOLHAPUR.lower():
            langCategotyAll = Marathi_Kolhapur.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SATARA.lower():
            langCategotyAll = Marathi_Satara.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == SANGLI.lower():
            langCategotyAll = Marathi_Sangli.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AKOLA.lower():
            langCategotyAll = Marathi_Akola.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == AHMEDNAGAR.lower():
            langCategotyAll = Marathi_Ahmednagar.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == JALGAON.lower():
            langCategotyAll = Marathi_Jalgaon.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == GOA.lower():
            langCategotyAll = Marathi_Goa.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == CHANDRAPUR.lower():
            langCategotyAll = Marathi_Chandrapur.objects.all()
    if lang.lower() == MARATHI.lower():
        if category.lower() == WARDHA.lower():
            langCategotyAll = Marathi_Wardha.objects.all()

    if lang.lower() == HINDI.lower():
        if category.lower() == SPORTS.lower():
            langCategotyAll = Hindi_Sports.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == TOP_STORIES.lower():
            langCategotyAll = Hindi_Top_Stories.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == WORLD.lower():
            langCategotyAll = Hindi_World.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == OPINION.lower():
            langCategotyAll = Hindi_Opinion.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == HEALTH.lower():
            langCategotyAll = Hindi_Health.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == LIFESTYLE.lower():
            langCategotyAll = Hindi_Lifestyle.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENTERTAINMENT.lower():
            langCategotyAll = Hindi_Entertainment.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == TECHNOLOGY.lower():
            langCategotyAll = Hindi_Technology.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == POLITICS.lower():
            langCategotyAll = Hindi_Politics.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ENVIRONMENT.lower():
            langCategotyAll = Hindi_Environment.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == TRAVEL.lower():
            langCategotyAll = Hindi_Travel.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SCIENCE.lower():
            langCategotyAll = Hindi_Science.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BUSINESS.lower():
            langCategotyAll = Hindi_Business.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == STOCKS.lower():
            langCategotyAll = Hindi_Stocks.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == FOOD.lower():
            langCategotyAll = Hindi_Food.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == WEEKEND.lower():
            langCategotyAll = Hindi_Weekend.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == FASHION.lower():
            langCategotyAll = Hindi_Fashion.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == AUTO.lower():
            langCategotyAll = Hindi_Auto.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == CRIME.lower():
            langCategotyAll = Hindi_Crime.objects.all()

    if lang.lower() == HINDI.lower():
        if category.lower() == UTTARPRADESH.lower():
            langCategotyAll = Hindi_UttarPradesh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == UTTARAKHAND.lower():
            langCategotyAll = Hindi_Uttarakhand.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == HIMACHALPRADESH.lower():
            langCategotyAll = Hindi_HimachalPradesh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == DELHI.lower():
            langCategotyAll = Hindi_Delhi.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAMMUKASHMIR.lower():
            langCategotyAll = Hindi_JammuKashmir.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == PUNJAB.lower():
            langCategotyAll = Hindi_Punjab.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MADHYAPRADESH.lower():
            langCategotyAll = Hindi_MadhyaPradesh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JHARKHAND.lower():
            langCategotyAll = Hindi_Jharkhand.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BIHAR.lower():
            langCategotyAll = Hindi_Bihar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == HARYANA.lower():
            langCategotyAll = Hindi_Haryana.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == CHATTISGARH.lower():
            langCategotyAll = Hindi_Chattisgarh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == RAJASTHAN.lower():
            langCategotyAll = Hindi_Rajasthan.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == WESTBENGAL.lower():
            langCategotyAll = Hindi_WestBengal.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ORISSA.lower():
            langCategotyAll = Hindi_Orissa.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == GUJRAT.lower():
            langCategotyAll = Hindi_Gujrat.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MAHARASHTRA.lower():
            langCategotyAll = Hindi_Maharashtra.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == LUCKNOW.lower():
            langCategotyAll = Hindi_Lucknow.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ALLAHABAD.lower():
            langCategotyAll = Hindi_Allahabad.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == PRATAPGARH.lower():
            langCategotyAll = Hindi_Pratapgarh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == KANPUR.lower():
            langCategotyAll = Hindi_Kanpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MERATH.lower():
            langCategotyAll = Hindi_Merath.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == AGRA.lower():
            langCategotyAll = Hindi_Agra.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == NOIDA.lower():
            langCategotyAll = Hindi_Noida.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == GAZIABAD.lower():
            langCategotyAll = Hindi_Gaziabad.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BAGPAT.lower():
            langCategotyAll = Hindi_Bagpat.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SAHARNPUR.lower():
            langCategotyAll = Hindi_Saharnpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BULANDSHAHAR.lower():
            langCategotyAll = Hindi_Bulandshahar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == VARANASI.lower():
            langCategotyAll = Hindi_Varanasi.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == GORAKHPUR.lower():
            langCategotyAll = Hindi_Gorakhpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JHANSI.lower():
            langCategotyAll = Hindi_Jhansi.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MUZAFFARNAGAR.lower():
            langCategotyAll = Hindi_Muzaffarnagar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SITAPUR.lower():
            langCategotyAll = Hindi_Sitapur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAUNPUR.lower():
            langCategotyAll = Hindi_Jaunpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == AZAMGARH.lower():
            langCategotyAll = Hindi_Azamgarh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MORADABAD.lower():
            langCategotyAll = Hindi_Moradabad.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BAREILLY.lower():
            langCategotyAll = Hindi_Bareilly.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BALIA.lower():
            langCategotyAll = Hindi_Balia.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ALIGARH.lower():
            langCategotyAll = Hindi_Aligarh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MATHURA.lower():
            langCategotyAll = Hindi_Mathura.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHOPAL.lower():
            langCategotyAll = Hindi_Bhopal.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == INDORE.lower():
            langCategotyAll = Hindi_Indore.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == GWALIOR.lower():
            langCategotyAll = Hindi_Gwalior.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JABALPUR.lower():
            langCategotyAll = Hindi_Jabalpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == UJJAIN.lower():
            langCategotyAll = Hindi_Ujjain.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == RATLAM.lower():
            langCategotyAll = Hindi_Ratlam.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SAGAR.lower():
            langCategotyAll = Hindi_Sagar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == DEWAS.lower():
            langCategotyAll = Hindi_Dewas.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SATNA.lower():
            langCategotyAll = Hindi_Satna.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == REWA.lower():
            langCategotyAll = Hindi_Rewa.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == PATNA.lower():
            langCategotyAll = Hindi_Patna.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHAGALPUR.lower():
            langCategotyAll = Hindi_Bhagalpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MUJAFFARPUR.lower():
            langCategotyAll = Hindi_Mujaffarpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == GAYA.lower():
            langCategotyAll = Hindi_Gaya.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == DARBHANGA.lower():
            langCategotyAll = Hindi_Darbhanga.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == POORNIYA.lower():
            langCategotyAll = Hindi_Poorniya.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SEWAN.lower():
            langCategotyAll = Hindi_Sewan.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BEGUSARAI.lower():
            langCategotyAll = Hindi_Begusarai.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == KATIHAR.lower():
            langCategotyAll = Hindi_Katihar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAIPUR.lower():
            langCategotyAll = Hindi_Jaipur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == UDAIPUR.lower():
            langCategotyAll = Hindi_Udaipur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JODHPUR.lower():
            langCategotyAll = Hindi_Jodhpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == AJMER.lower():
            langCategotyAll = Hindi_Ajmer.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BIKANER.lower():
            langCategotyAll = Hindi_Bikaner.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ALWAR.lower():
            langCategotyAll = Hindi_Alwar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SIKAR.lower():
            langCategotyAll = Hindi_Sikar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == KOTA.lower():
            langCategotyAll = Hindi_Kota.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHILWARA.lower():
            langCategotyAll = Hindi_Bhilwara.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHARATPUR.lower():
            langCategotyAll = Hindi_Bharatpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == CHHATIS.lower():
            langCategotyAll = Hindi_Chhatis.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == RAIPUR.lower():
            langCategotyAll = Hindi_Raipur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHILAI.lower():
            langCategotyAll = Hindi_Bhilai.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == RAJNANDGAO.lower():
            langCategotyAll = Hindi_Rajnandgao.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == RAIGARH.lower():
            langCategotyAll = Hindi_Raigarh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAGDALPUR.lower():
            langCategotyAll = Hindi_Jagdalpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == KORVA.lower():
            langCategotyAll = Hindi_Korva.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == RANCHI.lower():
            langCategotyAll = Hindi_Ranchi.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == DHANBAD.lower():
            langCategotyAll = Hindi_Dhanbad.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAMSHEDPUR.lower():
            langCategotyAll = Hindi_Jamshedpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == GIRIDIHI.lower():
            langCategotyAll = Hindi_Giridihi.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == HAZARIBAGH.lower():
            langCategotyAll = Hindi_Hazaribagh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BOKARO.lower():
            langCategotyAll = Hindi_Bokaro.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == DEHRADUN.lower():
            langCategotyAll = Hindi_Dehradun.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == NAINITAAL.lower():
            langCategotyAll = Hindi_Nainitaal.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == HARIDWAAR.lower():
            langCategotyAll = Hindi_Haridwaar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ALMORAH.lower():
            langCategotyAll = Hindi_Almorah.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == UDDHAMSINGHNAGAR.lower():
            langCategotyAll = Hindi_UddhamSinghNagar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SIMLA.lower():
            langCategotyAll = Hindi_Simla.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MANDI.lower():
            langCategotyAll = Hindi_Mandi.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BILASPUR.lower():
            langCategotyAll = Hindi_Bilaspur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == AMRITSAR.lower():
            langCategotyAll = Hindi_Amritsar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JALANDHAR.lower():
            langCategotyAll = Hindi_Jalandhar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == LUDHIANA.lower():
            langCategotyAll = Hindi_Ludhiana.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ROPARH.lower():
            langCategotyAll = Hindi_Roparh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == CHANDIGARH.lower():
            langCategotyAll = Hindi_Chandigarh.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ROHTAK.lower():
            langCategotyAll = Hindi_Rohtak.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == PANCHKULA.lower():
            langCategotyAll = Hindi_Panchkula.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == AMBALA.lower():
            langCategotyAll = Hindi_Ambala.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == PANIPAT.lower():
            langCategotyAll = Hindi_Panipat.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == GURGAON.lower():
            langCategotyAll = Hindi_Gurgaon.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == HISSAR.lower():
            langCategotyAll = Hindi_Hissar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JAMMU.lower():
            langCategotyAll = Hindi_Jammu.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SRINAGAR.lower():
            langCategotyAll = Hindi_Srinagar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == POONCH.lower():
            langCategotyAll = Hindi_Poonch.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == KOLKATA.lower():
            langCategotyAll = Hindi_Kolkata.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == JALPAIGURHI.lower():
            langCategotyAll = Hindi_Jalpaigurhi.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == DARJEELING.lower():
            langCategotyAll = Hindi_Darjeeling.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == ASANSOL.lower():
            langCategotyAll = Hindi_Asansol.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SILIGURHI.lower():
            langCategotyAll = Hindi_Siligurhi.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == BHUVANESHWAR.lower():
            langCategotyAll = Hindi_Bhuvaneshwar.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == PURI.lower():
            langCategotyAll = Hindi_Puri.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == CUTTACK.lower():
            langCategotyAll = Hindi_Cuttack.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == AHMEDABAD.lower():
            langCategotyAll = Hindi_Ahmedabad.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == SURAT.lower():
            langCategotyAll = Hindi_Surat.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == VADODARA.lower():
            langCategotyAll = Hindi_Vadodara.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == MUMBAI.lower():
            langCategotyAll = Hindi_Mumbai.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == NAGPUR.lower():
            langCategotyAll = Hindi_Nagpur.objects.all()
    if lang.lower() == HINDI.lower():
        if category.lower() == PUNE.lower():
            langCategotyAll = Hindi_Pune.objects.all()

    #logger.info("Exited selectLangCatAll ")
    return langCategotyAll

def updateArticleTable(lang,category):
    #logger.info("Entered updateArticleTable ")
    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=category)
    articleObjAll = News_Article.objects.filter(Language = langObj,
                                                Category = categoryObj,
                                                Is_New = True)
    for articleObj in articleObjAll:
        articleObj.Is_New = False
        articleObj.save()
    #logger.info("Exited updateArticleTable ")



def updateRep(lang,cat,langCatObj,isRep):
    if lang.lower() == ENGLISH.lower():
        if cat.lower() == TOP_STORIES.lower():
            TopStories = English_Top_Stories.objects.filter(id = langCatObj.id)
            for TopStoriesObj in TopStories:
                TopStoriesObj.Is_Rep = isRep
                TopStoriesObj.save()
    if lang.lower() == MARATHI.lower():
        if cat.lower() == TOP_STORIES.lower():
            TopStories = Marathi_Top_Stories.objects.filter(id = langCatObj.id)
            for TopStoriesObj in TopStories:
                TopStoriesObj.Is_Rep = isRep
                TopStoriesObj.save()

def insertArchive(lang,cat):
    #logger.info("Entered insertArchive ")
    langObj = Language.objects.get(Name=lang)
    categoryObj = News_Category.objects.get(Name=cat)
    langCategotyAll = selectLangCatAll(lang,cat)
    for langCategoryObj in langCategotyAll:
        articleObj = News_Article.objects.get(id = langCategoryObj.Article.id)
        archiveObj = News_Article_Archive(Language = langObj,
                                        Category = categoryObj,
                                        URL = langCategoryObj.URL,
                                        Title = articleObj.Title,
                                        Summary = articleObj.Summary,
                                        Thumbnail = articleObj.Thumbnail,
                                        Source = articleObj.Source,
                                        Published_Date=articleObj.Published_Date,
                                        Current_Date=articleObj.Current_Date,
                                        Is_New = articleObj.Is_New,
                                        Cluster_Id = langCategoryObj.Cluster_Id,
                                        Is_Rep = langCategoryObj.Is_Rep)
        archiveObj.save()
    #logger.info("Exited insertArchive ")

def deleteArticleTable(deltaDays):
    deltaDate = datetime.date.today() - datetime.timedelta(days=deltaDays)
    articleDict = News_Article.objects.filter(Current_Date__lt=deltaDate).delete()
