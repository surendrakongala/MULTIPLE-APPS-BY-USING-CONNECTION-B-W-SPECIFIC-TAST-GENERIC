from rcb.views import *
from  django.urls import path
app_name='something'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('macha1/',macha1,name='macha1'),
]