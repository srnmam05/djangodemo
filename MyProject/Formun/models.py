from django.db import models
from datetime import datetime
# from markdownx.models import MarkdownxField


class Article(models.Model):
    Title = models.TextField(max_length=255, null=False, blank=True)
    Content = models.TextField(max_length=255, null=False, blank=True)
    CreateBy = models.CharField(max_length=255, null=False, blank=True)
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
