from django.db import models
import uuid
from users.models import Profile
# Create your models here.
class Detail(models.Model):
    owner = models.ForeignKey(Profile , null=True , blank=True , on_delete=models.SET_NULL)
    company  = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=500 , null=True , blank=True)
    image = models.ImageField(upload_to='images/', null=True , blank=True , default="default.png")
    variant = models.ManyToManyField('Variant' , blank=True)
    created = models.DateTimeField(auto_now_add=True)
    source_link = models.CharField(max_length=200 , null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return f"{self.company} - {self.model}"
    
    class Meta:
        ordering = ['-created']

class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'detail']]

    def __str__(self):
        return self.body[:15]
   
class Variant(models.Model):
    variants = (
        ('simple' , 'Simple Oriel'),
        ('oriel' , 'oriel prosmectic'),
        ('oriel ivtec' , 'Oriel ivTec'),
        ('UG iv' , 'UG Oriel ivTec'),
        ('UG p' , 'UG Oriel Pros'),
        ('xli' , 'XLI'),
        ('gli' , 'GLI'),
        ('grande' , 'Grande'),
        ('altis' , 'Altis'),
        ('l' , 'L'),
        ('s' , 'S'),
        ('g' , 'G'),
    )
    car_variant = models.CharField(max_length=20 , choices=variants)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.car_variant
    
