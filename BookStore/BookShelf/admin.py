from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
  list_display=('Title','Author','PublishingDate')
  list_filter=('Author', 'PublishingDate')
  search_fields=('Author', 'Title')
admin.site.register(Book, BookAdmin)

# Register your models here.
