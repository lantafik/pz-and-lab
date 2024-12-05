#Импортируем библиотеку requests
import requests


# Задание 1
#Отправляем GET-запрос к API GitHub с параметром поиска репозиториев с кодом html
url = "https://api.github.com/search/repositories"
params = {
    "q": "html+language:html",  # Ищем репозитории с кодом html
}

response = requests.get(url, params=params)

#Cтатус-код ответа
print("Статус-код ответа:", response.status_code)

#Cодержимое ответа в формате JSON
print("Содержимое ответа (JSON):")
print(response.json())


# Задание 2
#URL для API jsonplaceholder
url = "https://jsonplaceholder.typicode.com/posts"

#Параметры запроса
params = {
    "userId": 1  # Фильтруем записи по userId, равному 1
}

#Отправляем GET-запрос с параметрами
response = requests.get(url, params=params)

#Проверяем статус-код ответа
if response.status_code == 200:
    #Распечатываем полученные записи в формате JSON
    posts = response.json()
    print("Полученные записи:")
    for post in posts:
        print(f"ID: {post['id']}, Заголовок: {post['title']}")
else:
    print("Ошибка при запросе:", response.status_code)


# Задание 3
#URL для API jsonplaceholder (для создания нового поста)
url = "https://jsonplaceholder.typicode.com/posts"

#Словарь с данными
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

#Отправляем POST-запрос с данными
response = requests.post(url, json=data)

#Распечатываем статус-код ответа
print("Статус-код ответа:", response.status_code)

#Распечатываем содержимое ответа
print("Содержимое ответа:", response.json())
