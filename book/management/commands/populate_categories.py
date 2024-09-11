from django.core.management.base import BaseCommand
from book.models import Category

class Command(BaseCommand):
    help = 'Populate categories from a text file'

    def handle(self, *args, **kwargs):
        with open('categories.txt', 'r', encoding='utf-8') as file:
            for line in file:
                english_name, arabic_name = line.strip().split(' - ')
                
                category_name = f"{english_name} - {arabic_name}"
                
                # Check if the category already exists
                if not Category.objects.filter(name=category_name).exists():
                    Category.objects.create(name=category_name)
                    self.stdout.write(self.style.SUCCESS(f"Added category: {category_name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Category already exists: {category_name}"))
