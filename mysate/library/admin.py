from django.contrib import admin

from library.models import Author, Publisher, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
  pass