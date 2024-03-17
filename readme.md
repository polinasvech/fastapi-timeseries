### Информационная система для анализа временных рядов
- Flask
- база данных реляционная (SQL)
- Что требуется: 
  1. Авторизация пользователя по "Логин и пароль"
  2. "Загрузить дата сет", загружается csv файл
  3. Должна присутствовать кнопка "История вычислений" (что пользователь вводил, результат)
  

### Этапы анализа

1. Поиск аномальных значений
2. Проверка на стационарность
3. Проверка наличия автокорреляции
4. Нахождение тренда (линейного или сезонного)


### Для запуска 

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
