
# Create your models here.


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

