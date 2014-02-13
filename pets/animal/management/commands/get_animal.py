from django.core.management.base import BaseCommand
from animal.models import Animal
from animal.utils import thumbnail
import json
import urllib2
import os
import urllib
import Image

class Command(BaseCommand):
    args = '<>'
    help = 'get animal data from http://data.taipei.gov.tw'
    url1 = "http://163.29.39.183/GetAnimals.aspx"
    params = urllib.urlencode({'resource_id': 'c57f54e2-8ac3-4d30-bce0-637a8968796e'})
    url2 = "http://60.199.253.136/api/action/datastore_search" + '?' + params

    def handle(self, *args, **options):
        print self.url2
        data = urllib2.urlopen(self.url2)
        j = json.load(data)
        j = j["result"]["records"]
        for i in j:
            print (i["Name"]).encode('utf-8')
            a1 = Animal.objects.filter(accept_num=i["AcceptNum"])
            print a1
            if not a1:
                url = i["ImageName"]
                url_file = url.split("/")[-1]
                f = urllib2.urlopen(url)
                data = f.read()
                with open("src/media/" + url_file, "wb") as code:
                    code.write(data)
                print thumbnail("src/media/" + url_file, "248x350")
                print thumbnail("src/media/" + url_file, "248x350", True)
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
                           image_file=url_file,)
                a.save()
        self.stdout.write('end\n')
        print self.url1
        data = urllib2.urlopen(self.url1)
        j = json.load(data)
        #j = j["result"]["records"]
        for i in j:
            print (i["Name"]).encode('utf-8')
            a1 = Animal.objects.filter(accept_num=i["AcceptNum"])
            print a1
            if not a1:
                url = i["ImageName"]
                url_file = url.split("/")[-1]
                f = urllib2.urlopen(url)
                data = f.read()
                with open("src/media/" + url_file, "wb") as code:
                    code.write(data)
                print thumbnail("src/media/" + url_file, "248x350")
                print thumbnail("src/media/" + url_file, "248x350", True)
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
                           image_file=url_file,)
                a.save()
        self.stdout.write('end\n')
