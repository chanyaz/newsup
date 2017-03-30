


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
