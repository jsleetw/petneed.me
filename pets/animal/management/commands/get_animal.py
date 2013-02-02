from django.core.management.base import BaseCommand, CommandError
from animal.models import Animal
import json
import urllib2
import time

class Command(BaseCommand):
    args = '<>'
    help = 'get animal data from http://data.taipei.gov.tw'
    url = 'http://163.29.39.183/GetAnimals.aspx'

    def handle(self, *args, **options):
        print self.url
        data = urllib2.urlopen(self.url)
        j = json.load(data)
        #print j
        #print j[0]["AcceptNum"]
        #print j[0]["Name"]
        for i in j:
            print i["AcceptNum"]
            print i["Name"]
            a = Animal(name=i["Name"],
                       sex=i["Sex"],
                       type=i["Type"],
                       build=i["Build"],
                       age=i["Age"],
                       variety=i["Variety"],
                       reason=i["Reason"],
                       accept_num=i["AcceptNum"],
                       chip_num=i["ChipNum"],
                       is_sterilization=i["IsSterilization"],
                       hair_type=i["HairType"],
                       note=i["Note"],
                       resettlement=i["Resettlement"],
                       phone=i["Phone"],
                       email=i["Email"],
                       childre_anlong=i["ChildreAnlong"],
                       animal_anlong=i["AnimalAnlong"],
                       bodyweight=i["Bodyweight"],
                       image_name=i["ImageName"],
                       )
            a.save()
        self.stdout.write('end\n')
