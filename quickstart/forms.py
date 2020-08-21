from django import forms
from .models import Book,Bookdata,Bookdatatwo
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','title','text')

        
        

class BookdataForm(forms.ModelForm):
    class Meta:
        model = Bookdatatwo
        fields = ('name','title','text')
        
        