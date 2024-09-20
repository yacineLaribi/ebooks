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
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE , blank=True , null=True)
    subject = models.CharField(max_length=255 , blank=True , null = True ) 
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pages = models.IntegerField(blank=True , null=True)
    link= models.URLField()
    image = models.ImageField(upload_to='book_covers',  blank=True, null=True) 
    image_url = models.URLField(null=True , blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    

    # Rating fields  
    average_rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    
    def total_favorites(self):
        return Favorite.objects.filter(book=self).count()
    
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
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.book.name}'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the book's average rating and review count
        reviews = self.book.reviews.all()
        total_reviews = reviews.count()
        total_rating = sum([review.rating for review in reviews])
        
        self.book.average_rating = total_rating / total_reviews
        self.book.review_count = total_reviews
        self.book.save()



class Author_Details (models.Model):
    name = models.CharField(max_length=250 , null= False , blank= False)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='author_pics', blank=True, null=True) 
    books = models.ManyToManyField( Book, verbose_name="author_book" , blank=True )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        return self.name
