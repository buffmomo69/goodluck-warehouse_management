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
    containernumber = models.ForeignKey("Container", related_name="marka_containernumber", verbose_name="Container Number", on_delete=models.CASCADE)
    receiveddate=models.DateField( auto_now_add=True,null=True,verbose_name="Stock Received Date")
    
    def __str__(self):
        return str(self.markname) + " " + str(self.cartoon)

    class Meta:
        unique_together = ("markname", 'cbm', 'cartoon',)


class Vehicle(models.Model):
    driver_name=models.CharField(verbose_name="Driver Name", max_length=50)
    driver_number=models.IntegerField(verbose_name="Driver Phone Number")
    driver_vehicle=models.CharField(verbose_name=("Driver vehicle number"), max_length=50)
    
class StockSentDetail(models.Model):
    
    sent=models.IntegerField(verbose_name=("Sent Stocks in Godown"))
    remaining=models.IntegerField(verbose_name=("Remaining Stocks in Godown"))
    sentdate=models.DateTimeField(verbose_name=("Stock Sent Date"), auto_now=False, auto_now_add=False)
    vehicle=models.ForeignKey("Vehicle", verbose_name=("Vehicle Sent From"), on_delete=models.CASCADE)
    markname=models.ManyToManyField("Marka", verbose_name=("Marka"),related_name="stocksentdetail_markname")
    total=models.ManyToManyField("Marka", verbose_name=("Total Cartoon"),related_name="stocksentdetail_total")