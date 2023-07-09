from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render

from app5.models import Book

@login_required
def welcome_page(request):  
    return render(request, "welcome.html")

import datetime

@login_required
def show_all_books(request):
    books = Book.objects.filter(is_active=True)  
    return render(request, "showbooks.html", {"allbooks": books, "today": datetime.datetime.now()})

@login_required
def show_single_book(request, bid): 
    try:
        book_obj = Book.objects.get(id=bid) 
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist..!")
    return render(request=request, template_name="bookdetail.html", context={"book": book_obj})

def common_var(req):
    final_dict = req.POST
    book_name = final_dict.get("nm")
    book_price = final_dict.get("prc")
    book_qty = final_dict.get("qty")
    book_is_pub = final_dict.get("ispub")
    return book_name, book_price, book_qty, book_is_pub

@login_required # type: ignore
def add_single_book(request):
           
    if request.method == "POST":
        book_name, book_price, book_qty, book_is_pub = common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
        Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_published=is_pub)
        messages.success(request, f"Book has been added Suceesfully..!")
        return redirect("show_books")
    

    elif request.method == "GET":
                
        return render(request, "addbook.html")
    
    
    
    
@login_required
def edit_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    if request.method == "GET":
        return render(request, "bookedit.html", {"single_book": book_obj})
    elif request.method == "POST":
        book_name, book_price, book_qty, book_is_pub = common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
        # for updating the data of books
        book_obj.name = book_name
        book_obj.price = book_price
        book_obj.qty = book_qty
        book_obj.is_published = is_pub
        book_obj.save()
        messages.success(request, f"Book:{book_obj.name} has been Updated Suceesfully..!") 
        return redirect("show_books")

@login_required
def delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.delete()  # hard delete
    return redirect("show_books")

@login_required
def soft_delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.is_active = False   # soft delete
    book_obj.save()
    messages.info(request,"Book deleted Successfully..")
    return redirect("show_books")

@login_required
def show_inactive_books(request):
    books = Book.objects.filter(is_active=False)  
    return render(request, "showinactivebook.html", {"allbooks": books, "today": datetime.datetime.now()})

#********************************************************************************************************
from app5.forms import AddressForm, BookForm, GeeksForm

# def form_view(request):
#     context ={}
#     context['form']= GeeksForm()
#     return render(request, "form_test.html", {"form": GeeksForm})

# def form_view(request):
#     context ={}
#     context['form']= GeeksForm()
#     return render(request, "form_test.html", {"form": BookForm})

# def form_view(request):
#     context ={}
#     context['form']= GeeksForm()
#     return render(request, "form_test.html", {"form": AddressForm})

# def form_view(request):
#     if request.method == "POST":
#                 # pass
#         print("IN POST Request")
#         data = request.POST
#         print(data)    #It will return None
#         return HttpResponse("All is ok")
    
# After submitting form ,we will get output as below
#     IN POST Request
# <QueryDict: {'csrfmiddlewaretoken': ['N0YeQ7Qa8RMtqPDHfHVIFgOlyqUOShRbJTGQ2j0IMGfVONTQjYEvaNPQPPS5K6o2'],
# 'name': ['Book_14'], 'price': ['344'], 'qty': ['5'], 'is_published': ['on']}>


# After submitting form ,we will get output as below if "is_published" is unchecked

# IN POST Request
# <QueryDict: {'csrfmiddlewaretoken': ['InlA3hPx4G7w0g7u41rPXIivBnTd0sDsEg3cftZ5IvAYoenD8iaCsfj0SMRuShaj'], 
# 'name': ['Book_17'], 'price': ['76'], 'qty': ['4']}>

    # elif request.method == "GET":
    #     print("GET request")
    #     return render(request, "book_form_test.html", {"bookform": BookForm})
  
# for below program o/p will be same only it will chk wheather data valid or not.  
# def form_view(request):
#     if request.method == "POST":
#                 # pass
#         print("IN POST Request")
#         data = request.POST
#         form= BookForm(data)
#         if form.is_valid():
#             print("For If condition")
#         return HttpResponse("All is ok")
#     elif request.method == "GET":
#         print("GET request")
#         return render(request, "book_form_test.html", {"bookform": BookForm})
    
# to get data in mysql database as well as in show active books, so redirect used so that after entering 
# it will go to show_active books

def form_view(request):
    if request.method == "POST":
                # pass
        print("IN POST Request")
        data = request.POST
        form= BookForm(data)
        if form.is_valid():
            form.save()
        # return HttpResponse("All is ok")
        return redirect("show_books")
    elif request.method == "GET":
        print("GET request")
        return render(request, "book_form_test.html", {"bookform": BookForm})
    
    
#****************************************************************************

# to create csv file of books
#1. create nav bar & url
#2. create object and write the following program

from django.http import HttpResponse
import csv

def create_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['content-Disposition'] = 'attachment; filename = "test.csv"'
    
    writer= csv.writer(response)
    writer.writerow(['name', 'price', 'qty','is_published','is_active'])
    
    books = Book.objects.all().values_list('name', 'price', 'qty','is_published','is_active')
    for book in books:
        writer.writerow(book)
    return response
    
    
