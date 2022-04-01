from django.db import models
from PIL import Image
from django.conf import settings
import os
# Create your models here.
class FishRecord(models.Model):
    def nameFile(instance, filename):
       image_name = '/'.join(['images', str(instance.title), filename])
       full_path = os.path.join(settings.MEDIA_ROOT, image_name)

       if os.path.exists(full_path):
            os.remove(full_path)

       return image_name


    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile,blank=True)
    weight= models.IntegerField()
    length= models.IntegerField()
    latitude = models.FloatField(default=0.000000)
    longitude = models.FloatField(default=0.000000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            pic=Image.open(self.image.path)
            pic.thumbnail((140,140),Image.LANCZOS)
            pic.save(self.image.path)
            
    def __str__(self):
        return self.title
