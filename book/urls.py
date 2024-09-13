from django.urls import path

from . import views

app_name = 'book'

urlpatterns = [
    path('',views.books, name='books'),
    path('<int:pk>/',views.detail, name='detail'),
    path('new/',views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('toggle-favorite/<int:book_id>/', views.toggle_favorite, name='toggle_favorite'),

    path('authors/',views.authors, name='authors'),

]