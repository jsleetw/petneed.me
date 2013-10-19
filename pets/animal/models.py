from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Animal(models.Model):
    accept_num = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    build = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)
    accept_num = models.CharField(max_length=200)
    chip_num = models.CharField(max_length=200)
    is_sterilization = models.CharField(max_length=200)
    hair_type = models.CharField(max_length=200)
    note = models.TextField()
    resettlement = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    childre_anlong = models.CharField(max_length=200)
    animal_anlong = models.CharField(max_length=200)
    bodyweight = models.CharField(max_length=200)
    image_name = models.URLField(max_length=200)
    image_file = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count_clicks = models.CharField(max_length=200, default=0)
    count_eyeons = models.CharField(max_length=200, default=0)

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
            verbose_name='email address',
            max_length=255,
            unique=True,
            db_index=True,
            )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_fb = models.BooleanField(default=False)
    fb_access_token = models.CharField(max_length=200)
    fb_user_id = models.IntegerField(default=False)
    last_login_date = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
