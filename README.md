# InventorySystem
Инструкция по deploy

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
sudo pip install uwsgi
sudo pip install -r requirements.txt
```
В файле config.py настроить подключение к БД

Миграция в БД
```
sudo python3 migate.py db init
sudo python3 migate.py db migrate
sudo python3 migate.py db upgrade
```

Выходим из витеальной среды
```
deactivate
```
Отредактировать файлы
```
sudo nano server.ini
```

Создать файл
```
sudo nano /etc/systemd/system/server.service
```

Вставить в него
```
[Unit]
Description=uWSGI instance to serve myproject
After=network.target
[Service]
User=8host
Group=www-data
WorkingDirectory=/var/www/inventory/InventorySyste/
Environment="PATH=/var/www/inventory/env/bin"
ExecStart=/var/www/inventory/env/bin/uwsgi --ini server.ini
[Install]
WantedBy=multi-user.target
```

Запускаем iwsgi
```
sudo systemctl start server
sudo systemctl enable server
```

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
