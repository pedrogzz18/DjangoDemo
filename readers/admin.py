from django.contrib import admin
from .models import Purchase, Share, OwnerShare
# Register your models here.
admin.site.register(Purchase)
admin.site.register(Share)
admin.site.register(OwnerShare)