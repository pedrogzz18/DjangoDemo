# Generated by Django 4.1.13 on 2023-11-27 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourbooks', '__first__'),
        ('readers', '0011_alter_ownershare_share'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ownershare',
            unique_together={('share', 'book_owner')},
        ),
    ]
