from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class PostTag(models.Model):
    tag_id = models.BigIntegerField()
    post_id = models.BigIntegerField()
