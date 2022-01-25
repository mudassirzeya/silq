from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    super_user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        default="profile1.jpg", null=True, blank=True)

    def __str__(self):
        return self.company_name


class UserProfile(models.Model):
    USERTYPE = (
        ('customer', 'customer'),
        ('staff', 'staff'),
        ('admin', 'admin'),
    )
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default="profile1.jpg", null=True, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=100, blank=True, choices=USERTYPE)

    def __str__(self):
        return str(self.user)
