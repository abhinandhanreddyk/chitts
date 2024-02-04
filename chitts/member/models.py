# models.py
from django.db import models
from decimal import Decimal


class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    parentname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class InterestInput(models.Model):
    principal_amount = models.DecimalField(max_digits=10, decimal_places=0)
    # principal_amount= int(principal_amount)
    interest_rate = 24

    def calculate_interest(self):
        print(self.interest_rate, self.principal_amount)
        return self.principal_amount * (Decimal(str(self.interest_rate)) / 100)

    def calculate_total_amount(self):
        return self.principal_amount + self.calculate_interest()

    def __str__(self):
        return f"Principal: {self.principal_amount}, Rate: {self.interest_rate}"