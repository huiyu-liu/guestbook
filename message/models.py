from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField('留言者', max_length=30)
    receipt = models.CharField('收件人', max_length=60)
    subject = models.CharField('留言主題', max_length=128)
    content = models.TextField('留言內容')
    created = models.DateTimeField('留言時間', auto_now_add=True)