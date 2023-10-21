from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name='home'),
    path('pu/', views.polling_result, name='pu'),
    path('lga/',views.lga_result, name='lga'),
    path('lga/lga_detail/<int:id>/', views.lga_details, name='lga_detail')   
]