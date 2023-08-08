from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class lead(models.Model):
    Website= models.TextField()
    Linkedin= models.TextField()
    Industry= models.CharField(max_length=266)
    Size= models.CharField(max_length=266)
    Location= models.CharField(max_length=266)
    Founded= models.CharField(max_length=266)
    Description= models.TextField()
    Company_Name= models.TextField()
    IP_adresse= models.TextField()
    IP_country= models.TextField()
    Email= models.TextField()
    Phones= models.TextField()
    Title= models.TextField()
    Description_W= models.TextField()
    Language= models.TextField()
    Verification_Date= models.TextField()
    Copyright_year= models.TextField()
    Copyright_owner= models.TextField()
    responsiveOrNot= models.TextField()
    Issuer= models.TextField()
    Cert_Country= models.TextField()
    Cert_state= models.TextField()
    Cert_Locality= models.TextField()
    Serial_number= models.TextField()
    Cert_start_date= models.TextField()
    Cert_expiry= models.TextField()
    SSL_TLS= models.TextField()
    Cert_Protocol= models.TextField()
    Cert_Organization= models.TextField()
    Schema_type= models.TextField()
    GoogleAnalytics_ID= models.TextField()
    AdSense_ID= models.TextField()
    Spf_record= models.TextField()
    Dmarc_record= models.TextField()
    Facebook= models.TextField()
    Twitter= models.TextField()
    Linkedin_W= models.TextField()
    Instagram= models.TextField()
    Youtube= models.TextField()
    Owler= models.TextField()
    Pintrest= models.TextField()
    Skype= models.TextField()
    WhatsApp= models.TextField()

    def __str__(self):
        return self.Industry

