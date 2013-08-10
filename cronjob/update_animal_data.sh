#!/bin/sh
DJANGO_SETTINGS_MODULE=pets.settings
export DJANGO_SETTINGS_MODULE

PYTHONPATH=/home/ail/Envs/pets/lib/python2.7:/home/ail/mydev/pets/pets
export PYTHONPATH

#/path/to/python /path/to/my_django_script
/home/ail/Envs/pets/bin/python /home/ail/mydev/pets/pets/manage.py get_animal
