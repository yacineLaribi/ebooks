from django.core.management.base import BaseCommand
from book.models import Author_Details
import re

class Command(BaseCommand):
    help = 'Clean unwanted characters from Author names and bios'

    def handle(self, *args, **kwargs):
        # Define the patterns for name and bio cleanup
        name_pattern = r'[*:]+'
        bio_image_pattern = r'!\[.*?\]\(.*?\)'  # Matches ![Alt](Image) pattern

        authors = Author_Details.objects.all()
        for author in authors:
            # Clean the name
            cleaned_name = re.sub(name_pattern, '', author.name)
            if cleaned_name != author.name:
                author.name = cleaned_name

            # Clean the bio
            if author.bio:
                cleaned_bio = re.sub(bio_image_pattern, '', author.bio).strip()  # Clean image markdown
                if cleaned_bio != author.bio:
                    author.bio = cleaned_bio

            # Save if any changes were made
            author.save()
            self.stdout.write(self.style.SUCCESS(f'Updated author: {author.name}'))

        self.stdout.write(self.style.SUCCESS('Finished cleaning Author names and bios'))

