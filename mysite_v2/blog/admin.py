from .models import Book,  About, Author, FileFormat, Rate
# from .models import BookFormat as Formats 

from django.contrib import admin
#from .models import Author, Editor, Reader
#from mysite_v2.admin_site import custom_admin_site

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'about', 'published_date', 'file_format')

class ChoiceInline(admin.TabularInline):
    model = Book #FileFormat.BookFormat
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('author', 'published_date','file_format','about')

admin.site.register(Book)
admin.site.register(FileFormat)
#admin.site.register(Author)  
admin.site.register(Rate)

#def add(Book):
  #  return 0


