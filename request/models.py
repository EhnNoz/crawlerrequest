from django.db import models





class Request(models.Model):
    keyword=models.CharField(verbose_name = 'KeyWord', max_length=200, blank=False, null=True, unique=True)
    res_id=models.IntegerField(verbose_name = 'Res_Id', blank=False, null=True, unique=True)
#    active=models.BooleanField(verbose_name = 'Active', default=True)

