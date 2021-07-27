from django.db import models
from .validators import validate_video_photo


class Post(models.Model):
    CHOICES = (
        ('video', 'video'),
        ('photo', 'photo')
    )
    title = models.CharField(max_length=200)
    img_or_vid = models.FileField(upload_to='files/', validators=[validate_video_photo])
    body = models.TextField()
    type = models.CharField(max_length=20, choices=CHOICES, null=True, blank=True, default='photo')

    def __str__(self):
        return self.title
