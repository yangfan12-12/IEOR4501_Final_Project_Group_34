import csv

import datetime

from distutils.util import strtobool

from django.core.management.base import BaseCommand

from sightings.models import Sighting




class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        Sighting.objects.all().delete() 
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            rows = list(reader)
        

        for row in rows:
        
            s = Sighting(
                    Longitude=row['X'],
                    Latitude=row['Y'],
                    Unique_Squirrel_Id=row['Unique Squirrel ID'],
                    Shift=row['Shift'],
                    Date=datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                    Age=row['Age'],
                    Primary_Fur_Color=row['Primary Fur Color'],
                    Location=row['Location'],
                    Specific_Location=row['Specific Location'],
                    Running=strtobool(row['Running']),
                    Chasing=strtobool(row['Chasing']),
                    Climbing=strtobool(row['Climbing']),
                    Eating=strtobool(row['Eating']),
                    Foraging= strtobool(row['Foraging']),
                    Other_Activities=row['Other Activities'],
                    Kuks=strtobool(row['Kuks']),
                    Quaas=strtobool(row['Quaas']),
                    Moans=strtobool(row['Moans']),
                    Tail_Flags=strtobool(row['Tail flags']),
                    Tail_Twitches=strtobool(row['Tail twitches']),
                    Approaches=strtobool(row['Approaches']),
                    Indifferent=strtobool(row['Indifferent']),
                    Runs_From=strtobool(row['Runs from']),
            )
            s.save()
        
