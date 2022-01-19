from django.urls import path
from . import views
urlpatterns = [
    path('persons/', views.PersonApiView.as_view()),
    path('persons/<int:pk>/', views.PersonView.as_view()),
]