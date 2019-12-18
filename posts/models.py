from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reference_link = models.URLField(max_length=200, blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
