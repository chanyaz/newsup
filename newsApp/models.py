from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from random import randint
from django.utils import timezone
# Create your models here.



class News_Source(models.Model):
    Name = models.CharField(max_length=70)
    def __unicode__(self):
        return '%s' % (self.Name)

class Language(models.Model):
    Name = models.CharField(max_length=15)
    def __unicode__(self):
        return '%s' % (self.Name)

class News_Category(models.Model):
    Name = models.CharField(max_length=20)
    def __unicode__(self):
        return '%s' % (self.Name)
        
class News_Feed(models.Model):
    Language = models.ForeignKey(Language)
    Category = models.ForeignKey(News_Category)
    URL = models.URLField(max_length=1000)
    Source = models.ForeignKey(News_Source)
    Type = models.CharField(max_length=20,default='JSON')
    
    def __unicode__(self):
        return '%s %s %s %s' % (self.Language,self.Category,self.URL,self.Source)

class Video_Source(models.Model):
    Name = models.CharField(max_length=70)
    def __unicode__(self):
        return '%s' % (self.Name)

class Video_Channel(models.Model):
    Language = models.ForeignKey(Language)
    Category = models.ForeignKey(News_Category)
    Channel_Id = models.CharField(max_length=100)
    Source = models.ForeignKey(Video_Source)

    def __unicode__(self):
        return '%s %s %s' % (self.Language,self.Category,self.Source)

class News_Article_Archive(models.Model):
    Language = models.ForeignKey(Language,db_index=True)
    Category = models.ForeignKey(News_Category,db_index=True)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Current_Date=models.DateTimeField()
    Archive_Date=models.DateTimeField(auto_now_add=True)
    Is_New = models.BooleanField(default=False)
    Cluster_Id = models.IntegerField(db_index=True)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Language,self.Category,self.URL)

class News_Article(models.Model):
    Language = models.ForeignKey(Language,db_index=True)
    Category = models.ForeignKey(News_Category,db_index=True)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Current_Date=models.DateTimeField(auto_now_add=True)
    Is_New = models.BooleanField(default=False)
    
    def __unicode__(self):
        return '%s %s %s' % (self.Language,self.Category,self.URL)

class TopN_News_Article(models.Model):
    Language = models.ForeignKey(Language)
    Category = models.ForeignKey(News_Category)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()


    def __unicode__(self):
        return '%s %s %s' % (self.Language,self.URL,self.Source,self.Title)

class TopN_English(models.Model):
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class TopN_Marathi(models.Model):
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class TopN_Hindi(models.Model):
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class News_Video(models.Model):
    Language = models.ForeignKey(Language,db_index=True)
    Category = models.ForeignKey(News_Category,db_index=True)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date= models.DateTimeField()
    Current_Date = models.DateTimeField(auto_now_add=True)
    Duration = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s %s %s' % (self.Language,self.Category,self.URL)

class TopN_English_Video(models.Model):
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class TopN_Marathi_Video(models.Model):
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class TopN_Hindi_Video(models.Model):
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)






class English_Economy_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s ' % (self.Title,self.URL,self.Source)

class English_Sports_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Top_Stories_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_World_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Opinion_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Health_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Lifestyle_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Entertainment_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Technology_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Politics_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s ' % (self.Title,self.URL,self.Source)

class English_Environment_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Books_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Travel_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Science_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Business_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Stocks_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Food_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Weekend_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Fashion_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Mumbai_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Pune_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)


