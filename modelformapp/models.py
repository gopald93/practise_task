from django.db import models

# Create your models here.
class Collection(models.Model):
    subject = models.CharField(max_length=300, blank=True)
    owner = models.CharField(max_length=300, blank=True)
    note = models.TextField(blank=True)
    def __str__(self):
        return str(self.subject)


class CollectionTitle(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Title")
    language = models.CharField(max_length=100) 

    def __str__(self):
        return str(self.name)       