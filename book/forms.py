from django import forms

from .models import Book


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('category', 'name', 'author', 'description', 'image',)


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','author' , 'description', 'image')
