from django.db import models
from django.conf import settings
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class About(models.Model):
    about = models.CharField(max_length = 50)

    def __str__(self):
        return self.about


class File_format(models.Model):
    file_format = models.CharField(max_length = 5, choices=(('PH', ' Printed - Hard Cover - Druk/papier w twardej okładce '), ('PS', ' Printed - Soft Cover - Druk/papier w miękkiej okładce') ,('epub', 'e-publikacja'),('pdf', 'pdf jaki jest każdy widzi')))
    condition = models.TextField(max_length = 100)

    def __str__(self):
        return self.file_format



class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    about = models.ForeignKey(About, on_delete = models.CASCADE)
    published_date = models.DateTimeField(
        blank = True, null = True)
    file_format= models.ForeignKey(File_format, on_delete = models.CASCADE)

    def info(self):
        self.published_date = timezone()
        #self.save()

    def __str__(self):
        return self.title












    
