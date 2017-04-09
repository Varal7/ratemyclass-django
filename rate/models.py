from django.db import models

# Create your models here.


class Department(models.Model):
    trigram = models.CharField(max_length=254)
    name = models.CharField(max_length=254)


class Year(models.Model):
    name = models.CharField(max_length=254)


class Period(models.Model):
    name = models.CharField(max_length=254)


class Type(models.Model):
    name = models.CharField(max_length=254)


class Class(models.Model):
    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    professor = models.CharField(max_length=254)
    description = models.TextField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    year = models.ForeignKey('year', on_delete=models.CASCADE)
    period = models.ForeignKey('period', on_delete=models.CASCADE)
    type = models.ForeignKey('type', on_delete=models.CASCADE)
    has_pale = models.NullBooleanField()
    has_project = models.NullBooleanField()
    has_presentation = models.NullBooleanField()
    has_oral = models.NullBooleanField()


