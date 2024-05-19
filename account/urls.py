from django.urls import path
from .views import main_view
from .views import main_view, passport_view
from . import views

urlpatterns = [
    path('', main_view, name='main'),
    path('passport/', passport_view, name='passport'), 
    path('save_passport/', views.save_passport_mo, name='save_passport'),
    path('reference_info/', views.reference_info, name='reference_info'),
]
