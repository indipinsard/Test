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
    loc_choices = [('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'),
       ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand-Est', 'Grand-Est'), ('Hauts-de-France', 'Hauts-de-France'),
       ('Ile-de-France', 'Ile-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'),
       ('Pays de la Loire', 'Pays de la Loire'), ('Provence-Alpes-Côte d\'Azur', 'Provence-Alpes-Côte d\'Azur')]
    
    power_choices = [(3, 3), (6, 6), (9, 9), (12, 12), (15, 15)]
    
    user = models.CharField(max_length=50, default='blabla')
    location = models.CharField(max_length=50, choices=loc_choices, default='Ile-de-France')
    power = models.FloatField(choices=power_choices, default=3)
    bill = models.FloatField()
    consumption = models.FloatField(default=0)
    load_profile = PickledObjectField()

    def __str__(self) :
        return self.user
