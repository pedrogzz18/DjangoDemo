from django.db import models
from ourbooks.models import Reader, Editorial
from Editoriales.models import Books

class Purchase(models.Model):
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)
    reader = models.ForeignKey(to=Reader, on_delete=models.CASCADE)
    date = models.DateField()
    
    class Meta:
        unique_together = ('reader', 'book',)

class Share(models.Model):
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)
    reader = models.ForeignKey(to=Reader, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('reader', 'book',)

class OwnerShare(models.Model):
    share = models.OneToOneField(to=Share, on_delete=models.CASCADE)
    book_owner = models.ForeignKey(to=Reader, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('share', 'book_owner',)

class Review(models.Model):
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)
    reader = models.ForeignKey(to=Reader, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField()
    class Meta:
        unique_together = ('book', 'reader')


