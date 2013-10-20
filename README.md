# PetNeed.Me(寵物需要我) project
## How to setup develop environment
0.1 setting pip python etc
```
sudo apt-get install python-pip python-dev build-essential
sudo apt-get install sqlite3 python-dev libsqlite3-dev
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
```
0.2 for PIL recompile
for ubuntu:
```
sudo apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib/
sudo ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib/
sudo ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/lib/
pip install -I PIL
--i386 will replace to 'uname -i'
```

for mac:
```
brew install jpeg-turbo jpeg little-cms zlib freetype
```

Then you will see:
```
    --------------------------------------------------------------------
    PIL 1.1.7 SETUP SUMMARY
    --------------------------------------------------------------------
    version       1.1.7
    platform      linux2 2.7.3 (default, Apr 10 2013, 05:46:21)
                  [GCC 4.6.3]
    --------------------------------------------------------------------
    *** TKINTER support not available
    --- JPEG support available
    --- ZLIB (PNG/ZIP) support available
    --- FREETYPE2 support available
    *** LITTLECMS support not available
    --------------------------------------------------------------------
```

1.Install packages in python

```
pip install -r requirements.txt
```

2.create setup `pets/pets/local_settings.py` from template file `local_settings.py`

```
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
SECRET_KEY = '' #<-random string and don't share it with anybody.
```

3.Sync db

```
cd pets
python manage.py syncdb
```

4.Get initial pet's data from api

```
python manage.py get_animal
```

5.Run development Server !

```
python manage.py runserver
```

## Run by http://docker.io

### Install Vagrant

http://downloads.vagrantup.com

### Setup a VM via Vagrant

```
vagrant up
```

### Connect to the VM

```
vagrant ssh
```

### Setup the development environment and start the app.

```
vagrant@precise64:~$ cd /vagrant
vagrant@precise64:/vagrant$ ./docker.sh
```

## contributor
* JS Lee
* Yao
* Fion
* Jacob
* Willy
* Zoe
* TTcat
* $4
