from django.db import models

class Posts(models.Model):
    id = models.AutoField(
        auto_created = True,
        primary_key = True,
        serialize = False, 
        verbose_name ='ID'
    )
    title = models.CharField(max_length=255)
    text = models.TextField()