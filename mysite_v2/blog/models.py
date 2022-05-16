from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    """ Klasa Autora, zawiera imię i nazwisko autora """
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class About(models.Model):
    """ Klasa Tematyki, zawiera pole tekstowe do 50 znaków, można w przyszłości rozbudować o dodatkowe informacje
        (np. 3 ramki choices zawierające szczegółowe działy IT, streszczenia texfield,
        spis treści)"""
    
    about = models.CharField(max_length = 50)

    def __str__(self):
        return self.about


class FileFormat(models.Model):
     """ Klasa Formatu Pliku - Ksiązki..."""
     
#       condition = models.TextField('''max_length = 50''')
     
    class BookFormat(models.TextChoices):
        """ Klasa Formatu Ksiązki, wewnętrzna w FileFormat czy fizyczna (okładka twarda/miękka) czy plik, oraz stan ksiązki ("nówka",
             "używana" w przypadku fizycznych, czy np. skan w przypadku starych niedostepnych już
              książek dostępnych w formie wirtualnej """
        
        hard_cover_printed = 'HCP', _(' Druk/papier w twardej okładce ')
        soft_cover_printed = 'PS', _(' Druk/papier w miękkiej okładce') 
        epub = 'epub' , _('e-publikacja')
        pdf = 'pdf', _('pdf jaki jest każdy widzi')
        
    book_format = models.CharField(
        max_length = 20,
        choices = BookFormat.choices,
        default = BookFormat.epub)
        
    def __str__(self):
        return self.file_format
    
#class Student(models.Model):
#
#    class YearInSchool(models.TextChoices):
#        FRESHMAN = 'FR', _('Freshman')
#        SOPHOMORE = 'SO', _('Sophomore')
#        JUNIOR = 'JR', _('Junior')
#        SENIOR = 'SR', _('Senior')
#        GRADUATE = 'GR', _('Graduate')
#
#    year_in_school = models.CharField(
#        max_length=2,
#        choices=YearInSchool.choices,
#        default=YearInSchool.FRESHMAN,
#    )
        
#    def is_upperclass(self):
  #          return self.year_in_school in {             #tutorial z docs.djangoproject.com
    #            self.YearInSchool.JUNIOR,
      #          self.YearInSchool.SENIOR,
        #    }

class Book(models.Model):
    """ Klasa Ksiązki,
        klucz obcy do klas zdefiniowanych powyżej """

    hard_cover_printed = 'HCP'
    soft_cover_printed = 'PS'
    epub = 'epub' 
    pdf = 'pdf'

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    
    title = models.CharField(max_length = 50)
    
    about = models.ForeignKey(About, on_delete = models.CASCADE)
    
    published_date = models.DateTimeField(
        blank = True, null = True)

    book_format= models.ForeignKey(FileFormat, on_delete = models.CASCADE)

    def info(self):
        self.published_date = timezone()
        #self.save()

    def __str__(self):
        return self.title












    
