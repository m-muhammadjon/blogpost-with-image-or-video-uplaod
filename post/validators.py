import os
from django.core.exceptions import ValidationError


def validate_video_photo(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.mp4']
    # print(ext)
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
