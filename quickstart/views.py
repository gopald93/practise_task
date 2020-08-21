from django.shortcuts import render
from .forms import BookForm,BookdataForm
from .models import Book,Bookdata,Bookdatatwo
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone


def index(request):
    bookdata_obj= Bookdatatwo.objects.all()
    return render(request, 'quickstart/book_details.html', {'bookdata_obj': bookdata_obj})

def book_data_add(request):

    if request.method == "GET":
        print("first=========>")
        print("request.method===>",request.method)
        form = BookdataForm()
        return render(request, 'quickstart/book_data_add.html', {'form': form}) 
    else:
        print("request.method===>",request.method)
        form = BookdataForm(request.POST)
        print("form==>",form)
        if form.is_valid():
            bookdata_obj = form.save(commit=False)
            user_obj=User.objects.get(id=1)
            print(user_obj)
            print("first data")
            # print(form.author_name)
            print(bookdata_obj.title)
            print(bookdata_obj.text)
            # print(bookdata_obj.published_date)
            # print(bookdata_obj.created_date)
            bookdata_obj.author_name = user_obj
            print("second data")
            print(bookdata_obj.author_name)
            bookdata_obj.published_date = timezone.now()
            bookdata_obj.save()
            return redirect('index')

def book_data_edit(request, id=None):
    bookdata_obj = get_object_or_404(Bookdatatwo, pk=id)
    if request.method == "POST":
        form = BookdataForm(request.POST, instance=bookdata_obj)
        if form.is_valid():
            bookdata_obj = form.save(commit=False)
            user_obj=User.objects.get(id=1)
            bookdata_obj.author_name = user_obj
            bookdata_obj.published_date = timezone.now()
            bookdata_obj.save()
            return redirect('index')
    else:
        form = BookdataForm(instance=bookdata_obj)
    return render(request, 'quickstart/book_data_add.html', {'form': form})

def book_data_delete(request, id=None):
    bookdata_obj = get_object_or_404(Bookdatatwo, pk=id)
    if request.method == 'POST':
        bookdata_obj.delete()
        return redirect('index')
    else:
        context = {}
        context['bookdata_obj'] = bookdata_obj
        return render(request, 'quickstart/book_data_delete.html', context)