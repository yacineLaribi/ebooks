from django.urls import path , include

from . import views

app_name = 'book'

urlpatterns = [
    path('',views.books, name='books'),
    path('<int:pk>/',views.detail, name='detail'),
    path('new/',views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('toggle-favorite/<int:book_id>/', views.toggle_favorite, name='toggle_favorite'),

    #Authors part 
    path('authors/',include([
        path('',views.authors, name='authors'),
        path('<int:pk>/',views.author_detail, name='author_detail'),
        path('new/', views.author_new, name='author_new'),
        path('<int:pk>/edit/', views.author_edit, name='author_edit'),
        

    ])),




]