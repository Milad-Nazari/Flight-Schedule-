from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import BooleanField
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.forms import widgets

class Flight(models.Model):
    iranair = 'IR'
    mahan = 'W5'
    airtour = 'B9'
    aseman = 'EP'
    zagros = 'ZV'
    kish = 'Y9'
    qeshm = 'QB'
    ata = 'I3'
    meraj = 'JI'
    taban = 'HH'
    caspian='Rv'
    karoon = 'Nv'
    sepehran_ = "ISS"
    varesh='VR'
    flypersia = 'PR'
    
    tehran='تهران'
    abadan='ABD'
    isfahan='IFN'
    ahvaz='AWZ'
    tabriz= 'TBZ'
    kish='KIH'
    chabahar='ZBR'
    khoramabad='KHD'
    shiraz='SYZ'
    kermanshah='KSH'
    mashhad='MHD'

    is_valid='باطل'
    City=[
        (tehran,'tehran'),
        (abadan,'abadan'),
        (mashhad,"mash'had"),
        (shiraz,'shiraz'),
        (isfahan,'isfahan'),
        (chabahar,'chabahar'),
    ]
    
    Airline =[
        (iranair,'iranair'),(mahan,'mahan'),(airtour,'airtour'),(aseman,'aseman'),(zagros,'zagros'),(kish,'kish'),
        (qeshm,'qeshm'),(ata,'ata'),(meraj,'meraj'),(taban,'taban'),(caspian,'caspian'),(karoon,'karon'),(sepehran_,'sepehran'),
        (varesh,'varesh'),(flypersia,'flypersia'),

    ]
    Flight_Origin = models.CharField(max_length=30,choices=City,)
    Flight_Distination = models.CharField(max_length=30,choices=City)
    Flight_Airline = models.CharField(max_length=10,choices=Airline)
    Flight_Nomber = models.CharField(max_length=10)
    Flight_Date = models.DateField()
    Flight_Time = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)
    is_valid = BooleanField(default=False)
    schadule_Date = models.DateField()
    schadule_Time = models.TimeField()


    def __str__(self):
        return f'{self.Flight_Nomber} {self.Flight_Origin} to {self.Flight_Distination} in {self.Flight_Date} at {self.Flight_Time} '

# class schadule(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     FlightNo = models.CharField(max_length=10,)
