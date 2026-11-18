from django.db import models

class RegisterModel(models.Model):
    profile = models.ImageField(upload_to="profile_image/")
    full_name=models.CharField(max_length=30)
    username=models.CharField(max_length=50)
    number=models.IntegerField()
    choose=[
        ("Male","Male"),
        ("Female","Female")
    ]
    gender=models.CharField(max_length=50)
    dob=models.DateField()
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

class ProductAdding(models.Model):
    image = models.ImageField(upload_to="product_image/")
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(max_length=500)

class RegisterViewModel(models.Model):
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)