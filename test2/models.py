from django.db import models
from test1.models import *

class Comment(models.Model):
    title = models.TextField()
    category = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
