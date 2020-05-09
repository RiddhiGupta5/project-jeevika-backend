import hashlib
from django.db import models


class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.email + '|' + str(id)

    def save(self, *args, **kwargs):
        m = hashlib.md5()     
        m.update(self.password.encode("utf-8")) 
        self.password = str(m.digest())
        super().save(*args, **kwargs)


class CustomToken(models.Model):
    token = models.CharField(max_length=500)
    object_id = models.IntegerField()
    user_type = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
