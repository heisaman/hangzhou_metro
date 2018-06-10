from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clean/', views.clean, name='clean'),
    path('ajax/line_trains/', views.line_trains, name='line_trains'),
    path('save/', views.save, name='clean_record_save'),
]