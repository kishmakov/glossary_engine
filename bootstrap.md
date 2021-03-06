## Prerequisites

nginx, python3.6

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
export PYTHON=python3.6
uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python36"
sudo mv python36_plugin.so /usr/lib/uwsgi/plugins/python36_plugin.so
sudo chmod 644 /usr/lib/uwsgi/plugins/python36_plugin.so
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

### Logrotate

```bash
sudo ln -s /usr/local/ge/glossary_logrotate.conf /etc/logrotate.d/glossary
sudo chown root:root /usr/local/ge/glossary_logrotate.conf
sudo chmod 644 /usr/local/ge/glossary_logrotate.conf
sudo chown www-data:www-data /var/log/glossary.log
```

Check it works:

```bash
sudo logrotate -d --force /etc/logrotate.d/glossary
```

## Start

```bash
cd /usr/local/ge/server/ && python3 build_index.py
sudo service uwsgi start
sudo service nginx start
```
