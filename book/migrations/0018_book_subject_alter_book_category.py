# Generated by Django 5.1.1 on 2024-09-20 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_book_image_url_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.category'),
        ),
    ]
