from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avtar=models.ImageField(upload_to='customer/image',blank=True,null=True)
    strip_customer_id=models.CharField(max_length=50,blank=True,null=True)
    strip_payment_method_id=models.CharField(max_length=50,null=True,blank=True)
    strip_card_last4=models.CharField(max_length=50,null=True,blank=True)



    def __str__(self):
        return self.user.username
    
