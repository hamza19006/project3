from django.shortcuts import render, redirect
from .models import book

# Create your views here.
def hello(request) :
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        date = request.POST['date']
        Book = book(title = title , author = author , date = date)
        Book.save()
        return redirect('/')
    else:
        return render(request, 'index.html')