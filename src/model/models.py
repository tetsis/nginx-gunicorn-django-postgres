from django.db import models

# Create your models here.
lass Table(models.Model):
    name = models.CharField(max_length=128, default='')
    access_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
