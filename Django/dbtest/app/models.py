from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField('名字',max_length=200)

    class Meta:
        verbose_name ='名字'
        verbose_name_plural=verbose_name
    
    def __str__(self):
        return self.name
