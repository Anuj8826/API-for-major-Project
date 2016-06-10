from __future__ import unicode_literals

from django.db import models
from authen.models import User
from datetime import datetime

# Create your models here.

class Receipt(models.Model):
    #user = models.ForeignKey(
     #   User, limit_choices_to=dict(groups__name='employee'))
    merchant_name = models.CharField(max_length=200, verbose_name = 'name of the merchant')
    price = models.CharField(max_length=200, verbose_name = 'price')
    date = models.CharField(max_length=200, verbose_name = 'date of receipt', default = datetime.now())
    status_receipt = models.CharField(max_length=200, verbose_name = 'status of receipt', default = 'disapproved')
    receipt = models.ImageField(upload_to='static/', default='default.png')	
    is_active = models.BooleanField(default=True)


    def __unicode__(self):
        return self.merchant_name

    class Meta:
            db_table = 'Receipt'
            verbose_name = 'Receipt'
            verbose_name_plural = 'Receipt'

        
