from django.contrib import admin

from .models import Book, File_format, About, Author

admin.site.register(Book)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'about', 'published_date', 'file_format')
