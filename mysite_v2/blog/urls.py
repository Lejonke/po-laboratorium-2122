
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
        #Home page
    path('', views.books_list, name='index'),      #lista książek tożsama z main site
    
       #Page that shows all books
    path('books/', views.books_list, name='books'),


    # argumenty domyślne 
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    
]
