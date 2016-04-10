from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=255)
    
    def __str__(self):
        return '[' + str(self.student_id) + '] ' + self.student_name

class Tweet(models.Model):
    tweet_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField() 
    date = models.DateField(null=True, blank=False)
    time = models.TimeField(null=True, blank=False)
    reply_to_user = models.BigIntegerField(null=True, blank=True)
    reply_to_user_url = models.CharField(max_length=255,null=True, blank=True)
    retweet_to_user = models.BigIntegerField(null=True, blank=True)
    retweet_to_user_url = models.CharField(max_length=255,null=True, blank=True)
    user_name = models.CharField(max_length=255,null=True, blank=False)
    user_followers = models.BigIntegerField(null=True, blank=False)
    user_location = models.CharField(max_length=255,null=True, blank=True)
    tweet_location = models.CharField(max_length=255,null=True, blank=True)
    hashtags = models.CharField(max_length=255,null=True, blank=True)
    tweet_url = models.CharField(max_length=255,null=True, blank=False)
    tweet_text = models.CharField(max_length=255,null=True, blank=False)
    
    
    def __str__(self):
        return str(self.tweet_id)

HUMORTYPES = ( 'Anekdote',
               'Fantasie',
               'Belediging',
               'Ironie',
               'Grap',
               'Observatief',
               'Quote',
               'Rollenspel',
               'Zelfspot',
               'Vulgariteit',
               'Woordspeling',
               'Overig',
               'Geen')

DISTANCEEB = (  "West-Afrika",
                "Afrika",
                "Europa",
                "Nederland",
                "Noord-Amerika",
                "Overig / geen")

DISTANCEVL = ( "Nederland",
               "Europa",
               "Buiten Europa",
               "Geen locatie")

SOURCE = ( "Overheid",
         "Journalistiek",
         "Burger",
         "Beroemdheid",
         "Instantie",
         "Overig")

CONTENTTYPE = ( "First hand",
                "Second hand",
                "Requesting help",
                "Coordinating relief",
                "Providing counseling",
                "Critizise governement",
                "Memorializing",
                "Discuss causes",
                "Reconnecting members",
                "Misc")

FEAR = (  "Jezelf",
          "Anderen",
          "Jezelf Anderen",
          "Geen")

ATTITUDE = (  'Negatief',
              'Neutraal',
              'Positief')
   
class Annotation_vl(models.Model):
    annotation_id = models.BigIntegerField()
    tweet_id = models.BigIntegerField()
    student_id = models.BigIntegerField()
    is_filled = models.BooleanField(default=False)
    
    humor_type = models.CharField(max_length=50,null=True, blank=True)
    distance = models.CharField(max_length=50,null=True, blank=True)
    source = models.CharField(max_length=50,null=True, blank=True)
    content_type = models.CharField(max_length=50,null=True, blank=True)
    attitude = models.CharField(max_length=50,null=True, blank=True)
    
    class Meta:
        unique_together = (("tweet_id", "student_id"),)
    
    def __str__(self):
        return str(self.student_id) + ' - ' + str(self.tweet_id) + ': ' + self.humor_type
    
class Annotation_eb(models.Model):
    annotation_id = models.BigIntegerField()
    tweet_id = models.BigIntegerField()
    student_id = models.BigIntegerField()
    is_filled = models.BooleanField(default=False)
    
    humor_type = models.CharField(max_length=50,null=True, blank=True)
    distance = models.CharField(max_length=50,null=True, blank=True)
    source = models.CharField(max_length=50,null=True, blank=True)
    content_type = models.CharField(max_length=50,null=True, blank=True)
    fear = models.CharField(max_length=50,null=True, blank=True)
    
    class Meta:
        unique_together = (("tweet_id", "student_id"),)
    
    def __str__(self):
        return str(self.student_id) + ' - ' + str(self.tweet_id) + ': ' + self.humor_type