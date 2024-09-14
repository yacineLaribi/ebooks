import os
import re
from django.core.management.base import BaseCommand
from book.models import Author_Details

class Command(BaseCommand):
    help = 'Import authors from a Markdown file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        authors = re.split(r'\n---\n', content)
        for author_block in authors:
            lines = author_block.strip().split('\n')
            if len(lines) < 2:
                continue

            name = lines[0].strip()
            bio = '\n'.join(lines[1:]).strip()

            # Extract image filename from bio text
            match = re.search(r'!\[.*?\]\((.*?)\)', bio)
            if match:
                image_filename = match.group(1)
                # Update the image filename if it has a relative path
                if not image_filename.startswith('author_pics/'):
                    image_filename = f'author_pics/{image_filename}'
            else:
                image_filename = None

            # Create or update author details
            author, created = Author_Details.objects.get_or_create(
                name=name,
                defaults={'bio': bio, 'image': image_filename}
            )

            if not created:
                author.bio = bio
                if image_filename:
                    author.image = image_filename
                author.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully imported author: {name}'))
