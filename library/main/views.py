from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.
class GetAllCreateBooks(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # поиск по названию книги api/books/?title=название
    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset
    

class GetDeleteUpdateBookById(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class GetAllCreateAuthors(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    

class GetDeleteUpdateAuthorById(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'


        