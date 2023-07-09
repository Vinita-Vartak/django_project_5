from django.db import models

# Create your models here.

class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.IntegerField()  
    email = models.EmailField()  
  
    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)  
    
    class Meta:
        db_table ="employee"