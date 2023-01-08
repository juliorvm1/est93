#Steps
```sh
git clone
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt update
sudo apt install mysql-server
sudo service mysql start
sudo mysql -u root -p;
create database dbEst93;
create user 'uEst93'@'localhost' indentified by 'ianr';
grant all on dbEst93.* to 'uEst93'@'localhost';

