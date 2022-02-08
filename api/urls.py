from django.urls import path,include
# from . import views
from .views import *



urlpatterns = [
    
    path('persons/', PersonApiView.as_view(),name='person'),
    path('persons/<int:pk>/',PersonDetailView.as_view(),name='person-details'),
]