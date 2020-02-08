from django.urls import path,include
from .views import show,edit,delete,add

urlpatterns=[
    path('',show.as_view(),name="show"),
    path('add/',add.as_view(),name="book-add"),
    path('edit/<int:pk>/',edit.as_view(),name="book-edit"),
    path('delete/<int:pk>/',delete.as_view(),name="book-delete"),
]