



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


