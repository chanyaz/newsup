


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
