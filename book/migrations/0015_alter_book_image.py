# Generated by Django 5.1.1 on 2024-09-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_alter_author_details_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='40.jpg', null=True, upload_to='book_covers'),
        ),
    ]
