from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text

class Responses(models.Model):
    user = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    nystagmus_present = models.CharField(max_length=50)
    video_link = models.CharField(max_length=200)

"""
class Video(models.Model):
    video_link = models.CharField(max_length=200)
    test_type = models.CharField(max_length=100)
    video_filename = models.CharField(max_length=100)
    amplitude_level = models.IntegerField(blank=True)
    face = models.CharField(max_length=100, blank=True)
    num_nystagmus_events = models.IntegerField(blank=True)
    hgn_max_side = models.CharField(max_length=50,blank=True)
"""
