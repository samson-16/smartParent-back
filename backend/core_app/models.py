from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    fisrt_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    roll_number = models.PositiveIntegerField()
    grade = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ]
    )
    section = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[('teacher', 'Teacher'), ('parent', 'Parent'), ('admin', 'Admin')])
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  
        help_text='Specific permissions for this user.',
    )


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    children = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    class Meta:
        ordering = ['user__first_name', 'user__last_name']

