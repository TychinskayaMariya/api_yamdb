# Generated by Django 3.2 on 2023-05-29 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_reviews_unique_author_title'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='reviews',
            name='unique_author_title',
        ),
    ]