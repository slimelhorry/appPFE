from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd
#from django.contrib.auth.models import User

# Create your models here.

analitycs = (
    (0, 'No IDs'),
    (1, 'One ID'),
    (2, 'Tow IDs'),
    (3, 'more than 2'),
)
records = (
    (0, 'No records'),
    (1, 'SPF or Dmarc'),
    (2, 'SPF and Dmarc'),
    
)
enability = (
    ("Enabled", 'Enabled'),
    ("Not Enabled", 'Not Enabled'),
    ("N/A", 'N/A'),
)
status= (
    ("Expired", 'Expired'),
    ("Not Expired", 'Not Expired'),
    ('N/A', 'N/A'),
)

respons= (
    ("Yes", 'Yes'),
    ("No", 'No'),
    ('N/A', 'N/A'),
)

class Data(models.Model):
    Company = models.CharField(max_length=100,  null=True)
    industry = models.CharField(max_length=100,  null=True)
    location = models.CharField(max_length=100, null=True)
    size = models.PositiveIntegerField(null=True)
    founded = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(2023)], null=True)
    Count_Analytics = models.PositiveIntegerField(choices=analitycs, null=True)
    Count_records = models.PositiveIntegerField(choices=records, null=True)
    Count_contact = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(11)], null=True)   
    Expiry_status =  models.CharField(max_length=100,
                  choices=status, default="Don't know")
    ResponsiveOrNot = models.CharField(max_length=10,
                  choices=respons,  default="Don't know")
    SSL_TLS =models.CharField(max_length=100,
                  choices=enability,  default="NO")
    predictions = models.CharField(max_length=100, blank=True)
    #owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        with open('ml_model/clusters1.pkl', 'rb') as f:
            ml_model = pickle.load(f)

        data=[[self.industry, self.location, self.size, self.founded, self.ResponsiveOrNot, self.SSL_TLS, self.Expiry_status, self.Count_contact, self.Count_records, self.Count_Analytics]]
        columns = ['Industry','Location', 'Size','Founded', 'responsiveOrNot', 'SSL_TLS','Expiry_Status', 'Count_contact','Count_records',  'Count_analytics' ]
        df = pd.DataFrame(data=data, columns=columns)

        label_encoder = LabelEncoder()
        categorical_colms = [ 'Industry', 'Location', 'Size', 'Founded', 'responsiveOrNot', 'SSL_TLS','Expiry_Status' ]
        for col in categorical_colms:
            df[col] = label_encoder.fit_transform(df[col])
        #predictions= ml_model.predict(df)
        #self.predictions= predictions
        if (self.size< 5 and self.ResponsiveOrNot == 'N/A' and self.SSL_TLS== "N/A" and self.Count_contact ==0 and self.Count_records ==0 and self.Count_Analytics ==0 ):
            predictions = 'Low digital maturity'
        else:
            cluster= ml_model.predict(df)
            print(cluster)
            if cluster == 2:
                predictions = 'High digital maturity'
            elif cluster == 0:
                predictions = ' Medium digital maturity'
            else:
                predictions = 'Low digital maturity'


        self.predictions= predictions
        
        return super().save(*args, *kwargs)


    def __str__(self):
        return self.Company
