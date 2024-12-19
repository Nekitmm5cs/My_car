import requests

# URL для API, который возвращает последние новости
api_url = "https://www.imsa.com/wp-json/wp/v2/posts"

# Заголовки для имитации запроса от браузера
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

# Выполняем GET-запрос к API с заголовками
response = requests.get(api_url, headers=headers)

# Проверяем, успешен ли запрос
if response.status_code == 200:
    # Парсим JSON-ответ
    news_items = response.json()
    
    # Печатаем заголовки новостей
    for item in news_items:
        print(item['title']['rendered'])  # Заголовок статьи
else:
    print("Ошибка при запросе:", response.status_code)
