from django.db import models
import datetime
from featuretickets.models import FeatureTicket

"""member's personal details"""
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField(null=True, default=datetime.date.today)
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

"""specific info on the featureticket item being purchased"""
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    feature = models.ForeignKey(FeatureTicket, on_delete=models.CASCADE, null=False, related_name="features_vote")
    quantity = models.IntegerField(blank=False, default=0)
    
    def __str__(self):
        return "Item {0} x {1}".format(self.id, self.quantity)
        