from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1500)
    image = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
