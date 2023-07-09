from django.urls import path  
from cbv_app.views import NewView ,EmployeeCreate ,EmployeeList,EmployeeDetailView
  
urlpatterns = [  
    path('new-cview/', NewView.as_view()),  
    path('emp-create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('emp-list/', EmployeeList.as_view()),
    path('emp-view/<pk>/', EmployeeDetailView.as_view()),
]  



  
