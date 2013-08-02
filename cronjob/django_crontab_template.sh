#!/bin/sh
DJANGO_SETTINGS_MODULE=mysettings
export DJANGO_SETTINGS_MODULE

PYTHONPATH=/path/to/python_libs:/path/to/my_django_apps
export PYTHONPATH

/path/to/python /path/to/my_django_script
