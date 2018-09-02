from django.urls import path
from .import views


app_name = 'employee_management_system'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
