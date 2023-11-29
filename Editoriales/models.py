from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length = 100)
    pages = models.IntegerField()
    publication_year = models.CharField(max_length=30)
    description = models.CharField(max_length = 300)
    image_url = models.CharField(max_length =250)
    author_first_name = models.CharField(max_length = 40)
    author_last_name = models.CharField(max_length=40)
    editorial_mail = models.CharField(max_length = 75)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})