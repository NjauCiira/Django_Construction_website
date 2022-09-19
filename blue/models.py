
from django.db import models


class join(models.Model):
    firstname  = models.CharField(max_length=60)
    lname  = models.CharField(max_length=60)
    email  = models.CharField(max_length=60)
    phone  = models.CharField(max_length=60)
    site   = models.CharField(max_length=60)
    other   = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    comment= models.CharField(max_length=200)



    



    
    

    
    
    