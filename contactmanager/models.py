from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, related_name='webpages', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    webpage_url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, related_name='accessrecords', on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

