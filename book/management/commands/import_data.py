import csv
from django.core.management.base import BaseCommand
from book.models import Book 

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def handle(self, *args, **kwargs):
        file_path = '../scraping/books_info_with_images.csv'  

        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Example fields from CSV row to model fields
                obj, created = Book.objects.update_or_create(
                    name=row['Title'],
                    author=row['Creator'],
                    description = row['Description'],
                    link = row['Link'],
                    image_url = row['Cover Image'],
                    subject = row['Categories'],
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created: {obj}'))
                else:
                    self.stdout.write(f'Updated: {obj}')
