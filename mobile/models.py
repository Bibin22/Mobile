from django.db import models

# Create your models here.

class Mobile(models.Model):
    mobile_company = models.CharField(max_length=50, unique=True)
    mobile_name = models.CharField(max_length=50)
    mobile_spec = models.TextField()
    mobile_price = models.IntegerField(default=1000)

    def __str__(self):
        return self.mobile_name