from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Author(models.Model):
    name = models.CharField("Автор", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    image = models.ImageField("Фотография", upload_to="authors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    year = models.PositiveSmallIntegerField("Дата написания", null=True)
    url = models.SlugField(max_length=160, unique=True)
    cover = models.ImageField("Обложка", upload_to="books/")
    genres = models.ManyToManyField(Genre, verbose_name="жанры", related_name="book_genre")
    authors = models.ManyToManyField(Author, verbose_name="авторы", related_name="book_author")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


