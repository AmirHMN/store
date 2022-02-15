from django.core.validators import ValidationError


def image_size_validator(file):
    MAX_IMAGE_SIZE = 50
    if file.size > MAX_IMAGE_SIZE * 1024:
        raise ValidationError(f'image cannot be larger than {MAX_IMAGE_SIZE}KB!')
