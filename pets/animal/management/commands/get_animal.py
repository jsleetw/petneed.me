from django.core.management.base import BaseCommand
from animal.models import Animal
import json
import urllib2
import os
import Image


class Command(BaseCommand):
    args = '<>'
    help = 'get animal data from http://data.taipei.gov.tw'
    url = "http://163.29.39.183/GetAnimals.aspx"

    def handle(self, *args, **options):
        print self.url
        data = urllib2.urlopen(self.url)
        j = json.load(data)
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
                f.path = "src/media/" + url_file
                f.url = url_file
                print self.thumbnail(f, "248x350")
                print self.thumbnail(f, "248x350", True)
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

    def thumbnail(self, file, size='104x104', x2=False):
        # defining the size
        x, y = [int(x) for x in size.split('x')]
        # defining the filename and the miniature filename
        filehead, filetail = os.path.split(file.path)
        basename, format = os.path.splitext(filetail)
        miniature = basename + '_' + size + format
        if x2:
            miniature = basename + '_' + size + '@2x' + format
        filename = file.path
        miniature_filename = os.path.join(filehead, miniature)
        filehead, filetail = os.path.split(file.url)
        miniature_url = filehead + '/' + miniature
        if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
            os.unlink(miniature_filename)
        # if the image wasn't already resized, resize it
        if not os.path.exists(miniature_filename):
            image = Image.open(filename)
            image.thumbnail([x, y], Image.ANTIALIAS)
            try:
                image.save(miniature_filename, image.format, quality=90, optimize=1)
            except:
                image.save(miniature_filename, image.format, quality=90)

        return miniature_url
