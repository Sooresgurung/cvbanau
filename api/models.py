from django.db import models

# Create your models here.

class CVform(models.Model):
    name = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=20,null=True)
    clz_name = models.CharField(max_length=200, null=True)
    interest = models.CharField(max_length=100, null=True)
    skill = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=700,null=True)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    
