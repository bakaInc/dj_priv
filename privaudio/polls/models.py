from django.db import models

# Create your models here.

#class User(models.Model):
#    #question = models.ForeignKey(User, on_delete=models.CASCADE)
#    #choice_text = models.CharField(max_length=200)
#    #votes = models.IntegerField(default=0)
#    cookie = models.CharField(max_length=200)
#
#    def __str__(self):
#        return self.cookie

class Audio(models.Model):
    audio_record = models.FileField()

class Video(models.Model):
    video_record = models.FileField()

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    
class Message(models.Model):
    #question = models.ForeignKey(Message, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)

    #votes = models.IntegerField(default=0)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    secure_key = models.CharField(max_length=200)

    def __str__(self):
        return self.message_text