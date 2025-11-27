from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from .forms import *

# Create your views here.
def book_list(request):
    book_list = Book.objects.all().order_by('-created_at')  
    paginator = Paginator(book_list, 2)                    
    page_num = request.GET.get('page')
    books = paginator.get_page(page_num)
    return render(request, "books/book_list.html", {"books": books})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
        return render(request, "books/book_create.html", {"form" : form})
    
def book_delete(request, pk):
    book =get_object_or_404(Book, pk = pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    else:
        return render(request, "books/book_delete.html", {"book" : book})
    
def book_update(request, pk):
    book =get_object_or_404(Book, pk = pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
        return render(request, "books/book_create.html", {"form" : form})