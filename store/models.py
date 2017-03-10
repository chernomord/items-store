from django.db import models


# TODO: create custom field for price, range 0-10000000
class StoreItem(models.Model):
    owner = models.ForeignKey('auth.User', related_name='storeitem', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField(default=0)
