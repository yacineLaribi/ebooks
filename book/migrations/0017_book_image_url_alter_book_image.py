# Generated by Django 5.1.1 on 2024-09-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_alter_author_details_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers'),
        ),
    ]
