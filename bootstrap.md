## Prerequisites

nginx, python3.5

## Install virtualenv

```bash
pip3 install virtualenv
```

## Install Django

```bash
virtualenv -p python3 env
source env/bin/activate
python3 -m pip install --upgrade pip
pip install Django
pip install django-analytical
pip install markdown
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
sudo ln -s /path/to/proj /usr/local/ge
sudo ln -s /usr/local/ge/glossary_nginx.conf /etc/nginx/sites-available/glossary_nginx.conf
sudo ln -s /usr/local/ge/uwsgi.service /etc/systemd/system/uwsgi.service
sudo ln -s /usr/local/ge/glossary_uwsgi.ini /etc/uwsgi/apps-available/glossary_uwsgi.ini
sudo ln -s /etc/uwsgi/apps-available/glossary_uwsgi.ini /etc/uwsgi/apps-enabled/glossary_uwsgi.ini
sudo ln -s /path/to/glossary_texts_sources /usr/local/ge/gt
sudo ln -s /path/to/glossary_texts /usr/local/ge/server/gt
```

## Start

```bash
cd /usr/local/ge/server/ && python3 build_index.py
sudo service uwsgi start
sudo service nginx start
```
