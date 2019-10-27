from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    pass


class Department(models.Model):
    name = models.CharField('Department', max_length=20)
    created_at = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField('Club', max_length=20)
    created_at = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return self.name


class Member(models.Model):
    first_name = models.CharField('First name', max_length=20)
    last_name = models.CharField('Last name', max_length=20)
    email = models.EmailField('Email', blank=True)
    department = models.ForeignKey(Department, verbose_name='Department', on_delete=models.PROTECT)
    club = models.ManyToManyField(Club, verbose_name='Club')
    created_at = models.DateTimeField('Date', default=timezone.now)

    '''
    verbose_name -> When models.ForeignKey and you want to describe it
    on_delete -> When ManyToManyField, on_delete is not need
    '''

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


