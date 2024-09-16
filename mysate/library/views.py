from django.shortcuts import render
from .models import Book, Author


def get_book(req):
  book = Book.objects.get(id=1)
  return render(req, 'base.html', {'book': book})


def get_author(req):
  book_author = Book.objects.filter(author__name='Roman')
  return render(req, 'author.html', {'author':book_author})


def get_publisher(req):
  author_publisher = Author.objects.all()
  return render(req, 'publisher.html', {'publisher': author_publisher})