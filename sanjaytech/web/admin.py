
from django.contrib import admin
from .models import tech



@admin.register(tech)
class techmodel(admin.ModelAdmin):
    list_filter = ('title','name','date_added')
    list_display =('title','name','date_added')





# title = models.CharField(max_length=250)
   # name = models.CharField(max_length=255 ,null=False ,blank=False)
   # description = models.TextField()
   # video = models.TextField()
    #image = models.ImageField(upload_to='images/',default='SOME STRING')
    #video= models.FileField(upload_to='deploy/videos/%Y/%m/%d/', null=True, verbose_name="")
    #date_added = models.DateTimeField(auto_now_add=True)
