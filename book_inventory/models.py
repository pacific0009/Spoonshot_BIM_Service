from django.db import models

class BookInventory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=False)
    active = models.BooleanField(default=True)
    google_id = models.CharField(max_length=30, unique=True, null=False)
    stock_count = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "active": self.active,
            "google_id": self.google_id,
            "stock_count": self.stock_count
        }

    ## indexes Unique google_id 

