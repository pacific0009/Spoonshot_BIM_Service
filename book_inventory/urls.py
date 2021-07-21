from django.urls import path
from .views import BookInventoryListCreate, BookInventoryUpdate, BookInventoryGoogle, GoogleBooks, GoogleBooksDetails
urlpatterns = [
    path('book/', BookInventoryListCreate.as_view()), 
    path('book/<book_id>/', BookInventoryUpdate.as_view()), 
    path('book/<book_id>/', BookInventoryUpdate.as_view()),  
    path('book_google/<google_id>/', BookInventoryGoogle.as_view()),  
    path('volumes/', GoogleBooks.as_view()), 
    path('volumes/<volume_id>/', GoogleBooksDetails.as_view()),

]
