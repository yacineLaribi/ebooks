# Generated by Django 5.1.1 on 2024-09-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
            preserve_default=False,
        ),
    ]
