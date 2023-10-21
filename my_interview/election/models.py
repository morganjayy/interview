from django.db import models

class PollingUnit(models.Model):
    polling_unit_id = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, null=False)

class LocalGovtResult(models.Model):
    lga_name = models.CharField(max_length=50, null=False)
    PDP = models.IntegerField(null=False, default=0)
    DPP = models.IntegerField(null=False, default=0)
    ACN = models.IntegerField(null=False, default=0)
    PPA = models.IntegerField(null=False, default=0)
    CDC = models.IntegerField(null=False, default=0)
    JP = models.IntegerField(null=False, default=0)
    ANPP = models.IntegerField(null=False, default=0)
    LAB = models.IntegerField(null=False, default=0)
    CPP = models.IntegerField(null=False, default=0)



# Create your models here.
