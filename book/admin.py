
from django.contrib import admin

from .models import Category, Book , Review , Author_Details

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Review)

admin.site.register(Author_Details)

