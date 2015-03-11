from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    project_name = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200, null=True)
    repository = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.project_name