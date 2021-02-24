# Used the code from the Code Institute Project - Boutique Ado -

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile')
]