from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import  date
from django.contrib.auth.models import User


# Create your models here.
class hmo_list(models.Model):
    name = models.CharField(max_length = 200)
    mobile = models.CharField(max_length = 100, null = True, blank = True)
    email = models.EmailField(help_text = "Please enter a valid email address!", blank=True, default="no-email@domain.com")
    address = models.TextField(default="NIL")
    hmo_status = models.BooleanField('Hmo Status', help_text = 'uncheck if HMO is not active', default = '0')
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, default = User.objects.get(username = "Admin").id)

    def __str__(self):
        return self.name

class state(models.Model):
    state_name = models.CharField("Name of State", max_length=15)

    def __str__(self):
        return ("%s" % self.state_name)


class patient(models.Model):
    surname = models.CharField(max_length = 20)
    firstname = models.CharField(max_length = 20)
    othername = models.CharField(max_length= 20, null=True, default="NIL")
    card_no = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 1, choices=(("M", "Male"), ("F", "Female")), default="M")
    phone_number = models.CharField(max_length = 15, default="NIL")
    address = models.CharField(max_length = 50, default="NIL")
    hmo_id = models.ForeignKey(hmo_list,verbose_name="hmo_id", default= 0)
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, User.objects.get(username = "Admin").id)
    origin = models.ForeignKey(state, default = state.objects.get(state_name = "OTHERS").id)


    def __str__(self):
        return ("%s %s" % (self.surname, self.firstname)).upper()

class drug(models.Model):
    drug_name = models.CharField(max_length=50)
    drug_code = models.CharField(max_length=15)
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, default = User.objects.get(username = "Admin").id)

    def __str__(self):
        return  ("%s" % self.drug_name).upper()


