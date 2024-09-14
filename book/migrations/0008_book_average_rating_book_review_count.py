# Generated by Django 5.1.1 on 2024-09-11 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='book',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
    ]