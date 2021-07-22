from django.contrib import admin
from .models import BookInventory
# Register your models here.
@admin.register(BookInventory)
class BookInventoryAdmin(admin.ModelAdmin):
    pass