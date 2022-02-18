
from django.db import models


# Create your models here.
class tech(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=255 ,null=False ,blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',default='SOME STRING')
    video= models.FileField(upload_to='deploy/videos/%Y/%m/%d/', null=True, verbose_name="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
