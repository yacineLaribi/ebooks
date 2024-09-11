from django.db import models
from core.models import CustomUser as User
class Category(models.Model):
    name = models.CharField(max_length=255 ,  unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link= models.URLField()
    image = models.ImageField(upload_to='book_covers', blank=True, null=True) 

    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'book')  # Prevent duplicates
        
class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.book.name}'
    
