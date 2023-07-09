"""B9_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from app5.views import (add_single_book, delete_single_book, edit_single_book,
#                         form_view, show_all_books, show_inactive_books,
#                         show_single_book, soft_delete_single_book,
#                         welcome_page)
# from user_app import views

from user_app import views as user_views

# from user_app.views import register_request

# import app5.views

from app5 import views




urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("home/", welcome_page, name="home_page"),
    # path("show-books/", show_all_books, name="show_books"),
    # path("show-single-book/<int:bid>/", show_single_book, name="show_single_book"),
    # path("add-book/", add_single_book, name="add_single_book"), # type: ignore
    # path("edit-book/<int:bid>/", edit_single_book, name="edit_single_book"), # type: ignore
    # path("delete-book/<int:bid>/", delete_single_book, name="delete_single_book"),
    # path("soft-delete-book/<int:bid>/", soft_delete_single_book, name="soft_delete_single_book"),
    # path("show-inactive-books/", show_inactive_books, name="show_inactive_books"),
    # path("form-view/", form_view, name="form_view"),  # type: ignore
    
    # # user_app urls
    # path("user-signup/", views.user_signup, name ="user-signup"),  # type: ignore
    
    
    path('admin/', admin.site.urls),
      
                
   
    
    # library url
    
    path('book/',include('app5.urls')),

    # user_app urls
    path('user/', include('user_app.urls')),
    
    path("views-a/", views.view_a, name = "view_a"),
    
    path('cbv/', include('cbv_app.urls')),
    
   

]

# <!--  <form method = "post">
# 	{% csrf_token %}
# 	{{form }}
# 	<input type="submit" value = "Submit">
# </form> 

#  <form method = "post">
# 	{% csrf_token %}
# 	<table>{{ form.as_table }}</table>
# 	<input type="submit" value = "Submit">
# </form>  -->


# <!-- {% block content %}
# <form method = "post">
# 	{% csrf_token %}
# 	<table>{{ form| crispy }}</table>
# 	<input type="submit" value = "Submit">
# </form>  -->

# <!-- <form method="post">
#     {% csrf_token %}
#     <div class="form-row">
#       <div class="form-group col-md-4 mb-0">
#         {{ form.email|as_crispy_field }}
#       </div>
#       <div class="form-group col-md-6 mb-0">
#         {{ form.password|as_crispy_field }}
#       </div>
#     </div>
#     {{ form.address_1|as_crispy_field }}
#     {{ form.address_2|as_crispy_field }}
#     <div class="form-row">
#       <div class="form-group col-md-6 mb-0">
#         {{ form.city|as_crispy_field }}
#       </div>
#       <div class="form-group col-md-4 mb-0">
#         {{ form.state|as_crispy_field }}
#       </div>
#       <div class="form-group col-md-2 mb-0">
#         {{ form.zip_code|as_crispy_field }}
#       </div>
#     </div>
#     {{ form.check_me_out|as_crispy_field }}
#     <button type="submit" class="btn btn-primary">Sign in</button>
#   </form> -->

