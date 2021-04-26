from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, default='username', verbose_name='Customer Name')
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    mobile = models.CharField(max_length=15)

    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name + "-" + self.password