class English_Politics(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s ' % (self.Title,self.URL,self.Source)

class English_Economy(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Sports(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Top_Stories(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_World(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Opinion(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Health(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Lifestyle(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Entertainment(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Technology(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Environment(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Books(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Travel(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Science(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Business(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Stocks(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Food(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Weekend(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Fashion(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Mumbai(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Pune(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)





class English_Top_Stories_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Entertainment_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Sports_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_World_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Business_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Lifestyle_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Health_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Fashion_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Technology_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Environment_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Science_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class English_Food_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)


class Hindi_Top_Stories_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Entertainment_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Business_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)



class Hindi_UttarPradesh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Uttarakhand(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_HimachalPradesh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Delhi(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_JammuKashmir(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Punjab(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_MadhyaPradesh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jharkhand(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bihar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Haryana(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Chattisgarh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Rajasthan(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_WestBengal(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Orissa(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Gujrat(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Maharashtra(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Lucknow(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Allahabad(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Pratapgarh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Kanpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Merath(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Agra(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Noida(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Gaziabad(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bagpat(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Saharnpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bulandshahar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Varanasi(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Gorakhpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jhansi(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Muzaffarnagar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Sitapur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jaunpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Azamgarh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Moradabad(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Faridabad(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bareilly(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Balia(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Aligarh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Mathura(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bhopal(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Indore(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Gwalior(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jabalpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Ujjain(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Ratlam(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Sagar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Dewas(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Satna(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Rewa(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Patna(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bhagalpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Mujaffarpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Gaya(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Darbhanga(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Poorniya(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Sewan(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Begusarai(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Katihar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jaipur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Udaipur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jodhpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Ajmer(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bikaner(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Alwar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Sikar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Kota(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bhilwara(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bharatpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Chhatis(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Raipur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bilaspur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bhilai(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Rajnandgao(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Raigarh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jagdalpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Korva(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Ranchi(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Dhanbad(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jamshedpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Giridihi(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Hazaribagh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bokaro(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Dehradun(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Nainitaal(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Haridwaar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Almorah(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_UddhamSinghNagar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Simla(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Mandi(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Amritsar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jalandhar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Ludhiana(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Roparh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Chandigarh(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Rohtak(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Panchkula(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Ambala(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Panipat(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Gurgaon(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Hissar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jammu(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Srinagar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Poonch(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Kolkata(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Jalpaigurhi(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Darjeeling(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Asansol(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Siligurhi(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Bhuvaneshwar(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Puri(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Cuttack(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Ahmedabad(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Surat(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Vadodara(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Mumbai(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Nagpur(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Pune(models.Model):
    Cluster_Id = models.IntegerField()
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=200)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)






class Hindi_Economy_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s ' % (self.Title,self.URL,self.Source)

class Hindi_Sports_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Top_Stories_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_World_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Opinion_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Health_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Lifestyle_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Entertainment_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Technology_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Politics_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s ' % (self.Title,self.URL,self.Source)

class Hindi_Environment_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Travel_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Science_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Business_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Stocks_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Food_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Weekend_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Fashion_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)


class Hindi_Politics(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s ' % (self.Title,self.URL,self.Source)

class Hindi_Economy(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Sports(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Top_Stories(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_World(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Opinion(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Health(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Lifestyle(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Entertainment(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Technology(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Environment(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Books(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Travel(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Science(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Business(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Stocks(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Food(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Weekend(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Fashion(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Crime(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Hindi_Auto(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)






class Marathi_Economy(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Sports(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Top_Stories(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_World(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Opinion(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Health(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Lifestyle(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Entertainment(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Technology(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Politics(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Environment(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Books(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Travel(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Science(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Business(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Stocks(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Food(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Weekend(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Fashion(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Mumbai(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Pune(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Nagpur(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Nasik(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Aurangabad(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Solapur(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Kolhapur(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Satara(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Sangli(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Akola(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Ahmednagar(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Jalgaon(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Goa(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Chandrapur(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Wardha(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Maharashtra(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)


class Marathi_Economy_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Sports_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Top_Stories_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_World_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Opinion_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Health_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Lifestyle_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Entertainment_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Technology_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Politics_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Environment_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Books_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Travel_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Science_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Business_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Stocks_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Food_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Weekend_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Fashion_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Mumbai_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)



class Marathi_Pune_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)



class Marathi_Nagpur_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Nasik_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Aurangabad_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Solapur_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Kolhapur_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Satara_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Sangli_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Akola_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Ahmednagar_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Jalgaon_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Goa_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Chandrapur_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Wardha_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Maharashtra_Rerun(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Article = models.ForeignKey(News_Article)
    URL = models.URLField(max_length=300)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(News_Source)
    Published_Date=models.DateTimeField()
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)





class Marathi_Top_Stories_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Entertainment_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)

class Marathi_Sports_Video(models.Model):
    Cluster_Id = models.IntegerField(db_index=True)
    Video = models.ForeignKey(News_Video)
    VideoId = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Summary = models.CharField(max_length=300)
    Thumbnail = models.URLField(max_length=300,null=True,blank=True)
    Source = models.ForeignKey(Video_Source)
    Published_Date=models.DateTimeField()
    Duration = models.CharField(max_length=50)
    Is_Rep = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.Title,self.URL,self.Source)





