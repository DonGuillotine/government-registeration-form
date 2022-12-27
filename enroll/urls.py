from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='first'),
    path('terms', views.terms, name='terms'),
    path('enrol_form', views.enrol, name='enrol_form'),
    path('register', views.register, name='register'),
    path('ajax/load-states/', views.load_stats, name='ajax_load_states'),
    path('ajax/load-lgas/', views.load_lga, name='ajax_load_lgas'),
    path('ajax/load-towns/', views.load_town, name='ajax_load_towns'),
    path('capture', views.capture, name='capture'),
    path('informal', views.informal, name='informal')
]