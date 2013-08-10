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
FACEBOOK_APP_ID                   = ''
FACEBOOK_API_SECRET               = ''
```

5.Run development Server !
```
python manage.py runserver
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