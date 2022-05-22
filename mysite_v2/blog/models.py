from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~AUTOR~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Author(models.Model):
    """ Klasa Autora, zawiera imię i nazwisko autora """
    
#    def __init__(self):
  #      return None
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TEMATYKA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class About(models.Model):
    """ Klasa Tematyki, zawiera pole tekstowe do 50 znaków, można w przyszłości rozbudować o dodatkowe informacje
        (np. 3 ramki choices zawierające szczegółowe działy IT, streszczenia texfield,
        spis treści)"""
    
#    def __init__(self):
  #      return None
    
    about = models.CharField(max_length = 300)

    def __str__(self):
        return "%s" % (self.about)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FORMAT PLIKU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class FileFormat(models.Model):
    """ Klasa Formatu Pliku - Ksiązki..."""

    def __init__(self):            # $%$!!!!!@@@@ (czyt. pkt 7.)
        return None
 
    condition = models.TextField('''max_length = 50''')

    class BookFormat(models.TextChoices):
            #   UNINDENT DOES NOT MATCH ANY OUTER INDENTATION LEVEL - złe odstępy/tab'y ?!
            # klasa tworzona na podstawie tutorialu ze strony djangoproject ....przykład na dole jako class Student(models.Model):

            #dziennik dziłań:
            # 1. usunięcie komentarzy i 'dokumentacji' nie usuwa problemu
            # 2. przesunięcie zmiennych (hard_cover...ect.) o +-1 tab nie usuwa błędu
            # 3. przesunięcie zmiennej book_format o +-1 tab nie usuwa błędu
            # 4. przesunięcie funkcji __str__ o +-1 tab nie usuwa błędu
            # 5. zrównanie wszystkeigo do lewej krawędzi i 'przetabowanie' (tylko tab) wszystkeigo
            # do odpowiednich poziomów nie usuwa błędu
            # 6. usuniecie ewentualnych spacji w pustych wersach kodu nie usuwa problemu
            # 7. doadanie ' def __init__(self):' przy $%$!!!!!@@@@ pozwala na uruchomienie serwera !!!!!

        """ Klasa Formatu Ksiązki, wewnętrzna w FileFormat czy fizyczna (okładka twarda/miękka) czy plik, oraz stan ksiązki ("nówka",
             "używana" w przypadku fizycznych, czy np. skan w przypadku starych niedostepnych już
             książek dostępnych w formie wirtualnej """
        
##        choices = (
##        (hard_cover_printed = 'HCP', _(' Druk/papier w twardej okładce ')),
##        (soft_cover_printed = 'SCP', _(' Druk/papier w miękkiej okładce')),
##        (epub = 'epub' , _('e-publikacja')),
##        (pdf = 'pdf', _('pdf jaki jest każdy widzi')),
##        )

##        choices = (
##            (hard_cover_printed),
##            (soft_cover_printed ),
##            (epub),
##            (pdf),
##        )


        hard_cover_printed = 'HCP', _(' Druk/papier w twardej okładce ')
        soft_cover_printed = 'SCP', _(' Druk/papier w miękkiej okładce')
        epub = 'epub' , _('e-publikacja')
        pdf = 'pdf', _('pdf jaki jest każdy widzi')
        
    #book_format = models.TextChoices(choices = BookFormat.choices, default = BookFormat.pdf)
    book_format = models.CharField(max_length = 4, choices = BookFormat.choices, default = BookFormat.pdf)


#    def __unicode__(self):
  #      return self.name
    
    def __str__(self):
        return "%s" % (self.book_format)
    
#    def __str__(self):
  #      return (self.file_format)         #zmienić żeby nie wpisywać w pdf 'pdf'
    

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
#
#    def is_upperclass(self):
  #          return self.year_in_school in {             #tutorial z docs.djangoproject.com
    #            self.YearInSchool.JUNIOR,
      #          self.YearInSchool.SENIOR,
        #    }


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~OCENA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Rate(models.Model):               
    """klasa oceny"""
    def __init__(self):
        return None

    class Scale(models.TextChoices):
        """klasa skali ocen"""
        wsp = '5.0', _(' Wspaniała')
        dbr = '4.0', _(' Dobra') 
        ptn = '3.0' , _('Przeciętna')
        sba = '2.0', _('Słaba')
        zla = '1.0',_('Zła')
        
    rate = models.CharField(max_length = 10, choices = Scale.choices, default = Scale.zla)

    
    def __str__(self):
        return "%s" % (self.rate)

#dobra = Rate.Scale.create(rate = "4.0")    # 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~KSIĄŻKA (KLASA GŁ.)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Book(models.Model):
    """ Klasa Ksiązki,
        klucz obcy do klas zdefiniowanych powyżej """

    def __init__(self):
        pass

##    BookFormat.hard_cover_printed = 'HCP'        #przerzucone na dół
##    BookFormat.soft_cover_printed = 'SCP'
##    BookFormat.epub = 'epub' 
##    BookFormat.pdf = 'pdf'

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    
    title = models.CharField(max_length = 100)
    
    about = models.ForeignKey(About, on_delete = models.CASCADE)

    rate = models.ForeignKey(Rate, on_delete = models.CASCADE)
    
 #   published_date = models.DateTimeField(
     #   blank = True, null = True)

    BookFormat = models.ForeignKey(FileFormat, on_delete = models.CASCADE)

    BookFormat.hard_cover_printed = 'HCP'
    BookFormat.soft_cover_printed = 'SCP'
    BookFormat.epub = 'epub' 
    BookFormat.pdf = 'pdf'


    def info(self):
        self.published_date = timezone()
        self.save()

#    def add_book():        #czy to jest potzebne? class Author działa bez problemów 
  #      return 0
    
    def __str__(self):
        return self.title



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DRUKARKA - TEST DO MIGRACJI~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #                                             NIE SPRAWDZAĆ !!!!
    
class Drukarka(models.Model):               #sprawdzam nowe migracje
    def __init__(self):
        return None
    abc = 1








    
