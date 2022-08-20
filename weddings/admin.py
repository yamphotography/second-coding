from django.contrib import admin

# Register your models here.
from .models import Wedding, Tag, Review

admin.site.register(Wedding)
admin.site.register(Tag)
admin.site.register(Review)
