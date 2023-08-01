from django.db import models

# Create your models here.
class Showroom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    role = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    showroom = models.ForeignKey(Showroom,on_delete=models.CASCADE,related_name="team")

    def __str__(self):
        return self.name
    

class Brands(models.Model):
    class Meta:
        verbose_name_plural = "Brands"
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class Engine(models.Model):
    ENGINE_TYPES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        # Add more engine types as needed
    ]
    engine_type = models.CharField(choices=ENGINE_TYPES, max_length=20)
    displacement = models.CharField(max_length=20)
    power = models.CharField(max_length=50)
    engine_number = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.engine_type
    
class Features(models.Model):
    class Meta:
        verbose_name_plural = "Features"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    

class Models(models.Model):
    class Meta:
        verbose_name_plural = "Models"
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='models')
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    engine = models.ForeignKey(Engine,on_delete=models.SET_NULL, null=True, blank=True, related_name="models")
    features = models.ManyToManyField(Features,blank=True,related_name="models")

    def __str__(self):
        return self.name
    
