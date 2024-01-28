from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Marka(models.Model):
    title = models.CharField(max_length=16, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Car(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField()
    sold = models.BooleanField("Черновик", default=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    marka = models.ForeignKey(to=Marka, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.CharField(max_length=16)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.car}'




#
# CRUD, search, folter (marka, model, category, year)
# CBV