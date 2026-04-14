from django.db import models
from django.contrib.auth.models import User


class Artworks(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="artworks/")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to="art_gallery/")


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artworks, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=20, default="Pending")
    Purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artwork.name
