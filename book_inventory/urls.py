from django.urls import path
from .views import BookInventoryListCreate, BookInventoryUpdate, GoogleBooks, GoogleBooksDetails
urlpatterns = [
    path('book/', BookInventoryListCreate.as_view()), # Get list of books with pagination and allow filter 
    path('book/<book_id>/', BookInventoryUpdate.as_view()), # Get list of books with pagination and allow filter 
    path('volumes/', GoogleBooks.as_view()), # Get list of books with pagination and allow filter 
    path('volumes/<volume_id>', GoogleBooksDetails.as_view()), # Get list of books with pagination and allow filter 

]
