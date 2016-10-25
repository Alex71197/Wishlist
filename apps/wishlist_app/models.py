from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.
class ItemManager(models.Manager):
    def validate(self, data):
        errors = []
        if len(data['title']) < 3:
            errors.append('You must enter more than 2 characters')
        if len(data['title']) == 0:
            errors.append('You must NOT leave this field blank')
        return errors
    def create_product(self, data, user_id):
        print data['title']
        Item.objects.create(title = data['title'], user = User.objects.get(id = user_id))
    def join_product(self, item_id, user_id):
        self.get(id = item_id).join.add(user_id)
    def remove_product(self, item_id, user_id):
        self.get(id = item_id).join.remove(user_id)

class Item(models.Model):
    title = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    user = models.ForeignKey(User)
    join = models.ManyToManyField(User, related_name = 'User_in_Item')
    objects = ItemManager()
