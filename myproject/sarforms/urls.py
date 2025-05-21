from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('', views.radio_log, name="radiolog"),
    path('logs/', views.radio_log_combined, name='logs'),
    path('edit-form133next/<int:pk>/', views.edit_form133next, name='edit_form133next'),
    path('delete-form133next/<int:pk>/', views.delete_form133next, name='delete_form133next'),
    path('incidenten/', views.incidenten_lijst, name='incidenten'),
]
           