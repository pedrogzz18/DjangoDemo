# Generated by Django 4.2.7 on 2023-11-29 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourbooks', '__first__'),
        ('Editoriales', '__first__'),
        ('readers', '0012_alter_ownershare_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Editoriales.books')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourbooks.reader')),
            ],
            options={
                'unique_together': {('book', 'reader')},
            },
        ),
    ]