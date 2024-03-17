### Инструкция по запуску

Создать виртуальное окружение
```commandline
python3.11 -m venv venv (Linux)
py -3.11 -m venv venv (Windows)
```

Активировать 
```commandline
source venv/bin/activate (Linux)
venv\Scripts\activate.bat (Windows)
```

Установить необходимые библиотеки 
```commandline
pip install -r requirements.txt
```

Создать .env файл
```commandline
cp .env.example .env
```

Запустить проект
```commandline
./run.sh
```


#### Проект будет запущен по адресу http://localhost:8001/
#### Документация OpenAPI http://localhost:8001/docs

### Этапы анализа

1. Поиск аномальных значений
2. Проверка на стационарность
3. Проверка наличия автокорреляции
4. Нахождение тренда (линейного или сезонного)
