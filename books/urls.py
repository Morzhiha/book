from django.urls import path

from . import views


urlpatterns = [
    path("", views.BooksView.as_view()),
    path("filter/", views.FilterBookView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"),
    path("author/<str:slug>/", views.AuthorDetailView.as_view(), name="author_detail"),
]
