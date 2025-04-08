from django.db import models

class user(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    city=models.CharField(max_length=50)

    def _str_(self):
        return self.name
