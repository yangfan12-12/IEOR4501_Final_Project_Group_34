import csv

import datetime

from django.core.management.base import BaseCommand

from sightings.models import Sighting

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
    
        with open(options['path'],'w') as fp:
            export_squirrels_writer = csv.DictWriter(
                    fp, 
                    delimiter=',',
                    fieldnames=[
                        'X',
                        'Y',
                        'Unique Squirrel ID',
                        'Shift',
                        'Date',
                        'Age',
                        'Primary Fur Color',
                        'Location',
                        'Specific Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail flags',
                        'Tail twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs from'
                        ]
                    )
            export_squirrels_writer.writeheader()
    
            for row in Sighting.objects.all():
                if row.Date: 
                    date_ = row.Date.strftime('%m%d%Y')
                else:
                    date_ = row.Date

                export_squirrels_writer.writerow({
                    'X':row.Longitude,
                    'Y':row.Latitude,
                    'Unique Squirrel ID':row.Unique_Squirrel_Id,
                    'Shift':row.Shift,
                    'Date':date_,
                    'Age':row.Age,
                    'Primary Fur Color':row.Primary_Fur_Color,
                    'Location':row.Location,
                    'Specific Location':row.Specific_Location,
                    'Running':row.Running,
                    'Chasing':row.Chasing,
                    'Climbing':row.Climbing,
                    'Eating':row.Eating,
                    'Foraging':row.Foraging,
                    'Other Activities':row.Other_Activities,
                    'Kuks':row.Kuks,
                    'Quaas':row.Quaas,
                    'Moans':row.Moans,
                    'Tail flags':row.Tail_Flags,
                    'Tail twitches':row.Tail_Twitches,
                    'Approaches':row.Approaches,
                    'Indifferent':row.Indifferent,
                    'Runs from':row.Runs_From,          
                    })
