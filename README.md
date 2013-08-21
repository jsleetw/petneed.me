# PetNeed.Me(寵物需要我) project

## How to setup develop environment

1.Install packages in python

```
pip install -r pip_package.txt
```

2.Sync db

```
cd pets
python manage.py syncdb
```

3.Get initial pet's data from api

```
python manage.py get_animal
```

4.setup local_setting
```
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
SECRET_KEY = '' <-random string and don't share it with anybody.
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
