# from operator import truediv
# from typing_extensions import Required
# from unicodedata import name
from django.db import models


# comapny model
class Firm(models.Model):
    name = models.CharField(max_length=50, verbose_name="Firm Name")
    address = models.CharField(max_length=100, verbose_name="Company Address")

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(Firm, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


# containermodel

class Container(models.Model):
    ContainerNumber = models.CharField(max_length=5,unique=True,verbose_name="Container Number")
    firm_name = models.ForeignKey(Firm, max_length=50, on_delete=models.CASCADE, verbose_name="Firm Name")

    def save(self, *args, **kwargs):
        self.ContainerNumber = self.ContainerNumber.upper()
        super(Container, self).save(*args, **kwargs)

    class Meta:
        ordering = ["ContainerNumber"]

    def __str__(self):
        return str(self.ContainerNumber) + " " + str(self.firm_name)


# marka model
class Marka(models.Model):
    markname = models.CharField(max_length=10, verbose_name="Marka Name")
    cartoon = models.IntegerField(verbose_name="Cartoon")
    cbm = models.FloatField(verbose_name="CBM", null=True, blank=True)
    containernumber = models.ForeignKey("Container", related_name="marka_containernumber",
                                        verbose_name="Container Number", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.markname) + " " + str(self.cartoon)

    class Meta:
        unique_together = ("markname", 'cbm', 'cartoon',)
