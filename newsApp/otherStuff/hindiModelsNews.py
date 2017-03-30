

# Create your models here.


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

