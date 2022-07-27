from django.urls import path
from . import views

# all URL patterns in this file start with catalog/

# this is a URLConf module. It must be imported into the locallibrary urls.py
urlpatterns = [
    path('', views.index, name='index'),
]

# display a list of books that are stored in the database
urlpatterns += [
    path('books/', views.BookListView.as_view(), name='books')
]

# 'pk' is the primary key for each book.
# display a page for each book in the database
urlpatterns += [
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail')
]

#whenever we go to /catalog/about/ load the about page
urlpatterns += [
  path('about/', views.about, name="about")
]
