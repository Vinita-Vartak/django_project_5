from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length= 100)
    age  = models.IntegerField()
    mobile = models.BigIntegerField(null= True, unique= True)
    email = models.EmailField(unique= True)
    is_active = models.BooleanField(default= True)
    
    def __str__(self):
        return self.name
    

    
    class Meta:
        db_table ="Person"
        
class Aadhar(models.Model):
    aadhar_no = models.BigIntegerField(unique= True)
    address = models.CharField(max_length= 100)
    created_date = models.DateTimeField(auto_now= True) # automatically itb will take dat and time
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default= True)
    # person = models.OneToOneField(Person, on_delete= models.CASCADE) # if we delete person adhar also get deleted
    person = models.OneToOneField(Person, on_delete= models.CASCADE, null= True)
    updated_date = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        # return self.aadhar_no
        return str(self.aadhar_no) #this is used to show adhar no 
    
    
    class Meta:
        db_table = "aadhar"