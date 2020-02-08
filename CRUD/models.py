from django.db import models
from django.contrib.auth.models import User
from django import forms

class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    thumbnail=models.FileField(upload_to="CRUD/",blank=True,null=True)
    objects=models.Manager
    def __str__(self):
        return self.title

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
