from django.db import models
from picklefield.fields import PickledObjectField
from django.contrib.auth.models import User

class GeographicLP(models.Model) :
    """
    This model model contains the normalised load profiles
    of each region covered by the application.
    """
    region = models.CharField(max_length=100)
    data = PickledObjectField()

    def __str__(self) :
        return self.region


class ElectricityPrice(models.Model) :
    """
    This model contains the different costs that comprise an
    electricity bill, depending on the power of the electric meter.
    """
    em_power = models.FloatField()
    sub_price = models.FloatField()
    kWh_price = models.FloatField()

    def __str__(self) :
        return 'Puissance : {0} kVA'.format(em_power)

class UsersLP(models.Model) :
    """
    This model contains the responses of the users to the form
    and their load profile resulting from the simulation.
    """
    loc_choices = []
    for obj in GeographicLP.objects.all() :
        loc_choices.append((obj.region, obj.region))
    
    power_choices = []
    for obj in ElectricityPrice.objects.all() :
        power_choices.append((obj.em_power, obj.em_power))
    
    user = models.CharField(max_length=50, default='blabla')
    location = models.CharField(max_length=50, choices=loc_choices, default='Ile-de-France')
    power = models.FloatField(choices=power_choices, default=3)
    bill = models.FloatField()
    consumption = models.FloatField(default=0)
    load_profile = PickledObjectField()

    def __str__(self) :
        return self.user
