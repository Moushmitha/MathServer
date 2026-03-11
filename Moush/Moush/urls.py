from django.urls import path
from gstapp import views
urlpatterns = [path('', views.calculate_Total, name='Total')]