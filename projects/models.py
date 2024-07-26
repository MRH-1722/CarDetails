from django.db import models
import uuid
# Create your models here.
class Detail(models.Model):
    company  = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=500 , null=True , blank=True)
    image = models.ImageField(upload_to="photos" , null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return f"{self.company} - {self.model}"