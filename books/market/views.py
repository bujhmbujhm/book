from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from market.models import Book

from market.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
