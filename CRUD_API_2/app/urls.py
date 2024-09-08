from django.urls import path

from app.views import CreateViewBook, UpdateDeleteBook

urlpatterns = [
    path('books', CreateViewBook.as_view()),
    path('books/<int:pk>', UpdateDeleteBook.as_view()),
]
