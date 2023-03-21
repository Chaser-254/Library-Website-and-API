from django.shortcuts import render
from .models import Book
from django.views.generic import ListView

class BookView(ListView):
    model = Book
    template_name = 'book_list.html'
