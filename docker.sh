#! /usr/bin/env bash

PORT='4243'

if [ "$(cat /etc/hostname)" = "sandbox" ]; then

  SCRIPT="$(readlink -f $0)"
  BASE="$(dirname $SCRIPT)"

  cd $BASE/pets

  if [ ! -e pets/local_settings.py ]; then
    cat > pets/local_settings.py <<ENDLINE
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
SECRET_KEY = '$(head /dev/urandom | md5sum | awk '{print $1}')'
ENDLINE
  fi

  if [ ! -e pets.db ]; then
    python manage.py syncdb
  fi

  if ! ls src/media/*.jpg >/dev/null 2>&1; then
    python manage.py get_animal
  fi

  python manage.py runserver 0.0.0.0:$PORT

else

  if sudo docker inspect petneed.me |& grep 'No such image'; then
    sudo docker build -t petneed.me - < Dockerfile
  fi
  sudo docker run -e LANG="en_US.UTF-8" -e LANGUAGE="en_US:en" -u 1000 -p $PORT:$PORT -v $PWD:/petneed.me -t -i petneed.me /petneed.me/docker.sh

fi
