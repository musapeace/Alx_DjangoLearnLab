from bookshelf.models import Book
book.delete()

print(Book.objects.all())  # Should return an empty list