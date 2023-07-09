# exec(open(r"C:\Users\vinit\OneDrive\Documents\Softskill\DjangoProject5\Fifth_Project\relationship\db_shell.py").read())

# from .models import * # KeyError: "'__name__' not in globals"

from relationship.models import Person,Aadhar

# Person.objects.create(name= "Jid", age= 34, mobile= 9828235781, email =" jid@email.com")
# Person.objects.create(name= "ABC", age= 24, mobile= 9828576781, email =" abc@email.com")
# Person.objects.create(name= "tina", age= 22, mobile= 9834035781, email =" tina@email.com")
# Person.objects.create(name= "Guru", age= 20, mobile= 8282357819, email =" guru1@email.com")

# person_list= Person.objects.all()
# print(person_list)
# print(list(person_list))

# p1= Person.objects.get(id=3)
p3= Person.objects.get(id=4)
# print(p1)

from django.utils import timezone
from datetime import date

# 1st method of adding person
# Aadhar.objects.create(aadhar_no=789789920163,address="Thane", date_of_birth=date(1980, 7, 8), person= p1)

# 2nd way of adding person

# Aadhar.objects.create(aadhar_no=262689920163,address="Thane", date_of_birth=date(1988, 7, 8), person_id= 2)

# a1= Aadhar.objects.create(aadhar_no=12389920163,address="Mumbai", date_of_birth=date(1983, 8,25))
# a1.save()   by this we will not get person id

# 3rd way of adding person
# a3= Aadhar.objects.get(aadhar_no =12389920163)
# # print(a3)
# a3.person =p3
# a3.save()

# a4= Aadhar.objects.get(aadhar_no =12389920163)
# print(a4.person)

# to fetch person from aadhar or id(aadhar_object.person)

# a4= Aadhar.objects.get(id= 5)
# print(a4.person)

# to fetch adhar from person(person_object.aadhar)

# p4 = Person.objects.get(id= 3)
# print(p4.aadhar)
# print(p4.aadhar.address)
# print(p4.__dict__)
# print(p4.aadhar.__dict__)



# a5= Aadhar.objects.get(id=1) 
# print(a5.person.name) Jid
# print(a5.person.__dict__)
# {'_state': <django.db.models.base.ModelState object at 0x000001763BE0F5D0>, 'id': 1,
# 'name': 'Jid', 'age': 34, 'mobile': 9828235781, 'email': ' jid@email.com', 'is_active': True}

# print(a5.person.email)  jid@email.com


# Code optimization(to reduce time)











