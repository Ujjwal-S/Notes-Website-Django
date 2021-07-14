from django.urls import path
from . import views
from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.http import HttpResponse

urlpatterns = [
    path('search/', views.search_notes, name="search_notes"),
    path('my_notes/', views.my_notes, name="my_notes"),
    path('get_my_notes/', views.get_my_notes, name="get_my_notes"),  # this just returns a list of users purchased notes - id -
    path('invalid_purchase/', views.invalid_purchase, name="invalid_purchase"),

    path('<str:std>/', views.standard_notes, name="standard_notes"),
    path('view_notes/<str:pdf_id>/', views.view_notes, name="standard_notes"),
]