from lib2to3.pgen2 import driver
from django.db import models
from invenotry.models import Container as inventorycontainer
from invenotry.models import Marka as inventorymarka



# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Driver name")
    phone_number = models.IntegerField( unique=True, verbose_name="Driver Phone Number")
    vehicle_number = models.CharField(max_length=20, unique=True, verbose_name="Vehicle Number")

    def __str__(self):
        return self.vehicle_number


class Sent(models.Model):
    marka_name = models.ManyToManyField(inventorymarka,max_length=10, verbose_name="Send Marka")
    driver=models.ForeignKey(Driver,on_delete=models.SET_NULL,null=True,verbose_name="Send Driver")
    lotissuedfrom=models.ManyToManyField(inventorymarka,verbose_name="Lot Send From",related_name="lotissuedfrom")
    totalcartoon=models.ManyToManyField(inventorymarka,verbose_name="Total Cartoon of the lot",related_name="totalcartoon")
    sentcartoon=models.ManyToManyField(inventorymarka,verbose_name="Sent Cartoon",related_name="sentcartoon")
    # sent_cartoons = models.

    def __self__(self):
        return self.lotissuedfrom.ContainerNumber
    