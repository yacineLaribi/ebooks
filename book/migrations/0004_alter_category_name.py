# Generated by Django 5.1.1 on 2024-09-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]