from django.urls import path, include
from myapp1 import views

urlpatterns = [
    path('',views.index),
    path('analyze',views.analyze, name="anaylze")
]

 