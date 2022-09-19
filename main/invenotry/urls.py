from django.contrib import admin
from django.urls import path,include
from . import views
    
urlpatterns = [
    path('', views.home,name="home"),
    path('add_stock/', views.add_stock,name="add_stock"),
    path('add_container/', views.add_container,name="add_container"),
    path('add_firm/', views.add_firm,name="add_firm"),
    path('login/', views.login,name="login"),
    path('update_stock/<int:pk>', views.update_stock, name="update_stock"),
    


    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]