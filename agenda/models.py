from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=55)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    cover = models.ImageField(
        upload_to='contact/covers/%Y/%m/%d/', blank=True, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
