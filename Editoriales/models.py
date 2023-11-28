from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length = 100)
    pages = models.IntegerField()
    publication_year = models.CharField(max_length=30)
    description = models.CharField(max_length = 300)
    image_url = models.CharField(max_length=30000)
    author_first_name = models.CharField(max_length = 40)
    author_last_name = models.CharField(max_length=40)
    editorial_mail = models.CharField(max_length = 75)
    ISBN = models.CharField(max_length=13, primary_key=True)
    price = models.FloatField()

