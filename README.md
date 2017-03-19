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

Создим виртуальную среду
```
sudo pip3 install virtualenv
sudo mkdir inventory
cd inventory
```
