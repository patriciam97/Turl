from django.db import models
import random
# Create your models here.


def random_path():
    return str(random.randint(100, 500))


class Entry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    link = models.TextField(max_length=1000)
    path = models.CharField(default=random_path, max_length=1000)
