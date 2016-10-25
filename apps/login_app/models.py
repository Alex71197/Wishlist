from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt
import datetime

# Create your models here.
class UserManager(models.Manager):
    def validate(self, data):
        errors = []
        if len(data['name']) < 3:
            errors.append('You must enter more than 3 characters')
        if len(data['username']) < 3:
            errors.append('You must enter more than 3 characters')
        if len(data['password']) == 0:
            errors.append('You must enter a password')
        if len(data['password']) < 8:
            errors.append('You must enter more than 8 characters')
        if not data['password'] == data['confirm_pass']:
            errors.append('password and Confirm password must match')
            print 'works'
        same = User.objects.filter(username = data['username'])
        if same:
            errors.append('This username is already in use')
        if len(errors) == 0:
            hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(name = data['name'], username = data['username'], password = hashed)
            return (True, user)
        else:
            return (False, errors)

    def login(self, data):
        try:
            user = User.objects.get(username = data['username'])
            print user
            pw_hash = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            print pw_hash
            if bcrypt.checkpw(data['password'].encode(), user.password.encode()):
                return (True, user)
        except ObjectDoesNotExist:
            pass

        return(False, 'Invalid Email or Password')

class User(models.Model):
    name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 30)
    date_hired = models.DateField(default = datetime.date.today)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
