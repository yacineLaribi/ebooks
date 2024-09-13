import csv
import os
from django.core.management.base import BaseCommand
from book.models import Author_Details

class Command(BaseCommand):
    help = 'Imports authors from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import authors from')
        parser.add_argument('image_folder', type=str, help='The folder containing author images')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        image_folder = kwargs['image_folder']

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name']
                bio = row['bio']
                image_name = row['image']  # Assuming your CSV has the image filename

                image_path = os.path.join(image_folder, image_name)
                if os.path.exists(image_path):
                    image_file = image_path
                else:
                    image_file = None

                author, created = Author_Details.objects.get_or_create(
                    name=name,
                    defaults={
                        'bio': bio,
                        'image': image_file
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Author "{name}" created'))
                else:
                    self.stdout.write(self.style.WARNING(f'Author "{name}" already exists'))
