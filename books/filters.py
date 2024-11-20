import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'author': ['exact'],
            'genre': ['exact'],
            'publication_year': ['exact'],
            'title': ['contains']
        }
