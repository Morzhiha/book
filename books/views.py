from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Book, Author, Genre


class GenreYear:

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Book.objects.filter().values("year")


class BooksView(GenreYear, ListView):

    model = Book
    queryset = Book.objects.all()
    paginate_by = 3


class BookDetailView(GenreYear, DetailView):

    model = Book
    slug_field = "url"


class AuthorDetailView(GenreYear, DetailView):

     model = Author
     template_name = 'books/author.html'
     slug_field = "name"


class FilterBookView(GenreYear, ListView):

    paginate_by = 3
    def get_queryset(self):
        queryset = Book.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context


class Search(ListView):

    paginate_by = 3
    def get_queryset(self):
        return Book.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context