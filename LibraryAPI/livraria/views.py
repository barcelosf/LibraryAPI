from django.shortcuts import render, redirect
from .models import Book
from .serializers import BookSerializer

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def list_create_books(request):
    if request.method =='GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    else:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def list_update_delete_book(request, id_book):
    try:
        book = Book.objects.get(pk=id_book)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        book.delete()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)