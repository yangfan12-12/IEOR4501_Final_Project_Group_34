from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Sighting(models.Model):
    Longitude  = models.FloatField(
            help_text = _('Longitude of the squirrel'),)
    
    Latitude = models.FloatField(
            help_text = _('Latitude of the squirrel'),)
    
    Unique_Squirrel_Id = models.CharField(
            help_text = _('The unique ID of the squirrel'),
            max_length = 25,
            )
    
    AM = 'AM'
    PM = 'PM'
    TIME_CHOICES=[
            (AM,'AM'),
            (PM,'PM'),
            ]
    Shift = models.CharField(
            help_text = _('Whether the squirrel appears in the morning or afternoon?'),
            max_length=16,
            choices=TIME_CHOICES,
            blank=True,)
    
    Date = models.DateField(
            help_text = _('Date of appearance'),
            null = True,
            blank=True,)
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown='?'
    AGE_CHOICES=[
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            (None, ''),
            (Unknown,'?')
            ]
    Age = models.CharField(
            help_text = _('Age of the squirrel'),
            max_length=16,
            choices = AGE_CHOICES,
            blank = True,
            )
    
    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    COLOR_CHOICES=[
            (Black, 'Black'),
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            (None, ''),
            ]
    Primary_Fur_Color = models.CharField(
            help_text = _('Fur color of the squirrel'),
            max_length=16,
            choices = COLOR_CHOICES,
            blank = True,
            )
    
    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    LOCATION_CHOICES=[
            (Ground_Plane, 'Ground Plane'),
            (Above_Ground, 'Above Ground'),
            (None, ''),
            ]
    Location =  models.CharField(
            help_text = _('Location'),
            max_length=200,
            choices = LOCATION_CHOICES,
            blank = True,
            )
    
    Specific_Location = models.TextField(
            help_text = _('Additional info of the location'),
            blank = True,
            )
    
    Running = models.BooleanField(
            null=True,
            blank=True,
            help_text = _('Running'),
            )
    
    Chasing = models.BooleanField(
            help_text = _('Chasing'),
            null=True,
            blank=True,
            )
    
    Climbing = models.BooleanField(
            help_text = _('Climbing'),
            null=True,
            blank=True,
            )
    
    Eating = models.BooleanField(
            help_text = _('Eating'),
            null=True,
            blank=True,
            )
    
    Foraging = models.BooleanField(
            help_text = _('Foraging'),
            null=True,
            blank=True,
            )
    
    Other_Activities = models.TextField(
            help_text = _('Other Activities'),
            null = True,
            blank = True,
        )
    
    Kuks = models.BooleanField(
            help_text = _('Kuks'),
            blank=True,
            null = True,
            )
    
    Quaas = models.BooleanField(
            help_text = _('Quaas'),
            blank=True,
            null = True,
            )
    
    Moans = models.BooleanField(
            help_text = _('Moans'),
            blank=True,
            null = True,
            )
    
    Tail_Flags = models.BooleanField(
            help_text = _('Tail_Flags'),
            blank=True,
            null = True,
            )
    
    Tail_Twitches = models.BooleanField(
            help_text = _('Tail_Twitches'),
            blank=True,
            null = True,
            )
    
    Approaches = models.BooleanField(
            help_text = _('Approaches'),
            blank=True,
            null = True, 
            )
    
    Indifferent = models.BooleanField(
            help_text = _('Indifferent'),
            blank=True,
            null = True, 
            )
    
    Runs_From = models.BooleanField(
            help_text = _('Runs_From'),
            blank=True,
            null = True, 
            )




    
    
