FROM ubuntu:latest

# Set a default language
RUN echo 'Acquire::Languages {"none";};' > /etc/apt/apt.conf.d/60language
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale
RUN echo 'LANGUAGE="en_US:en"' >> /etc/default/locale
RUN locale-gen en_US.UTF-8
RUN update-locale en_US.UTF-8

# Set APT source lists
RUN echo "# foreign-architecture i386" > /etc/dpkg/dpkg.cfg.d/multiarch
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main restricted universe multiverse" > /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu precise-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu precise-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python-pip python-dev gcc libsqlite3-dev git vim man
RUN apt-get install -y libfreetype6-dev zlib1g-dev libjpeg-turbo8-dev liblcms1-dev
RUN ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/
RUN ln -s /usr/lib/x86_64-linux-gnu/liblcms.so /usr/lib/
RUN pip install Django==1.5.3
RUN pip install PIL==1.1.7
RUN pip install argparse==1.2.1
RUN pip install django-appconf==0.6
RUN pip install django-compressor==1.2
RUN pip install flake8==1.7.0
RUN pip install gunicorn==0.17.2
RUN pip install pysqlite==2.6.3
RUN pip install six==1.2.0
RUN pip install wsgiref==0.1.2
RUN pip install django-social-auth==0.7.25

# Setup a default user
RUN useradd -u 1000 ubuntu
