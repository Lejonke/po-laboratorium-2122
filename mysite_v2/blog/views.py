from django.shortcuts import render
from django.http import HttpResponse
import datetime

def books_list(request):
    now = datetime.datetime.now()
    html = """
        <html>
            <body>
           Jest %s.
            </body>
        </html>
        """ % now
  #  return (HttpResponse(html), render(request, 'blog/books_list.html', {}))

    return (render(request, 'blog/books_list.html', {}))
