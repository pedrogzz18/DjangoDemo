# Generated by Django 4.1.13 on 2023-11-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourbooks', '__first__'),
        ('Editoriales', '__first__'),
        ('readers', '0008_alter_ownership_book_owner_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourbooks.reader')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Editoriales.books')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourbooks.reader')),
            ],
            options={
                'unique_together': {('reader', 'book')},
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Editoriales.books')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourbooks.reader')),
            ],
            options={
                'unique_together': {('reader', 'book')},
            },
        ),
        migrations.DeleteModel(
            name='Ownership',
        ),
        migrations.AddField(
            model_name='ownershare',
            name='share',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='readers.share'),
        ),
    ]
