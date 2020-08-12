
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    titles = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titles

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

