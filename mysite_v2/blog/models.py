from django.db import models
from django.conf import settings
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class About(models.Model):
    about = models.CharField(max_length = 50)

    def __str__(self):
        return self.about


class File_format(models.Model):
    
    class book_format(models.TextChoices):
        #FRESHMAN = 'FR', _('Freshman')
        Hard_Cover_Printed = 'HCP', (' Druk/papier w twardej okładce ')
        Soft_Cover_Printed = 'PS', (' Druk/papier w miękkiej okładce') 
        EPUB = 'epub' ,('e-publikacja')
        PDF = 'pdf', ('pdf jaki jest każdy widzi')
        
    condition = models.TextField(max_length = 100)

    def __str__(self):
        return self.file_format



class Book(models.Model):

    Hard_Cover_Printed = 'HCP'
    Soft_Cover_Printed = 'PS'
    EPUB = 'epub' 
    PDF = 'pdf'

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    
    title = models.CharField(max_length = 50)
    
    about = models.ForeignKey(About, on_delete = models.CASCADE)
    
    published_date = models.DateTimeField(
        blank = True, null = True)

    
    book_format= models.ForeignKey(File_format, on_delete = models.CASCADE)

    def info(self):
        self.published_date = timezone()
        #self.save()

    def __str__(self):
        return self.title












    
