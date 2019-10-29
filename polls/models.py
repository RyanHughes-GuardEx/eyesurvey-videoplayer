from django.db import models
from datetime import datetime as dt

class Question(models.Model):
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text


class Responses(models.Model):
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nystagmus_present = models.CharField(max_length=50)
    video_link = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=0)

    @classmethod
    def create_response(cls, user=None, nystagmus=None, video=None, question=1):
        resp = cls(user=user, nystagmus_present=nystagmus, video_link=video,
                   question=question, created_at=dt.now(), updated_at=dt.now())
        return resp

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
