from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.


class NewView(View):  
    def get(self, request): 
        print("in get method") 
        return HttpResponse('get response')  #request =200 ok
    
    # def post(self, request): # Postman is used to test end points
    #     print(request.POST)
    #     print("in post method") 
    #     return HttpResponse('post response')   # request 201---data created
    
# This o/p will come after hitting in postman
# 
# <QueryDict: {}>
# in post method

# in postman go to body----form-data and after inserting and hitting we will get o/p

# <QueryDict: {'name': ['Vinita'], 'age': ['34']}>
# in post method

    def post(self, request): 
        data= request.POST
        name= data.get("name")    
        age= data.get("age")
        
        print("in post method") 
        return HttpResponse('post response',status= HTTPStatus.CREATED) #resource created



    
# from .forms import EmployeeForm  
from django.views.generic.edit import CreateView

from .models import Employee


class EmployeeCreate(CreateView):  
    model = Employee  
    fields = '__all__'  
    success_url= "http://127.0.0.1:8000/cbv/emp-create/"   # it will redirect to that page after submitting the form.
    
# http://127.0.0.1:8000/cbv/emp-create/ it will create the form directly without creating form


# ListView(https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/?ref=lbp)

# ListView used to see all records
from django.views.generic.list import ListView


class EmployeeList(ListView):
    model = Employee
    context_object_name= "all_employees" # to change the name of object_list
    # queryset = Employee.objects.filter(is_active =1) it should have filted data
    
    # ordering = "id"
    # ordering = "email"
    
    ordering = "-email" # for descending
    
# DetailView

# it is used to see single record

from django.views.generic.detail import DetailView


class EmployeeDetailView(DetailView):
    model = Employee   # query for this Employee.objects.get(id= 3)
    context_object_name= "single_employee"

# if the id is not there, it will give error so if we want to change it
# go to DetailView---BaseDetailView
# following code copied ,as it is present in BaseDetailView ,I copied in EmployeeDetailView, it called Overridden method
# now it will run here only as get request provided in EmployeeDetailView

    # def get(self, request, *args, **kwargs):
    #     try:
    #         self.object = self.get_object()
    #         print(self.object)
    #     except Employee.DoesNotExist:
    #         return HttpResponse("No Data Found in databse")
    #     # print(self.object) Nita D
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)
    
# by above code it is not showing message

# change the below code by exception handling
    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.

        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            return "No Data"
            # raise Http404(
            #     _("No %(verbose_name)s found matching the query")
            #     % {"verbose_name": queryset.model._meta.verbose_name}
            # )
        return obj
    
    def get(self, request, *args, **kwargs):  
        self.object = self.get_object()
        print(type(self.object)) #if id is not there it will give,<class 'str'>
        if type(self.object) == str:
            return HttpResponse("No data in database")              
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)





    
    
 
