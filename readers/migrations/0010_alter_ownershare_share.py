# Generated by Django 4.1.13 on 2023-11-27 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0009_ownershare_purchase_share_delete_ownership_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownershare',
            name='share',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readers.share'),
        ),
    ]
