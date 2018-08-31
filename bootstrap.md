## Prerequisites

nginx, python3.5

## Install pip3

```bash
sudo apt-get install python3-pip
```

## Install Django

```bash
sudo pip3 install Django
sudo pip3 install django-analytical
```

## Install and configure UWSGI

```bash
sudo apt install uwsgi uwsgi-src uuid-dev libcap-dev libpcre3-dev
export PYTHON=python3.5
uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python35"
sudo mv python35_plugin.so /usr/lib/uwsgi/plugins/python35_plugin.so
sudo chmod 644 /usr/lib/uwsgi/plugins/python35_plugin.so
```

## Links

```bash
sudo ln -s /path/to/proj /usr/local/ge/
sudo ln -s /usr/local/ge/glossary_nginx.conf /etc/nginx/sites-available/glossary_nginx.conf
```

Add
```
/usr/bin/uwsgi --daemonize /var/log/glossary_uwsgi.log --ini /usr/local/ge/glossary_uwsgi.ini
```

to /etc/rc.local

## Start

```bash
uwsgi /usr/local/ge/glossary_uwsgi.ini
sudo chmod 777 /tmp/glossary.sock
```
