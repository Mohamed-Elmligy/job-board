from django.contrib import admin

# Register your models here.

from .models import job, Categoty

admin.site.register(job)
admin.site.register(Categoty)