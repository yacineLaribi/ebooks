# Generated by Django 5.1.1 on 2024-09-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_alter_author_details_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_details',
            name='books',
            field=models.ManyToManyField(blank=True, null=True, to='book.book', verbose_name='author_book'),
        ),
    ]
