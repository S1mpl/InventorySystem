# InventorySystem
Инструкция по deploy

Демо : <a href='http://86.110.118.96/'>http://86.110.118.96/</a>

Для начала нужно установить все зависимости из репозиториев: python, pip, Nginx, postgresql, git

```
sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx git postgresql postgresql-contrib
```

Измените пароль или создайте нового пользователя БД
Изменение пароля postgres

```
sudo -u postgres psql
  ALTER USER postgres with encrypted password 'your_password';
```

Создайте базу данных

```
sudo -u postgres createdb datacenter
```

Перейдем в папку www
```
cd /var/www
```
Удалим в ней папаку html
```
sudo rm -r html
```

Создаем виртуальную среду
```
sudo pip3 install virtualenv
sudo mkdir inventory
cd inventory
sudo virtualenv env
source env/bin/activate
```

Установка приложения
```
sudo git clone 
https://github.com/S1mpl/InventorySystem.git
cd InventorySystem
sudo pip install uwsgi gunicorn 
cd InventorySystem
sudo pip install -r requirements.txt
```
В файле config.py настроить подключение к БД

Миграция в БД
```
sudo python3 manage.py db init
sudo python3 manage.py db migrate
sudo python3 manage.py db upgrade
```

Запуск тествого сервера(для проверки)
```
sudo python manage.py runserver
```

Выходим из витеальной среды
```
deactivate
```

Создать файл
```
sudo nano /etc/systemd/system/server.service
```

Вставить в него
```
[Unit]
Description=uWSGI 
After=network.target
[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/inventory/InventorySystem
Environment="PATH=/var/www/inventory/env/bin"
ExecStart=/var/www/inventory/env/bin/uwsgi --ini server.ini
[Install]
WantedBy=multi-user.target
```

Запускаем uwsgi
```
sudo systemctl start server
sudo systemctl enable server
```

nginx
```
sudo nano /etc/nginx/sites-available/server

server {
  listen 80;
  server_name IP;
  location / {
    include uwsgi_params;
    uwsgi_pass unix:/var/www/inventory/InventorySystem/server.sock;
  }
}
```

Далее
```
sudo ln -s /etc/nginx/sites-available/server /etc/nginx/sites-enabled
```

Перезапускаем Nginx
```
sudo systemctl restart nginx
```
