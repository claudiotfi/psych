from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class PostTag(models.Model):
    tag_id = models.BigIntegerField()
    post_id = models.BigIntegerField()
