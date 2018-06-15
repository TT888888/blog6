from django.db import models

# Create your models here.

# 文章
class Article(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

#评论
class Comment(models.Model):
    aid = models.IntegerField()
    name = models.CharField(max_length=128,blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

#
# # 标签
# class tog(models.Model):
#     name = models.CharField(max_length=128)
#
#
# # 建立Article与tog多对多的表
# class ArticleTage(models.Model):
#
#     aid = models.IntegerField()
#     tid = models.IntegerField()


