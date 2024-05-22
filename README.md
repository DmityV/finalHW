## О проекте:

Проект блога сделан в рамках итогово домашнего задания.
В проекте фронтенд на vue.js, бэкенд на django.
Вместе с проектом для удобства также устанавливаются: база данных sqlite с образцами постов и директория /dist фронтенда с собранной частью фронтенда.

## Как запустить проект:

#### Клонировать репозиторий и перейти в него, выполнив следующие команды в командной строке:

```
git clone https://github.com/DmityV/finalHW.git
```


#### Далее в командной строке:

Перейти в директорию проекта

```
cd finalHW
```

Cоздать и активировать виртуальное окружение:

Windows
```
python -m venv env
source env/Scripts/activate
```
Linux/macOS
```
python3 -m venv env
source env/bin/activate
```

Обновить PIP:

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в директорию бэкенда

```
cd blog_backend
```

Запустить проект:

Windows

```
python manage.py runserver
```

Linux/macOS

```
python3 manage.py runserver
```

В браузере перейти на страницу http://127.0.0.1:8000/
