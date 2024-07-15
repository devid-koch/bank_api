from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11)
    address = models.TextField()

    def __str__(self):
        return self.name
