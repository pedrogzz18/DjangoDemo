from django.contrib import admin
from .models import Editorial, Reader, CustomUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Editorial)
admin.site.register(Reader)