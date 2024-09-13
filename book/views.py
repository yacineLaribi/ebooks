from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Count

from .forms import NewBookForm, EditBookForm , ReviewForm
from .models import Category, Book , Favorite , Review , Author_Details

def books(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    books = Book.objects.order_by('?')
    categories = Category.objects.annotate(book_count=Count('books'))
    all_books_count = Book.objects.all().count()
    if category_id:
        books = books.filter(category_id=category_id)

    if query:
        books = books.filter(Q(name__icontains=query) | Q(description__icontains=query))


    favorites = []

    if request.user.is_authenticated:
        favorite_books = Favorite.objects.filter(user=request.user).values_list('book_id', flat=True)
        favorites = list(favorite_books)




    return render(request, 'book/books.html', {
        'books': books,
        'query': query,
        'categories': categories,
        'category_id': int(category_id) , 
        'favorites': favorites,
        'all_books_count':all_books_count,
    })

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related_books = Book.objects.filter(category=book.category).exclude(pk=pk)[0:3]
    reviews = book.reviews.all()
    favorites = []

    if request.user.is_authenticated:
        favorite_books = Favorite.objects.filter(user=request.user).values_list('book_id', flat=True)
        favorites = list(favorite_books)

    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(book=book, user=request.user).first()

    if request.method == 'POST' and not user_review:
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()
                return redirect('book:detail', pk=book.id)
        else:
            # Redirect to login if not authenticated
            return redirect('login')
    else:
        form = ReviewForm()

    return render(request, 'book/detail.html', {
        'book': book,
        'related_books': related_books , 
        'favorites' : favorites ,
        'reviews': reviews ,
        'form': form ,
        'user_review': user_review,
    })

@login_required

def new(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            return redirect('book:detail', pk=book.id)
    else:
        form = NewBookForm()

    return render(request, 'book/form.html', {
        'form': form,
        'title': 'New book',
    })

@login_required

def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()

            return redirect('book:detail', pk=book.id)
    else:
        form = EditBookForm(instance=book)

    return render(request, 'book/form.html', {
        'form': form,
        'title': 'Edit book',
    })

@login_required
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()

    return redirect('/')

@login_required
def toggle_favorite(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user = request.user
    
    # Toggle the favorite status
    favorite, created = Favorite.objects.get_or_create(user=user, book=book)
    
    if not created:
        favorite.delete()
        return JsonResponse({'favorite': False})  # Return status for frontend
    
    return JsonResponse({'favorite': True})


def authors(request):
    query = request.GET.get('query', '')
    authors = Author_Details.objects.order_by('?')

    if query:
        authors = authors.filter(Q(name__icontains=query) | Q(description__icontains=query))



    return render(request , "book/authors.html" , {
        'authors': authors ,
        'query': query,
    })