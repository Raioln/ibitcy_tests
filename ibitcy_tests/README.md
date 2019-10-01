# About #
Ui тесты, поддерживают локальный запуск (необходимо установить хром драйвер и указать путь до него в settings.local)
и запуск через selenoid
## Install ##
1. Скачать репу тестами
2. установить python 3.6 и pipenv
3. pipenv shell
4. pipenv install --dev
5. установить docker (https://docs.docker.com/install/)
6 установить selenoid запустить его в докере 

```bash
curl -s https://aerokube.com/cm/bash 
chmod +x ./cm
./cm selenoid start --vnc
./cm selenoid-ui start
```
7. Запустить тесты одной из команд
tox -e chrome
tox -e firefox
tox -e opera

