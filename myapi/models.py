from django.db import models

# Create your models here.



from django.db import models
from django.utils import timezone


class MyData(models.Model):
    slack_name = models.CharField(max_length=255, default='')
    track = models.CharField(max_length=255, default='backend')
    current_day = models.CharField(
        max_length=255, default=timezone.now().strftime('%A'))
    utc_time = models.DateTimeField(default=timezone.now)
    github_file_url = models.URLField(default='')
    github_repo_url = models.URLField(default='')
    status_code = models.IntegerField(default=200)
