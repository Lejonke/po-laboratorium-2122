from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib.auth import get_user_model

##def index(request):
##    html = """
##
##<a href="{% url 'index' %}">Home</a>.
##
##"""
##    return (render(request,)

def books_list(request):
    now = datetime.datetime.now()
    content = 'że lista tabelka coś takiego'
    render_to_response("template.html", {"content":content})
    html = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>


</body>
</html> """
##<h1>Półka z książkami</h1>
##<table>
##  <tr>
##    <th>Tytuł</th>
##    <th>Autor</th>
##    <th>Tematyka</th>
##  </tr>
##  <tr>
##    <td> yyy </td>
##   
##  </tr>
##  <tr>
##    <td> abc </td>
##    <
##  </tr>
##</table> 
##
##</body>
##</html>
    
    #return (render(HttpResponse(html), render(request, 'blog/books_list.html', {})))
    return (render(request, 'blog/books_list.html', {}))

