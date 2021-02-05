from django.db import models
from datetime import datetime
  
class Mood(models.TextChoices): 
    crying = '😢'
    sad = '🙁'
    neutral = '😐'
    happy = '🙂'
    grin = '😁'

class MediaType(models.TextChoices): 
    audio = 'a'
    video = 'v'
    picture = 'p'
    fileType = 'f'


class JournalEntry(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    date = models.DateTimeField()
    mood = models.CharField(max_length=1, choices=Mood.choices,default=Mood.crying)
    longitude = models.CharField(max_length=64)
    latitude = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"
    

class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"
  
class Media(models.Model):
    name = models.CharField(max_length=64)
    filePath = models.FileField(upload_to='%Y/%m/%d/')
    mediaType = models.CharField(max_length=1, choices=MediaType.choices,default=MediaType.fileType)
    entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)

class EntryTag(models.Model):
    class Meta:
        unique_together = (('entry', 'tag'),)
    
    entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)