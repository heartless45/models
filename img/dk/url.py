from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('ime/',views.a,name='a')

]
