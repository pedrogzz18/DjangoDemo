from django.db import models
from ourbooks.models import Reader, Editorial
from Editoriales.models import Books

class Ownership(models.Model):
    book_id = models.ForeignKey(to=Books, on_delete=models.CASCADE)
    reader_id = models.ForeignKey(to=Reader, on_delete=models.CASCADE)
    is_purchase = models.BooleanField(default=True)
    is_borrowed = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('book_id', 'reader_id', 'is_purchase')


