from django import forms

from .models import Book , Review


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('category', 'name', 'author', 'description', 'image',)


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','author' , 'description', 'image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f'{i} Stars') for i in range(1, 6)], attrs={
                'class': 'flex flex-row-reverse gap-2',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-textarea text-end mt-2 w-[95%] md:w-[50%] border-1 p-6 shadow rounded border-gray-300',
                'placeholder': ' ... اكتب رأيك هنا',
                'rows': 4,
            }),
        }
