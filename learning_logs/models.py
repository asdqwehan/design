#coding=utf-8
from django.db import models
from django.contrib.auth.models import User, Permission
# Create your models here.
class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'entries'
        permissions = (
            ('canchange_entry', 'Can change the entries'),
        )

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."

class Comment(models.Model):
    """comments"""
    entry = models.ForeignKey(Entry)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text

class UserPerm(models.Model):
    """user permissions"""
    entry = models.ForeignKey(Entry)
    applicant = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)