# def upload_csv(request):
#     file=request.FILES["csv_file"]
#     print(file)
#     return HttpResponse("Success") by this after uploading we can see only sucess


# by this we can read the data in console
# def upload_csv(request):
#     file=request.FILES["csv_file"]
#     data = file.read().decode('utf-8').splitlines()
#     print(data)
#     return HttpResponse("Success")
   
#    ['name,price,qty,is_published', 'Book_101,450,5,TRUE', 'Book_102,450,10,TRUE', 
#     'Book_103,667,15,TRUE', 'Book_104,567,20,FALSE', 'Book_105,362,25,FALSE', 'Book_106,789,30,TRUE', 
#     'Book_107,898,35,TRUE', 'Book_108,345,40,TRUE', 'Book_109,568,45,FALSE', 'Book_110,434,50,FALSE']


# to upload csv data into database

# def upload_csv(request):
#     file=request.FILES["csv_file"]
    
#     decoded_file = file.read().decode('utf-8').splitlines()
#     reader = csv.DictReader(decoded_file)
#     for i in reader:
#         print(i)
#     # print(reader)
#     return HttpResponse("Success")


# {'name': 'Book_101', 'price': '450', 'qty': '5', 'is_published': 'TRUE'}
# {'name': 'Book_102', 'price': '450', 'qty': '10', 'is_published': 'TRUE'}
# {'name': 'Book_103', 'price': '667', 'qty': '15', 'is_published': 'TRUE'}
# {'name': 'Book_104', 'price': '567', 'qty': '20', 'is_published': 'FALSE'}
# {'name': 'Book_105', 'price': '362', 'qty': '25', 'is_published': 'FALSE'}
# {'name': 'Book_106', 'price': '789', 'qty': '30', 'is_published': 'TRUE'}
# {'name': 'Book_107', 'price': '898', 'qty': '35', 'is_published': 'TRUE'}
# {'name': 'Book_108', 'price': '345', 'qty': '40', 'is_published': 'TRUE'}
# {'name': 'Book_109', 'price': '568', 'qty': '45', 'is_published': 'FALSE'}
# {'name': 'Book_110', 'price': '434', 'qty': '50', 'is_published': 'FALSE'}

# to upload csv data into database

# def upload_csv(request):
#     file=request.FILES["csv_file"]
    
#     decoded_file = file.read().decode('utf-8').splitlines()
#     reader = csv.DictReader(decoded_file)
#     lst = []
#     for element in reader:
#         is_pub = element.get("is_published")
#         if is_pub == "TRUE":
#             is_pub = True
#         else:
#             is_pub = False
            
#         lst.append(Book(name=element.get("name"), price= element.get("price"), qty=element.get("qty"), is_published= is_pub))
#         # Book(name=element.["name"], price= element.get("price"), qty=element.get("qty"), is_published=element.get("is_pub"))
#     # print(lst)
#     # [<Book: Book_101>, <Book: Book_102>, <Book: Book_103>, <Book: Book_104>, 
#     #  <Book: Book_105>, <Book: Book_106>, <Book: Book_107>, <Book: Book_108>, <Book: Book_109>, <Book: Book_110>]
#     Book.objects.bulk_create(lst)
#     return HttpResponse("Success")

# lst = ['name,price,qty,is_published', 'Book_101,450,5,TRUE', 'Book_102,450,10,TRUE', 
#     'Book_103,667,15,TRUE', 'Book_104,567,20,FALSE', 'Book_105,362,25,FALSE', 'Book_106,789,30,TRUE', 
#     'Book_107,898,35,TRUE', 'Book_108,345,40,TRUE', 'Book_109,568,45,FALSE', 'Book_110,434,50,FALSE']
# list(map(lambda x: x.split(","), lst))


def upload_csv(request):
    file=request.FILES["csv_file"]
    
    decoded_file = file.read().decode('utf-8').splitlines()
    expected_header_lst = ["name","price","qty","is_published"]
    expected_header_lst.sort()
    
    actual_header_lst= decoded_file[0].split(",")
    actual_header_lst.sort()
    
    print(expected_header_lst, actual_header_lst)
    if expected_header_lst != actual_header_lst:
        return HttpResponse("Header are not equal...")
    # if we cahnge csv header u will get above error
    reader = csv.DictReader(decoded_file)
    lst = []
    for element in reader:
        is_pub = element.get("is_published")
        if is_pub == "TRUE":
            is_pub = True
        else:
            is_pub = False
            
        lst.append(Book(name=element.get("name"), price= element.get("price"), qty=element.get("qty"), is_published= is_pub))
        # Book(name=element.["name"], price= element.get("price"), qty=element.get("qty"), is_published=element.get("is_pub"))
    # print(lst)
    # [<Book: Book_101>, <Book: Book_102>, <Book: Book_103>, <Book: Book_104>, 
    #  <Book: Book_105>, <Book: Book_106>, <Book: Book_107>, <Book: Book_108>, <Book: Book_109>, <Book: Book_110>]
    Book.objects.bulk_create(lst)
    return HttpResponse("Success")
