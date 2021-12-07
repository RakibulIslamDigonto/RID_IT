from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class NewUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='related_user')
    full_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='crud_app/', blank=True)

    def __str__(self):
        return self.full_name

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
