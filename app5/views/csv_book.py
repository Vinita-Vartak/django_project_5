from django.shortcuts import render,HttpResponse

# splitting views for systematic arrangement

def view_c(request):
    return HttpResponse("view_c")

def view_d(request):
    return HttpResponse("view_d")